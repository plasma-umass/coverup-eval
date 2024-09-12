# file: docstring_parser/google.py:269-274
# asked: {"lines": [269, 274], "branches": []}
# gained: {"lines": [269, 274], "branches": []}

import pytest
from docstring_parser.google import parse, GoogleParser, Docstring

def test_parse_empty_docstring():
    result = parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert result.params == []
    assert result.raises == []
    assert result.returns is None

def test_parse_simple_docstring():
    docstring = """
    Short description.
    
    Long description.
    """
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert result.params == []
    assert result.raises == []
    assert result.returns is None

def test_parse_with_params():
    docstring = """
    Short description.
    
    Args:
        param1 (int): Description of param1.
        param2 (str): Description of param2.
    """
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert len(result.params) == 2
    assert result.params[0].arg_name == "param1"
    assert result.params[0].type_name == "int"
    assert result.params[0].description == "Description of param1."
    assert result.params[1].arg_name == "param2"
    assert result.params[1].type_name == "str"
    assert result.params[1].description == "Description of param2."
    assert result.raises == []
    assert result.returns is None

def test_parse_with_returns():
    docstring = """
    Short description.
    
    Returns:
        bool: Description of return value.
    """
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert result.params == []
    assert result.raises == []
    assert result.returns.type_name == "bool"
    assert result.returns.description == "Description of return value."

def test_parse_with_raises():
    docstring = """
    Short description.
    
    Raises:
        ValueError: Description of exception.
    """
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert result.params == []
    assert len(result.raises) == 1
    assert result.raises[0].type_name == "ValueError"
    assert result.raises[0].description == "Description of exception."
    assert result.returns is None
