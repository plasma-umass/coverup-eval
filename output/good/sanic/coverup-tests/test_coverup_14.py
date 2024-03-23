# file sanic/utils.py:13-42
# lines [13, 25, 26, 38, 39, 40, 42]
# branches ['26->38', '26->39', '39->40', '39->42']

import pytest

from sanic.utils import str_to_bool

@pytest.mark.parametrize("true_val", [
    "y", "yes", "yep", "yup", "t", "true", "on", "enable", "enabled", "1",
    "Y", "YES", "YEP", "YUP", "T", "TRUE", "ON", "ENABLE", "ENABLED"
])
def test_str_to_bool_true(true_val):
    assert str_to_bool(true_val) is True

@pytest.mark.parametrize("false_val", [
    "n", "no", "f", "false", "off", "disable", "disabled", "0",
    "N", "NO", "F", "FALSE", "OFF", "DISABLE", "DISABLED"
])
def test_str_to_bool_false(false_val):
    assert str_to_bool(false_val) is False

@pytest.mark.parametrize("invalid_val", [
    "maybe", "2", "yesno", "truefalse", "", "null", "none", "undefined"
])
def test_str_to_bool_invalid(invalid_val):
    with pytest.raises(ValueError):
        str_to_bool(invalid_val)
