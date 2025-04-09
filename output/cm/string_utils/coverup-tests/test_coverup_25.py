# file string_utils/validation.py:555-574
# lines [555, 571, 572, 574]
# branches ['571->572', '571->574']

import pytest
from string_utils.validation import contains_html, is_string

def test_contains_html_with_tags():
    assert contains_html('my string is <strong>bold</strong>') is True

def test_contains_html_without_tags():
    assert contains_html('my string is not bold') is False

def test_contains_html_with_invalid_input(mocker):
    mocker.patch('string_utils.validation.is_string', return_value=False)
    with pytest.raises(Exception) as exc_info:
        contains_html(123)
    assert exc_info.type.__name__ == "InvalidInputError"
