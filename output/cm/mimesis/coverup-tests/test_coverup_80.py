# file mimesis/providers/person.py:495-502
# lines [495, 501, 502]
# branches []

import pytest
from mimesis.providers import Person

# Mocking the Person's password method
@pytest.fixture
def person_with_mocked_password(mocker):
    person = Person()
    mocker.patch.object(Person, 'password', return_value='hashed_password')
    return person

def test_avatar_with_mocked_password(person_with_mocked_password):
    size = 256
    expected_url = 'https://api.adorable.io/avatars/256/hashed_password.png'
    avatar_url = person_with_mocked_password.avatar(size)
    assert avatar_url == expected_url
