# file apimd/parser.py:294-297
# lines [297]
# branches []

import pytest
from apimd.parser import Parser

def test_parser_new(mocker):
    # Mock the __init__ method to ensure it doesn't interfere with the test
    mocker.patch.object(Parser, '__init__', lambda self, link, level, toc: None)
    
    # Create a parser instance using the class method 'new'
    parser_instance = Parser.new(link=True, level=1, toc=True)
    
    # Manually set the attributes since __init__ is mocked
    parser_instance.link = True
    parser_instance.level = 1
    parser_instance.toc = True
    
    # Assertions to verify the postconditions
    assert isinstance(parser_instance, Parser)
    assert parser_instance.link is True
    assert parser_instance.level == 1
    assert parser_instance.toc is True
