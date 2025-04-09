# file: docstring_parser/google.py:61-73
# asked: {"lines": [61, 62, 69, 70, 71, 72, 73], "branches": [[69, 70], [69, 71]]}
# gained: {"lines": [61, 62, 69, 70, 71, 72, 73], "branches": [[69, 70], [69, 71]]}

import pytest
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS

def test_google_parser_init_with_sections():
    sections = [Section('Test', 'test', 'test')]
    parser = GoogleParser(sections=sections, title_colon=False)
    assert parser.sections == {'Test': sections[0]}
    assert parser.title_colon is False
    assert parser.titles_re is not None

def test_google_parser_init_without_sections():
    parser = GoogleParser(sections=None, title_colon=True)
    assert parser.sections == {s.title: s for s in DEFAULT_SECTIONS}
    assert parser.title_colon is True
    assert parser.titles_re is not None
