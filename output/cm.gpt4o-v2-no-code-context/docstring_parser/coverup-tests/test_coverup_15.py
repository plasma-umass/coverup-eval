# file: docstring_parser/numpydoc.py:326-331
# asked: {"lines": [326, 331], "branches": []}
# gained: {"lines": [326, 331], "branches": []}

import pytest
from docstring_parser.numpydoc import parse, NumpydocParser
from docstring_parser.common import Docstring

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

    Parameters
    ----------
    param1 : int
        Description of param1.

    Returns
    -------
    bool
        Description of return value.
    """
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert len(result.params) == 1
    assert result.params[0].arg_name == "param1"
    assert result.params[0].type_name == "int"
    assert result.params[0].description == "Description of param1."
    assert result.returns.type_name == "bool"
    assert result.returns.description == "Description of return value."

def test_parse_complex_docstring():
    docstring = """
    Short description.

    Long description.

    Parameters
    ----------
    param1 : int
        Description of param1.
    param2 : str
        Description of param2.

    Raises
    ------
    ValueError
        Description of ValueError.

    Returns
    -------
    bool
        Description of return value.
    """
    result = parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert len(result.params) == 2
    assert result.params[0].arg_name == "param1"
    assert result.params[0].type_name == "int"
    assert result.params[0].description == "Description of param1."
    assert result.params[1].arg_name == "param2"
    assert result.params[1].type_name == "str"
    assert result.params[1].description == "Description of param2."
    assert len(result.raises) == 1
    assert result.raises[0].type_name == "ValueError"
    assert result.raises[0].description == "Description of ValueError."
    assert result.returns.type_name == "bool"
    assert result.returns.description == "Description of return value."
