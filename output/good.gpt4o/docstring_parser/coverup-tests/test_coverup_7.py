# file docstring_parser/google.py:269-274
# lines [269, 274]
# branches []

import pytest
from docstring_parser.google import parse, Docstring

def test_parse_google_docstring():
    docstring_text = """
    Summary of the function.

    Args:
        param1 (int): Description of param1.
        param2 (str): Description of param2.

    Returns:
        bool: Description of return value.
    """
    result = parse(docstring_text)
    
    assert isinstance(result, Docstring)
    assert result.short_description == "Summary of the function."
    assert len(result.params) == 2
    assert result.params[0].arg_name == "param1"
    assert result.params[0].type_name == "int"
    assert result.params[0].description == "Description of param1."
    assert result.params[1].arg_name == "param2"
    assert result.params[1].type_name == "str"
    assert result.params[1].description == "Description of param2."
    assert result.returns.type_name == "bool"
    assert result.returns.description == "Description of return value."
