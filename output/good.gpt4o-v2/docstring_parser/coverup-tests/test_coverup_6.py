# file: docstring_parser/google.py:61-73
# asked: {"lines": [61, 62, 69, 70, 71, 72, 73], "branches": [[69, 70], [69, 71]]}
# gained: {"lines": [61, 62, 69, 70, 71, 72, 73], "branches": [[69, 70], [69, 71]]}

import pytest
from docstring_parser.google import GoogleParser, DEFAULT_SECTIONS
from unittest.mock import patch

def test_google_parser_no_sections():
    parser = GoogleParser()
    assert parser.sections == {s.title: s for s in DEFAULT_SECTIONS}
    assert parser.title_colon is True

def test_google_parser_with_sections():
    custom_sections = [DEFAULT_SECTIONS[0]]
    parser = GoogleParser(sections=custom_sections)
    assert parser.sections == {s.title: s for s in custom_sections}
    assert parser.title_colon is True

def test_google_parser_title_colon_false():
    parser = GoogleParser(title_colon=False)
    assert parser.sections == {s.title: s for s in DEFAULT_SECTIONS}
    assert parser.title_colon is False

def test_google_parser_setup_called():
    with patch.object(GoogleParser, '_setup', return_value=None) as mock_setup:
        parser = GoogleParser()
        mock_setup.assert_called_once()
