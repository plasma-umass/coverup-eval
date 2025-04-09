# file thefuck/argument_parser.py:7-12
# lines [7, 8]
# branches []

import pytest
from thefuck.argument_parser import Parser

def test_parser_initialization():
    # Test the initialization of the Parser class
    parser = Parser()
    assert isinstance(parser, Parser)

# Clean up after the test
@pytest.fixture(autouse=True)
def cleanup(mocker):
    yield
    mocker.stopall()
