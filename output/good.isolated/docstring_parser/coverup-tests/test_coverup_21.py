# file docstring_parser/google.py:269-274
# lines [269, 274]
# branches []

import pytest
from docstring_parser import parse
from docstring_parser.parser import Style

def test_parse_function():
    docstring_text = """
    Function description.

    Args:
        param1 (int): The first parameter.
        param2 (str): The second parameter.

    Returns:
        bool: The return value. True for success, False otherwise.
    """

    expected_docstring = parse(docstring_text, style=Style.google)

    # Test the parse function directly
    parsed_docstring = parse(docstring_text, style=Style.google)

    # Assertions to check if the parse function works as expected
    assert isinstance(parsed_docstring, type(expected_docstring))
    assert parsed_docstring.short_description == expected_docstring.short_description
    assert parsed_docstring.long_description == expected_docstring.long_description
    assert len(parsed_docstring.params) == len(expected_docstring.params)
    for parsed_param, expected_param in zip(parsed_docstring.params, expected_docstring.params):
        assert parsed_param.arg_name == expected_param.arg_name
        assert parsed_param.type_name == expected_param.type_name
        assert parsed_param.description == expected_param.description
    assert parsed_docstring.returns.description == expected_docstring.returns.description
    assert parsed_docstring.returns.type_name == expected_docstring.returns.type_name
    assert parsed_docstring.returns.is_generator == expected_docstring.returns.is_generator
