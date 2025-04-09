# file docstring_parser/google.py:60-60
# lines [60]
# branches []

import pytest
from docstring_parser.google import GoogleParser

def test_google_parser_parse(mocker):
    # Mocking the input to the GoogleParser
    mock_docstring = """
    Summary line.

    Extended description of function.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
    """
    
    # Create an instance of GoogleParser
    parser = GoogleParser()
    
    # Parse the mock docstring
    parsed_docstring = parser.parse(mock_docstring)
    
    # Assertions to verify the parsed docstring
    assert parsed_docstring.short_description == "Summary line."
    assert parsed_docstring.long_description == "Extended description of function."
    assert len(parsed_docstring.params) == 2
    assert parsed_docstring.params[0].arg_name == "param1"
    assert parsed_docstring.params[0].type_name == "int"
    assert parsed_docstring.params[0].description == "The first parameter."
    assert parsed_docstring.params[1].arg_name == "param2"
    assert parsed_docstring.params[1].type_name == "str"
    assert parsed_docstring.params[1].description == "The second parameter."
    assert parsed_docstring.returns.type_name == "bool"
    assert parsed_docstring.returns.description == "The return value. True for success, False otherwise."
