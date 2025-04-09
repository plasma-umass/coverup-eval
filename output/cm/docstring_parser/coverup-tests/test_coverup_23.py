# file docstring_parser/numpydoc.py:281-323
# lines [281, 286, 287, 288, 291, 294, 295, 296, 297, 299, 300, 303, 304, 305, 306, 307, 308, 310, 311, 313, 314, 315, 319, 320, 321, 323]
# branches ['287->288', '287->291', '295->296', '295->299', '305->306', '305->313', '313->314', '313->323']

import pytest
from docstring_parser.parser import Docstring
from docstring_parser.numpydoc import NumpydocParser
from unittest.mock import MagicMock

@pytest.fixture
def numpydoc_parser():
    return NumpydocParser()

def test_numpydoc_parser_empty_string(numpydoc_parser):
    result = numpydoc_parser.parse("")
    assert isinstance(result, Docstring)
    assert result.short_description is None
    assert result.long_description is None
    assert not result.meta

def test_numpydoc_parser_no_meta(numpydoc_parser):
    text = "Short description\n\nLong description with more details."
    result = numpydoc_parser.parse(text)
    assert result.short_description == "Short description"
    assert result.long_description == "Long description with more details."
    assert not result.meta

def test_numpydoc_parser_with_meta(numpydoc_parser, mocker):
    text = (
        "Short description\n\n"
        "Long description with more details.\n\n"
        "Parameters\n"
        "----------\n"
        "param1 : int\n"
        "    The first parameter.\n"
    )
    mock_factory = MagicMock()
    mock_factory.parse.return_value = ["parsed meta"]
    mocker.patch.object(numpydoc_parser, 'sections', {'Parameters': mock_factory})
    result = numpydoc_parser.parse(text)
    assert result.short_description == "Short description"
    assert result.long_description == "Long description with more details."
    assert result.meta == ["parsed meta"]
    mock_factory.parse.assert_called_once()

def test_numpydoc_parser_with_multiple_meta(numpydoc_parser, mocker):
    text = (
        "Short description\n\n"
        "Long description with more details.\n\n"
        "Parameters\n"
        "----------\n"
        "param1 : int\n"
        "    The first parameter.\n\n"
        "Returns\n"
        "-------\n"
        "output : str\n"
        "    The result.\n"
    )
    mock_factory = MagicMock()
    mock_factory.parse.side_effect = [["parsed params"], ["parsed returns"]]
    mocker.patch.object(numpydoc_parser, 'sections', {'Parameters': mock_factory, 'Returns': mock_factory})
    result = numpydoc_parser.parse(text)
    assert result.short_description == "Short description"
    assert result.long_description == "Long description with more details."
    assert result.meta == ["parsed params", "parsed returns"]
    assert mock_factory.parse.call_count == 2
