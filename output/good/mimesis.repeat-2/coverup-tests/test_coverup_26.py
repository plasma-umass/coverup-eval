# file mimesis/providers/person.py:223-241
# lines [223, 233, 234, 236, 237, 238, 239, 241]
# branches ['236->237', '236->241']

import pytest
import hashlib
from mimesis.providers.person import Person
from string import ascii_letters, digits, punctuation

@pytest.fixture
def person_provider():
    return Person()

def test_password_hashed(person_provider):
    password = person_provider.password(length=10, hashed=True)
    assert isinstance(password, str)
    assert len(password) == 32  # MD5 hash length
    # Verify that the password is a valid MD5 hash
    try:
        int(password, 16)
    except ValueError:
        pytest.fail("Generated password is not a valid MD5 hash")

def test_password_not_hashed(person_provider):
    password = person_provider.password(length=10, hashed=False)
    assert isinstance(password, str)
    assert len(password) == 10  # Password length as requested
    # Verify that the password contains only valid characters
    valid_characters = set(ascii_letters + digits + punctuation)
    assert all(char in valid_characters for char in password)
