"""ESP32-S3 memory-bus and silicon-hole regressions.

Every expectation here is pinned to ESP-IDF v5.5.1 sources rather than to
vendor marketing tables:

* ``SOC_GPIO_VALID_GPIO_MASK`` (components/soc/esp32s3/include/soc/soc_caps.h)
  excludes BIT22..BIT25 — GPIO22-25 do not exist on S3.
* ``SOC_GPIO_VALID_OUTPUT_GPIO_MASK == SOC_GPIO_VALID_GPIO_MASK`` on S3, so the
  S2-only input-only GPIO46 restriction must not be applied to S3.
* The ESP32-S3 GPIO reference states that with octal flash or octal PSRAM,
  GPIO33-37 carry SPIIO4..SPIIO7 and SPIDQS.
* ``SOC_LEDC_CHANNEL_NUM`` is 8 on S2/S3 (16 on the original ESP32 across its
  high-speed and low-speed groups).
"""

import json

from platforms import ConflictType, get_platform


# In-package octal PSRAM takes SPIIO6/SPIIO7/SPIDQS; GPIO33/34 (SPIIO4/5) are
# only claimed by an octal *flash* and are not bonded out on WROOM-1 at all.
OCTAL_PSRAM_PINS = [35, 36, 37]
OCTAL_FLASH_PINS = [33, 34]


def _assignment(pins, **kwargs):
    base = {"platform": "esp32", "variant": "esp32s3", "pins": pins}
    base.update(kwargs)
    return base


def _codes(findings):
    return [f["code"] for f in findings]


class TestInputOnly:
    def test_gpio46_can_drive_output_on_s3(self):
        """GPIO46 drives an RGB data line on real S3 boards (Pregmate MAIN A1)."""
        platform = get_platform("esp32", variant="esp32s3")
        result = platform.validate(_assignment(
            [{"gpio": 46, "function": "RGB_R0", "direction": "output"}]
        ))
        assert result.valid, result.errors
        assert ConflictType.INPUT_ONLY.value not in _codes(result.errors)

    def test_gpio46_stays_input_only_on_s2(self):
        platform = get_platform("esp32", variant="esp32s2")
        result = platform.validate({
            "platform": "esp32", "variant": "esp32s2",
            "pins": [{"gpio": 46, "function": "LED", "direction": "output"}],
        })
        assert not result.valid
        assert ConflictType.INPUT_ONLY.value in _codes(result.errors)


class TestSiliconHoles:
    def test_gpio22_to_25_rejected_on_s3(self):
        platform = get_platform("esp32", variant="esp32s3")
        for gpio in (22, 23, 24, 25):
            result = platform.validate(_assignment(
                [{"gpio": gpio, "function": "LED", "direction": "output"}]
            ))
            assert not result.valid, f"GPIO{gpio} must be rejected on S3"
            assert ConflictType.INVALID_GPIO.value in _codes(result.errors)

    def test_valid_gpio_ranges_are_reported(self):
        platform = get_platform("esp32", variant="esp32s3")
        result = platform.validate(_assignment(
            [{"gpio": 23, "function": "LED", "direction": "output"}]
        ))
        assert "0-21, 26-48" in result.errors[0]["message"]

    def test_pin_database_skips_holes(self):
        platform = get_platform("esp32", variant="esp32s3")
        numbers = {pin.gpio_num for pin in platform.get_all_pins()}
        assert numbers.isdisjoint({22, 23, 24, 25})
        assert {0, 21, 26, 48} <= numbers


