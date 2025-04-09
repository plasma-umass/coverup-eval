# file: tornado/options.py:217-302
# asked: {"lines": [217, 220, 221, 222, 223, 224, 225, 226, 262, 263, 264, 265, 266, 268, 269, 273, 274, 275, 277, 279, 280, 281, 282, 283, 284, 286, 287, 288, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 302], "branches": [[263, 264], [263, 268], [273, 277], [273, 279], [280, 281], [280, 282], [282, 283], [282, 287], [283, 284], [283, 286], [287, 288], [287, 290]]}
# gained: {"lines": [217, 220, 221, 222, 223, 224, 225, 226, 262, 263, 264, 265, 266, 268, 269, 273, 274, 275, 279, 280, 281, 282, 283, 284, 287, 288, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 302], "branches": [[263, 264], [263, 268], [273, 279], [280, 281], [280, 282], [282, 283], [282, 287], [283, 284], [287, 288], [287, 290]]}

import pytest
from tornado.options import OptionParser, _Option

@pytest.fixture
def option_parser():
    return OptionParser()

def test_define_new_option(option_parser):
    option_parser.define("test_option", default=42, type=int, help="A test option", metavar="TEST", multiple=False, group="test_group")
    normalized_name = option_parser._normalize_name("test_option")
    assert normalized_name in option_parser._options
    option = option_parser._options[normalized_name]
    assert option.name == "test_option"
    assert option.default == 42
    assert option.type == int
    assert option.help == "A test option"
    assert option.metavar == "TEST"
    assert option.multiple is False
    assert option.group_name == "test_group"

def test_define_existing_option_raises_error(option_parser):
    option_parser.define("test_option", default=42, type=int)
    with pytest.raises(Exception) as excinfo:
        option_parser.define("test_option", default=43, type=int)
    assert "Option 'test-option' already defined" in str(excinfo.value)

def test_define_option_with_callback(option_parser):
    callback_called = False

    def callback(value):
        nonlocal callback_called
        callback_called = True

    option_parser.define("callback_option", type=str, callback=callback)
    normalized_name = option_parser._normalize_name("callback_option")
    option_parser._options[normalized_name].set("new_value")
    assert callback_called

def test_define_option_with_default_type(option_parser):
    option_parser.define("default_type_option", default=3.14)
    normalized_name = option_parser._normalize_name("default_type_option")
    assert normalized_name in option_parser._options
    option = option_parser._options[normalized_name]
    assert option.type == float

def test_define_option_with_multiple(option_parser):
    option_parser.define("multiple_option", multiple=True, type=int)
    normalized_name = option_parser._normalize_name("multiple_option")
    assert normalized_name in option_parser._options
    option = option_parser._options[normalized_name]
    assert option.multiple is True
    assert option.default == []

@pytest.fixture(autouse=True)
def cleanup_options():
    yield
    OptionParser()._options.clear()
