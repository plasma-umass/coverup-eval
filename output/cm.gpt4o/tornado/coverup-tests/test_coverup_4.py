# file tornado/options.py:524-549
# lines [524, 527, 528, 529, 530, 531, 532, 533, 534, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549]
# branches ['536->537', '536->538', '539->540', '539->541']

import pytest
from unittest import mock

# Assuming the _Option class is imported from tornado.options
from tornado.options import _Option

def test_option_initialization():
    # Test case to cover the branch where type is None
    with pytest.raises(ValueError, match="type must not be None"):
        _Option(name="test_option", type=None)

    # Test case to cover the branch where default is None and multiple is True
    option = _Option(name="test_option", type=str, multiple=True)
    assert option.default == []

    # Test case to cover normal initialization
    callback_mock = mock.Mock()
    option = _Option(
        name="test_option",
        default="default_value",
        type=str,
        help="help text",
        metavar="metavar",
        multiple=False,
        file_name="file_name",
        group_name="group_name",
        callback=callback_mock,
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
