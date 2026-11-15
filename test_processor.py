
import pytest
from hypothesis import given, strategies as st

from processor import (
    calculate_dimensional_weight,
    format_tracking_label,
    parse_package_manifest
)


# 1. Fuzz testing: Dimensional Weight
@given(st.text() | st.none())
def test_calculate_dimensional_weight_no_crash(s):
    try:
        calculate_dimensional_weight(s)
    except Exception as error:
        pytest.fail(
            f"Dimensional weight function crashed for {s!r}: {error}"
        )


# 2. Fuzz testing: Tracking Label
@given(st.text() | st.none())
def test_format_tracking_label_safe(s):
    try:
        format_tracking_label(s)
    except Exception as error:
        pytest.fail(
            f"Tracking label function crashed for {s!r}: {error}"
        )


# 3. Fuzz testing: Package Manifest
@given(st.text() | st.none())
def test_parse_package_manifest_safe(s):
    try:
        parse_package_manifest(s)
    except Exception as error:
        pytest.fail(
            f"Manifest parser crashed for {s!r}: {error}"
        )


# 4. Normal test: Valid Dimensional Weight
def test_valid_dimensional_weight():
    assert calculate_dimensional_weight("20x30x10") == 1.2


# 5. Normal test: Valid Tracking Label
def test_valid_tracking_label():
    assert format_tracking_label("E123") == "E-000123"


# 6. Normal test: Valid Package Manifest
def test_valid_package_manifest():
    assert parse_package_manifest('{"weight": 12.5}') == 12.5
