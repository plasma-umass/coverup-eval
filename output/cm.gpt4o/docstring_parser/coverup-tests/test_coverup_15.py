# file docstring_parser/google.py:89-114
# lines [89, 97, 99, 100, 101, 102, 103, 106, 107, 108, 109, 110, 111, 112, 114]
# branches ['99->103', '99->106', '107->108', '107->114', '109->110', '109->112']

import pytest
from unittest.mock import Mock, patch
from docstring_parser.google import GoogleParser, SectionType, DocstringMeta
import inspect

@pytest.fixture
def google_parser():
    parser = GoogleParser()
    parser.sections = {
        "params": Mock(type=SectionType.SINGULAR_OR_MULTIPLE),
        "returns": Mock(type=SectionType.SINGULAR)
    }
    return parser

def test_build_meta_singular(google_parser):
    google_parser.sections["returns"].type = SectionType.SINGULAR
    text = "return value"
    title = "returns"
    
    with patch.object(GoogleParser, '_build_single_meta', return_value=Mock(spec=DocstringMeta)) as mock_build_single_meta:
        result = google_parser._build_meta(text, title)
        mock_build_single_meta.assert_called_once_with(google_parser.sections[title], text)
        assert isinstance(result, DocstringMeta)

def test_build_meta_singular_or_multiple_single(google_parser):
    google_parser.sections["params"].type = SectionType.SINGULAR_OR_MULTIPLE
    text = "param1"
    title = "params"
    
    with patch.object(GoogleParser, '_build_single_meta', return_value=Mock(spec=DocstringMeta)) as mock_build_single_meta:
        result = google_parser._build_meta(text, title)
        mock_build_single_meta.assert_called_once_with(google_parser.sections[title], text)
        assert isinstance(result, DocstringMeta)

def test_build_meta_singular_or_multiple_multiple(google_parser):
    google_parser.sections["params"].type = SectionType.SINGULAR_OR_MULTIPLE
    text = "param1: description\nmore description"
    title = "params"
    
    with patch.object(GoogleParser, '_build_multi_meta', return_value=Mock(spec=DocstringMeta)) as mock_build_multi_meta:
        result = google_parser._build_meta(text, title)
        mock_build_multi_meta.assert_called_once_with(google_parser.sections[title], "param1", "description\nmore description")
        assert isinstance(result, DocstringMeta)

def test_build_meta_singular_or_multiple_multiple_with_newline(google_parser):
    google_parser.sections["params"].type = SectionType.SINGULAR_OR_MULTIPLE
    text = "param1: description\n    more description"
    title = "params"
    
    with patch.object(GoogleParser, '_build_multi_meta', return_value=Mock(spec=DocstringMeta)) as mock_build_multi_meta:
        result = google_parser._build_meta(text, title)
        mock_build_multi_meta.assert_called_once_with(google_parser.sections[title], "param1", "description\nmore description")
        assert isinstance(result, DocstringMeta)
