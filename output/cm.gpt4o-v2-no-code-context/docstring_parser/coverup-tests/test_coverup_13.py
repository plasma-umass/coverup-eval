# file: docstring_parser/numpydoc.py:281-323
# asked: {"lines": [281, 286, 287, 288, 291, 294, 295, 296, 297, 299, 300, 303, 304, 305, 306, 307, 308, 310, 311, 313, 314, 315, 319, 320, 321, 323], "branches": [[287, 288], [287, 291], [295, 296], [295, 299], [305, 306], [305, 313], [313, 314], [313, 323]]}
# gained: {"lines": [281, 286, 287, 288, 291, 294, 295, 296, 297, 299, 300, 303, 304, 305, 306, 307, 308, 310, 311, 313, 314, 315, 319, 320, 321, 323], "branches": [[287, 288], [287, 291], [295, 296], [295, 299], [305, 306], [305, 313], [313, 314], [313, 323]]}

import pytest
from docstring_parser.numpydoc import NumpydocParser, Docstring
import inspect

@pytest.fixture
def parser():
    return NumpydocParser()

def test_parse_empty_string(parser):
    result = parser.parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert result.meta == []

def test_parse_no_titles(parser):
    docstring = """
    Short description.

    Long description.
    """
    result = parser.parse(docstring)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert result.meta == []

def test_parse_with_titles(parser):
    docstring = """
    Short description.

    Long description.

    Parameters
    ----------
    param1 : int
        Description of param1.
    param2 : str
        Description of param2.

    Returns
    -------
    bool
        Description of return value.
    """
    result = parser.parse(docstring)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert len(result.meta) > 0

def test_parse_with_blank_lines(parser):
    docstring = """
    Short description.


    Long description.


    Parameters
    ----------
    param1 : int
        Description of param1.
    """
    result = parser.parse(docstring)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert result.blank_after_short_description
    assert result.blank_after_long_description
    assert len(result.meta) > 0

def test_parse_no_long_description(parser):
    docstring = """
    Short description.

    Parameters
    ----------
    param1 : int
        Description of param1.
    """
    result = parser.parse(docstring)
    assert result.short_description == "Short description."
    assert result.long_description is None
    assert len(result.meta) > 0

def test_parse_no_short_description(parser):
    docstring = """
    Parameters
    ----------
    param1 : int
        Description of param1.
    """
    result = parser.parse(docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert len(result.meta) > 0
