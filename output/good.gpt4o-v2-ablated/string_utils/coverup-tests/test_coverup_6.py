# file: string_utils/validation.py:555-574
# asked: {"lines": [555, 571, 572, 574], "branches": [[571, 572], [571, 574]]}
# gained: {"lines": [555, 571, 572, 574], "branches": [[571, 572], [571, 574]]}

import pytest
from string_utils.validation import contains_html, InvalidInputError
import re

# Mocking the dependencies
HTML_RE = re.compile(r'<[^>]+>')
def is_string(input_string):
    return isinstance(input_string, str)

@pytest.fixture(autouse=True)
def mock_dependencies(monkeypatch):
    monkeypatch.setattr('string_utils.validation.HTML_RE', HTML_RE)
    monkeypatch.setattr('string_utils.validation.is_string', is_string)

def test_contains_html_with_html_tags():
    assert contains_html('my string is <strong>bold</strong>') is True

def test_contains_html_without_html_tags():
    assert contains_html('my string is not bold') is False

def test_contains_html_invalid_input():
    with pytest.raises(InvalidInputError):
        contains_html(12345)

def test_contains_html_empty_string():
    assert contains_html('') is False

def test_contains_html_with_special_characters():
    assert contains_html('my string is <strong>bold</strong> and <em>italic</em>') is True
    assert contains_html('my string is not <bold>') is True
    assert contains_html('my string is not bold & strong') is False
