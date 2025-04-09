# file mimesis/providers/person.py:223-241
# lines [223, 233, 234, 236, 237, 238, 239, 241]
# branches ['236->237', '236->241']

import pytest
from mimesis.providers.person import Person
import hashlib
from string import ascii_letters, digits, punctuation

@pytest.fixture
def person():
    return Person()

def test_password_length(person):
    password = person.password(length=12)
    assert len(password) == 12

def test_password_characters(person):
    password = person.password(length=12)
    assert all(c in (ascii_letters + digits + punctuation) for c in password)

def test_password_hashed(person):
    password = person.password(length=12, hashed=True)
    assert len(password) == 32  # MD5 hash length
    assert all(c in '0123456789abcdef' for c in password)

def test_password_default_length(person):
    password = person.password()
    assert len(password) == 8

def test_password_not_hashed(person):
    password = person.password(length=12, hashed=False)
    assert len(password) == 12
    assert all(c in (ascii_letters + digits + punctuation) for c in password)
