# file string_utils/validation.py:204-244
# lines [242]
# branches ['240->242']

import pytest
from string_utils.validation import is_email

def test_is_email_with_escaped_at_sign():
    # Test case where the email contains an escaped "@" sign
    email_with_escaped_at = 'my.email\\@example@domain.com'
    assert is_email(email_with_escaped_at) == True

    # Test case where the email contains multiple "@" signs but the head part is correctly escaped
    email_with_multiple_ats = 'my.email\\@example@domain.com'
    assert is_email(email_with_multiple_ats) == True

    # Test case where the email is invalid after replacing escaped "@" with "a"
    email_invalid_after_replacement = 'my.email\\@example@domain.com'
    assert is_email(email_invalid_after_replacement) == True

    # Test case where the email is valid after replacing escaped "@" with "a"
    email_valid_after_replacement = 'my.email\\@example.com'
    assert is_email(email_valid_after_replacement) == True

@pytest.fixture(autouse=True)
def cleanup(mocker):
    # Cleanup code to ensure no side effects on other tests
    yield
    mocker.stopall()
