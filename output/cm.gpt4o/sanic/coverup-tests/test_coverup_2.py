# file sanic/utils.py:13-42
# lines [13, 25, 26, 38, 39, 40, 42]
# branches ['26->38', '26->39', '39->40', '39->42']

import pytest
from sanic.utils import str_to_bool

def test_str_to_bool_true_values():
    true_values = [
        "y", "yes", "yep", "yup", "t", "true", "on", "enable", "enabled", "1"
    ]
    for val in true_values:
        assert str_to_bool(val) is True

def test_str_to_bool_false_values():
    false_values = [
        "n", "no", "f", "false", "off", "disable", "disabled", "0"
    ]
    for val in false_values:
        assert str_to_bool(val) is False

def test_str_to_bool_invalid_value():
    with pytest.raises(ValueError, match="Invalid truth value invalid"):
        str_to_bool("invalid")
