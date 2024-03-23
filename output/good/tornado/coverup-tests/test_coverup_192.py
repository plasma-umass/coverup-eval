# file tornado/options.py:160-161
# lines [160, 161]
# branches []

import pytest
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    parser = OptionParser()
    parser.define("foo", default="bar")
    parser.define("baz", default="qux")
    yield parser
    parser._options.clear()

def test_option_parser_iteration(option_parser):
    # Define options to the parser
    option_parser.define("test_option", default="test_value")
    option_parser.define("another_option", default="another_value")

    # Collect all option names from the iterator
    option_names = list(iter(option_parser))

    # Assert that the option names are in the list
    assert "test_option" in option_names
    assert "another_option" in option_names
    assert "foo" in option_names
    assert "baz" in option_names

    # The 'help' option is automatically added by tornado, so we expect 5 options
    assert len(option_names) == 5

    # Cleanup is handled by the option_parser fixture
