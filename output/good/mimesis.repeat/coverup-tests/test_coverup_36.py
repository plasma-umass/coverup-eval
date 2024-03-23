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
    password = person_provider.password(hashed=True)
    assert isinstance(password, str)
    assert len(password) == 32  # MD5 hash length
    try:
        int(password, 16)  # Check if it's a valid hex value
    except ValueError:
        pytest.fail("Generated hash is not a valid hex value")

def test_password_not_hashed(person_provider):
    password = person_provider.password(hashed=False)
    assert isinstance(password, str)
    assert 1 <= len(password) <= 100  # Assuming a reasonable max length for a password
    assert all(c in (ascii_letters + digits + punctuation) for c in password)

def test_password_length(person_provider):
    length = 10
    password = person_provider.password(length=length, hashed=False)
    assert len(password) == length
