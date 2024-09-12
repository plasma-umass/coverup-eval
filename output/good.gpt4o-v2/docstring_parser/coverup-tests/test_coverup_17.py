# file: docstring_parser/google.py:75-87
# asked: {"lines": [75, 76, 77, 79, 80, 81, 82, 83, 84, 85, 86], "branches": [[76, 77], [76, 79]]}
# gained: {"lines": [75, 76, 77, 79, 80, 81, 82, 83, 84, 85, 86], "branches": [[76, 77], [76, 79]]}

import pytest
import re
from docstring_parser.google import GoogleParser, Section, DEFAULT_SECTIONS

def test_setup_with_title_colon():
    parser = GoogleParser(title_colon=True)
    parser._setup()
    expected_pattern = "^(" + "|".join("(%s)" % t for t in parser.sections) + "):[ \t\r\f\v]*$"
    assert parser.titles_re.pattern == expected_pattern
    assert parser.titles_re.flags & re.M

def test_setup_without_title_colon():
    parser = GoogleParser(title_colon=False)
    parser._setup()
    expected_pattern = "^(" + "|".join("(%s)" % t for t in parser.sections) + ")[ \t\r\f\v]*$"
    assert parser.titles_re.pattern == expected_pattern
    assert parser.titles_re.flags & re.M
