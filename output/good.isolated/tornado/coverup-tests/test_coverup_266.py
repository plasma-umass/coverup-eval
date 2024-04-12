# file tornado/options.py:163-165
# lines [164, 165]
# branches []

import pytest
from tornado.options import OptionParser

@pytest.fixture
def option_parser():
    parser = OptionParser()
    yield parser
    parser._options.clear()

def test_option_parser_contains(option_parser):
    # Add an option to the parser to test the __contains__ method
    option_parser.define("mock_name", default="mock_value", type=str, help="mock option")
    
    # Check that the __contains__ method returns True for an existing option
    assert "mock_name" in option_parser
    
    # Check that the __contains__ method returns False for a non-existent option
    assert "non_existent_option" not in option_parser
