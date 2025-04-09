# file: string_utils/validation.py:204-244
# asked: {"lines": [242], "branches": [[240, 242]]}
# gained: {"lines": [242], "branches": [[240, 242]]}

import pytest
from string_utils.validation import is_email
from string_utils._regex import ESCAPED_AT_SIGN

def test_is_email_with_escaped_at_sign():
    # Test case where the input string has multiple "@" signs but the head part is correctly escaped
    input_string = 'test\\"@example.com'
    assert is_email(input_string) == is_email(ESCAPED_AT_SIGN.sub('a', input_string))

def test_is_email_with_invalid_escaped_at_sign():
    # Test case where the input string has multiple "@" signs and the head part is not correctly escaped
    input_string = 'test@@example.com'
    assert not is_email(input_string)

def test_is_email_with_valid_email():
    # Test case with a valid email
    input_string = 'my.email@the-provider.com'
    assert is_email(input_string)

def test_is_email_with_invalid_email():
    # Test case with an invalid email
    input_string = '@gmail.com'
    assert not is_email(input_string)

def test_is_email_with_multiple_escaped_at_signs():
    # Test case where the input string has multiple "@" signs and the head part is correctly escaped
    input_string = 'test\\"@test\\"@example.com'
    assert is_email(input_string) == is_email(ESCAPED_AT_SIGN.sub('a', input_string))
