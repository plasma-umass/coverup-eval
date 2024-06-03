# file docstring_parser/google.py:61-73
# lines [61, 62, 69, 70, 71, 72, 73]
# branches ['69->70', '69->71']

import pytest
from unittest import mock
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS

def test_google_parser_init_with_defaults():
    parser = GoogleParser()
    assert parser.sections == {s.title: s for s in DEFAULT_SECTIONS}
    assert parser.title_colon is True

def test_google_parser_init_with_custom_sections():
    custom_sections = [Section(title="Custom", key="custom", type="custom")]
    parser = GoogleParser(sections=custom_sections)
    assert parser.sections == {s.title: s for s in custom_sections}
    assert parser.title_colon is True

def test_google_parser_init_with_title_colon_false():
    parser = GoogleParser(title_colon=False)
    assert parser.sections == {s.title: s for s in DEFAULT_SECTIONS}
    assert parser.title_colon is False

def test_google_parser_setup_called(mocker):
    mock_setup = mocker.patch.object(GoogleParser, '_setup', autospec=True)
    parser = GoogleParser()
    mock_setup.assert_called_once_with(parser)
