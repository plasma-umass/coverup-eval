# file: string_utils/validation.py:555-574
# asked: {"lines": [555, 571, 572, 574], "branches": [[571, 572], [571, 574]]}
# gained: {"lines": [555, 571, 572, 574], "branches": [[571, 572], [571, 574]]}

import pytest
from string_utils.validation import contains_html
from string_utils.errors import InvalidInputError

def test_contains_html_with_html_tags():
    assert contains_html('my string is <strong>bold</strong>') == True

def test_contains_html_without_html_tags():
    assert contains_html('my string is not bold') == False

def test_contains_html_invalid_input():
    with pytest.raises(InvalidInputError):
        contains_html(12345)

def test_contains_html_empty_string():
    assert contains_html('') == False
