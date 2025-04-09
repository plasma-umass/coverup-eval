# file mimesis/providers/person.py:223-241
# lines [241]
# branches ['236->241']

import pytest
from mimesis.providers.person import Person
from unittest.mock import patch

@pytest.fixture
def person():
    return Person()

def test_password_not_hashed(person):
    with patch.object(person.random, 'choice', return_value='a'):
        result = person.password(length=4, hashed=False)
        assert result == 'aaaa'

def test_password_hashed(person):
    with patch.object(person.random, 'choice', return_value='a'):
        result = person.password(length=4, hashed=True)
        assert result.isalnum() and len(result) == 32
