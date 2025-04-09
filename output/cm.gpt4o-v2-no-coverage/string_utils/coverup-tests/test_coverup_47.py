# file: string_utils/validation.py:204-244
# asked: {"lines": [204, 220, 221, 223, 225, 228, 229, 232, 233, 234, 236, 238, 240, 242, 244], "branches": [[220, 221], [220, 223], [228, 229], [228, 232], [233, 234], [233, 236], [240, 242], [240, 244]]}
# gained: {"lines": [204, 220, 221, 223, 225, 228, 229, 232, 233, 234, 236, 238, 240, 242, 244], "branches": [[220, 221], [220, 223], [228, 229], [228, 232], [233, 234], [233, 236], [240, 242], [240, 244]]}

import pytest
from string_utils.validation import is_email
from string_utils._regex import EMAIL_RE, ESCAPED_AT_SIGN

def test_is_email_valid():
    assert is_email('my.email@the-provider.com') == True

def test_is_email_invalid_no_at():
    assert is_email('my.email.the-provider.com') == False

def test_is_email_invalid_starts_with_dot():
    assert is_email('.my.email@the-provider.com') == False

def test_is_email_invalid_multiple_ats():
    assert is_email('my.email@@the-provider.com') == False

def test_is_email_invalid_head_too_long():
    long_head = 'a' * 65
    assert is_email(f'{long_head}@the-provider.com') == False

def test_is_email_invalid_tail_too_long():
    long_tail = 'a' * 256
    assert is_email(f'my.email@{long_tail}.com') == False

def test_is_email_invalid_head_ends_with_dot():
    assert is_email('my.email.@the-provider.com') == False

def test_is_email_invalid_multiple_consecutive_dots():
    assert is_email('my..email@the-provider.com') == False

def test_is_email_escaped_at_sign():
    assert is_email('my.email\\@the-provider.com') == True

def test_is_email_escaped_spaces():
    assert is_email('"my email"@the-provider.com') == True

def test_is_email_invalid_escaped_at_sign():
    assert is_email('my.email\\@\\@the-provider.com') == False

def test_is_email_invalid_empty_string():
    assert is_email('') == False

def test_is_email_invalid_none():
    assert is_email(None) == False

def test_is_email_invalid_only_spaces():
    assert is_email('   ') == False
