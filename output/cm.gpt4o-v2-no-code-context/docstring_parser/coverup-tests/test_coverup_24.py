# file: docstring_parser/google.py:61-73
# asked: {"lines": [], "branches": [[69, 71]]}
# gained: {"lines": [], "branches": [[69, 71]]}

import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS

def test_google_parser_with_default_sections():
    parser = GoogleParser()
    assert parser.sections == {s.title: s for s in DEFAULT_SECTIONS}
    assert parser.title_colon is True

def test_google_parser_with_custom_sections():
    custom_sections = [Section("custom_key", "Custom", "custom_type")]
    parser = GoogleParser(sections=custom_sections)
    assert parser.sections == {s.title: s for s in custom_sections}
    assert parser.title_colon is True

def test_google_parser_without_title_colon():
    parser = GoogleParser(title_colon=False)
    assert parser.sections == {s.title: s for s in DEFAULT_SECTIONS}
    assert parser.title_colon is False
