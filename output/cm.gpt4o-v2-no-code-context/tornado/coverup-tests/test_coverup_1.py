# file: tornado/options.py:524-549
# asked: {"lines": [524, 527, 528, 529, 530, 531, 532, 533, 534, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549], "branches": [[536, 537], [536, 538], [539, 540], [539, 541]]}
# gained: {"lines": [524, 527, 528, 529, 530, 531, 532, 533, 534, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549], "branches": [[536, 537], [536, 538], [539, 540], [539, 541]]}

import pytest
from unittest.mock import Mock

# Assuming the _Option class is imported from tornado.options
from tornado.options import _Option

def test_option_initialization_with_default_none_and_multiple_true():
    option = _Option(
        name="test_option",
        default=None,
        type=str,
        multiple=True
    )
    assert option.default == []

def test_option_initialization_with_type_none():
    with pytest.raises(ValueError, match="type must not be None"):
        _Option(
            name="test_option",
            default=None,
            type=None
        )

def test_option_initialization_with_all_parameters():
    callback_mock = Mock()
    option = _Option(
        name="test_option",
        default="default_value",
        type=str,
        help="help text",
        metavar="metavar",
        multiple=False,
        file_name="file_name",
        group_name="group_name",
        callback=callback_mock
    )
    assert option.name == "test_option"
    assert option.default == "default_value"
    assert option.type == str
    assert option.help == "help text"
    assert option.metavar == "metavar"
    assert option.multiple is False
    assert option.file_name == "file_name"
    assert option.group_name == "group_name"
    assert option.callback == callback_mock
    assert option._value == _Option.UNSET