class TestOctalMemoryBus:
    def test_octal_module_reserves_psram_pins(self):
        platform = get_platform("esp32", variant="esp32s3",
                                module="ESP32-S3-WROOM-1-N16R8")
        assert platform.psram == "octal"
        for gpio in OCTAL_PSRAM_PINS:
            result = platform.validate(_assignment(
                [{"gpio": gpio, "function": "SENSOR_EN", "direction": "output"}],
                module="ESP32-S3-WROOM-1-N16R8",
            ))
            assert not result.valid, f"GPIO{gpio} must be rejected on an octal module"
            assert ConflictType.PSRAM_PIN.value in _codes(result.errors)

    def test_wroom1_does_not_bond_gpio33_34(self):
        """WROOM-1/1U pin table: the module brings out GPIO35-48, never 33/34."""
        platform = get_platform("esp32", variant="esp32s3",
                                module="ESP32-S3-WROOM-1-N16R8")
        for gpio in OCTAL_FLASH_PINS:
            result = platform.validate(_assignment(
                [{"gpio": gpio, "function": "SENSOR_EN", "direction": "output"}],
                module="ESP32-S3-WROOM-1-N16R8",
            ))
            assert not result.valid
            assert ConflictType.RESERVED_PIN.value in _codes(result.errors)

    def test_bare_chip_warns_on_spiio4_5_instead_of_failing(self):
        """On a bare S3 die GPIO33/34 are usable unless the flash is octal."""
        platform = get_platform("esp32", variant="esp32s3",
                                module="ESP32-S3R8", psram="octal")
        result = platform.validate(_assignment(
            [{"gpio": 33, "function": "SENSOR_EN", "direction": "output"}],
            module="ESP32-S3R8", psram="octal",
        ))
        assert result.valid, result.errors
        assert ConflictType.PSRAM_PIN.value in _codes(result.warnings)

    def test_v_part_flags_1v8_spi_clock_pins(self):
        """GPIO47/48 swing 1.8 V on R8V/R16V parts — the Pregmate panel uses both."""
        platform = get_platform("esp32", variant="esp32s3",
                                module="ESP32-S3-WROOM-1-N16R16V")
        result = platform.validate(_assignment(
            [{"gpio": 47, "function": "RGB_B3", "direction": "output"}],
            module="ESP32-S3-WROOM-1-N16R16V",
        ))
        assert result.valid, result.errors
        messages = " ".join(w["message"] for w in result.warnings)
        assert "1.8 V" in messages

    def test_non_v_part_has_no_voltage_warning(self):
        platform = get_platform("esp32", variant="esp32s3",
                                module="ESP32-S3-WROOM-1-N16R8")
        result = platform.validate(_assignment(
            [{"gpio": 47, "function": "RGB_B3", "direction": "output"}],
            module="ESP32-S3-WROOM-1-N16R8",
        ))
        messages = " ".join(w["message"] for w in result.warnings)
        assert "1.8 V" not in messages

    def test_explicit_psram_field_overrides_module_name(self):
        platform = get_platform("esp32", variant="esp32s3", module="WROOM",
                                psram="octal")
        result = platform.validate(_assignment(
            [{"gpio": 35, "function": "SENSOR_EN", "direction": "output"}],
            psram="octal",
        ))
        assert platform.psram == "octal"
        assert not result.valid

    def test_unknown_module_warns_instead_of_approving(self):
        """The script default module="WROOM" is meaningless on S3 — warn."""
        platform = get_platform("esp32", variant="esp32s3", module="WROOM")
        assert platform.psram == "unknown"
        result = platform.validate(_assignment(
            [{"gpio": 35, "function": "SENSOR_EN", "direction": "output"}]
        ))
        assert result.valid, result.errors
        assert ConflictType.PSRAM_PIN.value in _codes(result.warnings)

    def test_quad_module_leaves_pins_free(self):
        platform = get_platform("esp32", variant="esp32s3",
                                module="ESP32-S3-WROOM-1-N8R2")
        assert platform.psram == "quad"
        result = platform.validate(_assignment(
            [{"gpio": 35, "function": "SENSOR_EN", "direction": "output"}],
            module="ESP32-S3-WROOM-1-N8R2",
        ))
        assert result.valid, result.errors
        assert ConflictType.PSRAM_PIN.value not in _codes(result.warnings)

    def test_flash_only_module_leaves_pins_free(self):
        platform = get_platform("esp32", variant="esp32s3",
                                module="ESP32-S3-WROOM-1-N8")
        assert platform.psram == "none"

    def test_original_esp32_wrover_still_reserves_gpio16_17(self):
        platform = get_platform("esp32", variant="esp32", module="WROVER")
        assert platform.psram == "quad"
        result = platform.validate({
            "platform": "esp32", "variant": "esp32", "module": "WROVER",
            "pins": [{"gpio": 16, "function": "LED", "direction": "output"}],
        })
        assert not result.valid
        assert ConflictType.PSRAM_PIN.value in _codes(result.errors)


class TestLedcChannels:
    def test_s3_caps_at_eight_channels(self):
        platform = get_platform("esp32", variant="esp32s3")
        pins = [{"gpio": g, "function": f"PWM{g}", "protocol_bus": "pwm",
                 "direction": "output"} for g in (1, 2, 4, 5, 6, 7, 8, 9, 10)]
        result = platform.validate(_assignment(pins))
        messages = " ".join(w["message"] for w in result.warnings)
        assert "max 8 LEDC channels" in messages

    def test_original_esp32_keeps_sixteen_channels(self):
        platform = get_platform("esp32", variant="esp32")
        pins = [{"gpio": g, "function": f"PWM{g}", "protocol_bus": "pwm",
                 "direction": "output"} for g in range(16, 24)]
        result = platform.validate({
            "platform": "esp32", "variant": "esp32", "module": "WROOM",
            "pins": pins,
        })
        messages = " ".join(w["message"] for w in result.warnings)
        assert "LEDC channels" not in messages


class TestPregmateBoardFixture:
    def test_real_board_pinmap_is_valid(self, fixtures_dir):
        """The shipping Pregmate MAIN A1 pinmap must pass as-is."""
        data = json.loads(
            (fixtures_dir / "board_pregmate_main_a1.json").read_text()
        )
        platform = get_platform("esp32", variant="esp32s3",
                                module=data["module"], psram=data["psram"])
        result = platform.validate(data)
        assert result.valid, result.errors

    def test_real_board_flags_only_strapping_pins(self, fixtures_dir):
        data = json.loads(
            (fixtures_dir / "board_pregmate_main_a1.json").read_text()
        )
        platform = get_platform("esp32", variant="esp32s3",
                                module=data["module"], psram=data["psram"])
        result = platform.validate(data)
        warned = {w["gpio"] for w in result.warnings}
        assert warned == {3, 45, 46}, result.warnings
