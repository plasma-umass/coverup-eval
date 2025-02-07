# file: string_utils/validation.py:204-244
# asked: {"lines": [204, 220, 221, 223, 225, 228, 229, 232, 233, 234, 236, 238, 240, 242, 244], "branches": [[220, 221], [220, 223], [228, 229], [228, 232], [233, 234], [233, 236], [240, 242], [240, 244]]}
# gained: {"lines": [204, 220, 221, 223, 225, 228, 229, 232, 233, 234, 236, 238, 240, 242, 244], "branches": [[220, 221], [220, 223], [228, 229], [228, 232], [233, 234], [233, 236], [240, 242], [240, 244]]}

import pytest
from string_utils.validation import is_email
from string_utils._regex import EMAIL_RE, ESCAPED_AT_SIGN

def test_is_email_valid():
    assert is_email('my.email@the-provider.com') == True

def test_is_email_invalid_empty_string():
    assert is_email('') == False

def test_is_email_invalid_too_long():
    long_email = 'a' * 321 + '@example.com'
    assert is_email(long_email) == False

def test_is_email_invalid_starts_with_dot():
    assert is_email('.email@example.com') == False

def test_is_email_invalid_no_at_symbol():
    assert is_email('email.example.com') == False

def test_is_email_invalid_head_too_long():
    long_head = 'a' * 65 + '@example.com'
    assert is_email(long_head) == False

def test_is_email_invalid_tail_too_long():
    long_tail = 'a@' + 'b' * 256 + '.com'
    assert is_email(long_tail) == False

def test_is_email_invalid_head_ends_with_dot():
    assert is_email('email.@example.com') == False

def test_is_email_invalid_multiple_consecutive_dots():
    assert is_email('email..email@example.com') == False

def test_is_email_escaped_spaces():
    assert is_email('\"my email\"@example.com') == True

def test_is_email_multiple_at_signs():
    assert is_email('\"my@ema@il\"@example.com') == True

def test_is_email_invalid_multiple_at_signs():
    assert is_email('my@ema@il@example.com') == False
