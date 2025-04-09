# file docstring_parser/numpydoc.py:326-331
# lines [326, 331]
# branches []

import pytest
from docstring_parser.numpydoc import NumpydocParser, parse
from docstring_parser.common import Docstring

def test_parse_numpy_docstring():
    docstring = """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    param1 : int
        Description of parameter `param1`.
    param2 : str
        Description of parameter `param2`.

    Returns
    -------
    bool
        Description of return value.
    """
    result = parse(docstring)
    
    assert isinstance(result, Docstring)
    assert result.short_description == "Summary line."
    assert result.long_description == "Extended description of function."
    assert len(result.params) == 2
    assert result.params[0].arg_name == "param1"
    assert result.params[0].type_name == "int"
    assert result.params[0].description == "Description of parameter `param1`."
    assert result.params[1].arg_name == "param2"
    assert result.params[1].type_name == "str"
    assert result.params[1].description == "Description of parameter `param2`."
    assert result.returns.type_name == "bool"
    assert result.returns.description == "Description of return value."
