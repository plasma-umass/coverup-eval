# file string_utils/validation.py:555-574
# lines [555, 571, 572, 574]
# branches ['571->572', '571->574']

import pytest
from string_utils.validation import contains_html, InvalidInputError
import re

# Mocking the dependencies
@pytest.fixture(autouse=True)
def mock_dependencies(mocker):
    global HTML_RE, is_string
    HTML_RE = re.compile(r'<[^>]+>')
    is_string = mocker.patch('string_utils.validation.is_string', return_value=True)

def test_contains_html_with_html_tags():
    assert contains_html('my string is <strong>bold</strong>') is True

def test_contains_html_without_html_tags():
    assert contains_html('my string is not bold') is False

def test_contains_html_invalid_input(mocker):
    mocker.patch('string_utils.validation.is_string', return_value=False)
    with pytest.raises(InvalidInputError):
        contains_html(12345)
