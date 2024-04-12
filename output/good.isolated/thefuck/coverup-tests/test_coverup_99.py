# file thefuck/argument_parser.py:7-12
# lines [7, 8]
# branches []

import pytest
from thefuck.argument_parser import Parser

def test_parser_initialization():
    parser = Parser()
    assert parser is not None, "Parser object should be instantiated"
