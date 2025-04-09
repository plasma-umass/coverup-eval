# file: tornado/options.py:134-143
# asked: {"lines": [134, 136, 137, 138, 139, 140, 141, 142], "branches": []}
# gained: {"lines": [134, 136, 137, 138, 139, 140, 141, 142], "branches": []}

import pytest
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    return OptionParser()

def test_option_parser_initialization(option_parser):
    assert '_options' in option_parser.__dict__
    assert '_parse_callbacks' in option_parser.__dict__
    assert 'help' in option_parser._options
    assert option_parser._options['help'].type == bool
    assert option_parser._options['help'].help == "show this help information"
    assert option_parser._options['help'].callback == option_parser._help_callback

def test_define_new_option(option_parser):
    option_parser.define("test_option", type=int, help="a test option", default=10)
    normalized_name = option_parser._normalize_name("test_option")
    assert normalized_name in option_parser._options
    assert option_parser._options[normalized_name].type == int
    assert option_parser._options[normalized_name].help == "a test option"
    assert option_parser._options[normalized_name].default == 10

def test_define_existing_option_raises_error(option_parser):
    with pytest.raises(Exception) as excinfo:
        option_parser.define("help", type=bool, help="another help option")
    assert "Option 'help' already defined" in str(excinfo.value)
