# file: docstring_parser/numpydoc.py:281-323
# asked: {"lines": [286, 287, 288, 291, 294, 295, 296, 297, 299, 300, 303, 304, 305, 306, 307, 308, 310, 311, 313, 314, 315, 319, 320, 321, 323], "branches": [[287, 288], [287, 291], [295, 296], [295, 299], [305, 306], [305, 313], [313, 314], [313, 323]]}
# gained: {"lines": [286, 287, 288, 291, 294, 295, 296, 297, 299, 300, 303, 304, 305, 306, 307, 308, 310, 311, 313, 314, 315, 319, 320, 321, 323], "branches": [[287, 288], [287, 291], [295, 296], [295, 299], [305, 306], [313, 314], [313, 323]]}

import pytest
from docstring_parser.numpydoc import NumpydocParser
from docstring_parser.common import Docstring

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

def test_parse_with_titles(parser, monkeypatch):
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
    mock_titles_re = parser.titles_re
    mock_sections = {
        "Parameters": MockSection(),
        "Returns": MockSection()
    }
    monkeypatch.setattr(parser, "titles_re", mock_titles_re)
    monkeypatch.setattr(parser, "sections", mock_sections)

    result = parser.parse(docstring)
    assert result.short_description == "Short description."
    assert result.long_description == "Long description."
    assert len(result.meta) == 2  # 2 sections parsed

class MockSection:
    def parse(self, text):
        return [text.strip()]
