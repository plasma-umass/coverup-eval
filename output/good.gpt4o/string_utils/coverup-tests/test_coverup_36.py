# file string_utils/validation.py:204-244
# lines [204, 220, 221, 223, 225, 228, 229, 232, 233, 234, 236, 238, 240, 242, 244]
# branches ['220->221', '220->223', '228->229', '228->232', '233->234', '233->236', '240->242', '240->244']

import pytest
from string_utils.validation import is_email

def test_is_email_valid():
    assert is_email('my.email@the-provider.com') == True

def test_is_email_invalid_empty_string():
    assert is_email('') == False

def test_is_email_invalid_too_long():
    long_email = 'a' * 65 + '@' + 'b' * 256 + '.com'
    assert is_email(long_email) == False

def test_is_email_invalid_starts_with_dot():
    assert is_email('.email@provider.com') == False

def test_is_email_invalid_multiple_at_signs():
    assert is_email('my.email@@provider.com') == False

def test_is_email_valid_escaped_at_sign():
    assert is_email('my.email\\@provider.com') == True

def test_is_email_invalid_head_ends_with_dot():
    assert is_email('my.email.@provider.com') == False

def test_is_email_invalid_multiple_consecutive_dots():
    assert is_email('my..email@provider.com') == False

def test_is_email_valid_escaped_spaces():
    assert is_email('my\\ email@provider.com') == True

def test_is_email_valid_quoted_head():
    assert is_email('"my email"@provider.com') == True

def test_is_email_invalid_quoted_head_with_spaces():
    assert is_email('"my email @provider.com') == False

@pytest.fixture(autouse=True)
def cleanup(mocker):
    mocker.stopall()
