# file: docstring_parser/numpydoc.py:326-331
# asked: {"lines": [326, 331], "branches": []}
# gained: {"lines": [326], "branches": []}

import pytest
from docstring_parser.numpydoc import NumpydocParser
from docstring_parser.common import Docstring

def test_parse_with_valid_docstring():
    docstring = """
    Short description.

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
    result = NumpydocParser().parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert len(result.meta) == 3  # 2 params + 1 return

def test_parse_with_empty_docstring():
    docstring = ""
    result = NumpydocParser().parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert len(result.meta) == 0

def test_parse_with_no_params_or_returns():
    docstring = """
    Short description.

    Long description.
    """
    result = NumpydocParser().parse(docstring)
    assert isinstance(result, Docstring)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert len(result.meta) == 0
