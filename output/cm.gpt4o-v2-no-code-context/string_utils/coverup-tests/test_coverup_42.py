# file: string_utils/validation.py:204-244
# asked: {"lines": [204, 220, 221, 223, 225, 228, 229, 232, 233, 234, 236, 238, 240, 242, 244], "branches": [[220, 221], [220, 223], [228, 229], [228, 232], [233, 234], [233, 236], [240, 242], [240, 244]]}
# gained: {"lines": [204, 220, 221, 223, 225, 228, 229, 232, 233, 234, 236, 238, 240, 244], "branches": [[220, 221], [220, 223], [228, 229], [228, 232], [233, 234], [233, 236], [240, 244]]}

import pytest
from string_utils.validation import is_email

def test_is_email_valid():
    assert is_email('my.email@the-provider.com') is True

def test_is_email_empty_string():
    assert is_email('') is False

def test_is_email_too_long():
    long_email = 'a' * 321 + '@example.com'
    assert is_email(long_email) is False

def test_is_email_starts_with_dot():
    assert is_email('.email@example.com') is False

def test_is_email_no_at_symbol():
    assert is_email('email.example.com') is False

def test_is_email_multiple_at_symbols():
    assert is_email('email@@example.com') is False

def test_is_email_head_too_long():
    long_head = 'a' * 65 + '@example.com'
    assert is_email(long_head) is False

def test_is_email_tail_too_long():
    long_tail = 'a' * 256 + '@example.com'
    assert is_email(long_tail) is False

def test_is_email_head_ends_with_dot():
    assert is_email('email.@example.com') is False

def test_is_email_head_contains_multiple_dots():
    assert is_email('email..email@example.com') is False

def test_is_email_escaped_spaces():
    assert is_email('email\\ @example.com') is True

def test_is_email_quoted_head():
    assert is_email('"email"@example.com') is True

def test_is_email_escaped_at_sign():
    assert is_email('email\\@example.com') is True

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    # Clean up or reset any state if necessary
    yield
    # Perform any necessary cleanup after each test
