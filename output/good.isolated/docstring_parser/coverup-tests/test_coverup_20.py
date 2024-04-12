# file docstring_parser/numpydoc.py:326-331
# lines [326, 331]
# branches []

import pytest
from docstring_parser import parse, Docstring
from docstring_parser.numpydoc import NumpydocParser

def test_parse_function():
    docstring_text = """
    Summary line.

    Extended description of function.

    Parameters
    ----------
    arg1 : int
        Description of arg1
    arg2 : str
        Description of arg2

    Returns
    -------
    bool
        Description of return value
    """

    expected_docstring = NumpydocParser().parse(docstring_text)
    parsed_docstring = parse(docstring_text)

    assert isinstance(parsed_docstring, Docstring), "The result should be a Docstring instance."
    assert parsed_docstring.short_description == expected_docstring.short_description, "Short descriptions should match."
    assert parsed_docstring.long_description == expected_docstring.long_description, "Long descriptions should match."
    assert len(parsed_docstring.params) == len(expected_docstring.params), "Number of parameters should match."
    for parsed_param, expected_param in zip(parsed_docstring.params, expected_docstring.params):
        assert parsed_param.arg_name == expected_param.arg_name, "Parameter names should match."
        assert parsed_param.type_name == expected_param.type_name, "Parameter types should match."
        assert parsed_param.description == expected_param.description, "Parameter descriptions should match."
    
    # Compare the returns by their attributes instead of direct object comparison
    assert parsed_docstring.returns.type_name == expected_docstring.returns.type_name, "Return types should match."
    assert parsed_docstring.returns.description == expected_docstring.returns.description, "Return descriptions should match."
    assert parsed_docstring.returns.is_generator == expected_docstring.returns.is_generator, "Return is_generator should match."
