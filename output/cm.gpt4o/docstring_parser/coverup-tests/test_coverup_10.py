# file docstring_parser/numpydoc.py:256-256
# lines [256]
# branches []

import pytest
from docstring_parser.numpydoc import NumpydocParser

def test_numpydoc_parser_parse(mocker):
    # Mock the input to the NumpydocParser
    docstring = """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    param1 : int
        The first parameter.
    param2 : str
        The second parameter.

    Returns
    -------
    bool
        Description of return value.
    """
    
    parser = NumpydocParser()
    parsed_docstring = parser.parse(docstring)
    
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
    assert parsed_docstring.returns.description == "Description of return value."
