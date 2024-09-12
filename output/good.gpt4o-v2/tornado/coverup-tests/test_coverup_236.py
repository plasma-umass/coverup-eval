# file: tornado/options.py:217-302
# asked: {"lines": [264, 265, 266], "branches": [[263, 264]]}
# gained: {"lines": [264, 265, 266], "branches": [[263, 264]]}

import pytest
from tornado.options import OptionParser, Error

@pytest.fixture
def option_parser():
    parser = OptionParser()
    parser.__dict__['_options'] = {}
    return parser

def test_define_option_already_defined(option_parser):
    option_parser.define("test_option", default="default_value")
    with pytest.raises(Error, match="Option 'test-option' already defined in"):
        option_parser.define("test_option", default="another_value")

def test_define_option_cleanup(option_parser):
    option_parser.define("test_option", default="default_value")
    assert "test-option" in option_parser._options
    assert option_parser._options["test-option"].default == "default_value"

    # Clean up
    option_parser._options.pop("test-option")
    assert "test-option" not in option_parser._options
