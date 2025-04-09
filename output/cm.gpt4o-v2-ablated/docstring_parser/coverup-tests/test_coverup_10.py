# file: docstring_parser/numpydoc.py:326-331
# asked: {"lines": [326, 331], "branches": []}
# gained: {"lines": [326, 331], "branches": []}

import pytest
from docstring_parser.numpydoc import NumpydocParser, parse
from docstring_parser.common import Docstring

def test_parse_empty_string():
    result = parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert result.params == []
    assert result.returns is None

def test_parse_simple_description():
    text = "A simple description."
    result = parse(text)
    assert isinstance(result, Docstring)
    assert result.short_description == "A simple description."
    assert result.long_description is None
    assert result.params == []
    assert result.returns is None

def test_parse_with_params_and_returns():
    text = """
    A function that does something.

    Parameters
    ----------
    x : int
        The first parameter.
    y : str
        The second parameter.

    Returns
    -------
    bool
        The return value. True for success, False otherwise.
    """
    result = parse(text)
    assert isinstance(result, Docstring)
    assert result.short_description == "A function that does something."
    assert result.long_description is None
    assert len(result.params) == 2
    assert result.params[0].arg_name == "x"
    assert result.params[0].type_name == "int"
    assert result.params[0].description == "The first parameter."
    assert result.params[1].arg_name == "y"
    assert result.params[1].type_name == "str"
    assert result.params[1].description == "The second parameter."
    assert result.returns.type_name == "bool"
    assert result.returns.description == "The return value. True for success, False otherwise."

def test_parse_with_long_description():
    text = """
    A function that does something.

    This is a longer description of the function that spans multiple lines.
    It provides more details about the function's behavior and usage.

    Parameters
    ----------
    x : int
        The first parameter.

    Returns
    -------
    bool
        The return value. True for success, False otherwise.
    """
    result = parse(text)
    assert isinstance(result, Docstring)
    assert result.short_description == "A function that does something."
    assert result.long_description == "This is a longer description of the function that spans multiple lines.\nIt provides more details about the function's behavior and usage."
    assert len(result.params) == 1
    assert result.params[0].arg_name == "x"
    assert result.params[0].type_name == "int"
    assert result.params[0].description == "The first parameter."
    assert result.returns.type_name == "bool"
    assert result.returns.description == "The return value. True for success, False otherwise."
