# file: docstring_parser/google.py:61-73
# asked: {"lines": [61, 62, 69, 70, 71, 72, 73], "branches": [[69, 70], [69, 71]]}
# gained: {"lines": [61, 62, 69, 70, 71, 72, 73], "branches": [[69, 70], [69, 71]]}

import pytest
from docstring_parser.google import GoogleParser, DEFAULT_SECTIONS, Section, SectionType

def test_google_parser_init_with_default_sections():
    parser = GoogleParser()
    assert parser.sections == {s.title: s for s in DEFAULT_SECTIONS}
    assert parser.title_colon is True

def test_google_parser_init_with_custom_sections():
    custom_sections = [Section('Custom', 'custom', SectionType.SINGULAR)]
    parser = GoogleParser(sections=custom_sections)
    assert parser.sections == {s.title: s for s in custom_sections}
    assert parser.title_colon is True

def test_google_parser_init_with_title_colon_false():
    parser = GoogleParser(title_colon=False)
    assert parser.sections == {s.title: s for s in DEFAULT_SECTIONS}
    assert parser.title_colon is False
