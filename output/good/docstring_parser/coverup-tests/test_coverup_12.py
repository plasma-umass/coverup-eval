# file docstring_parser/google.py:75-87
# lines [75, 76, 77, 79, 80, 81, 82, 83, 84, 85, 86]
# branches ['76->77', '76->79']

import re
import pytest
from docstring_parser.google import GoogleParser

@pytest.fixture
def google_parser_with_colon():
    parser = GoogleParser()
    parser.title_colon = True
    parser.sections = ['Arguments', 'Returns', 'Raises']
    parser._setup()
    return parser

@pytest.fixture
def google_parser_without_colon():
    parser = GoogleParser()
    parser.title_colon = False
    parser.sections = ['Arguments', 'Returns', 'Raises']
    parser._setup()
    return parser

def test_google_parser_titles_re_with_colon(google_parser_with_colon):
    assert google_parser_with_colon.titles_re.match('Arguments:')
    assert google_parser_with_colon.titles_re.match('Returns:')
    assert google_parser_with_colon.titles_re.match('Raises:')
    assert not google_parser_with_colon.titles_re.match('Arguments')
    assert not google_parser_with_colon.titles_re.match('Returns')
    assert not google_parser_with_colon.titles_re.match('Raises')

def test_google_parser_titles_re_without_colon(google_parser_without_colon):
    assert google_parser_without_colon.titles_re.match('Arguments')
    assert google_parser_without_colon.titles_re.match('Returns')
    assert google_parser_without_colon.titles_re.match('Raises')
    assert not google_parser_without_colon.titles_re.match('Arguments:')
    assert not google_parser_without_colon.titles_re.match('Returns:')
    assert not google_parser_without_colon.titles_re.match('Raises:')
