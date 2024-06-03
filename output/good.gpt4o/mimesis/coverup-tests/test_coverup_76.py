# file mimesis/providers/person.py:495-502
# lines [495, 501, 502]
# branches []

import pytest
from mimesis.providers.person import Person
from unittest.mock import patch

@pytest.fixture
def person():
    return Person()

def test_avatar(person, mocker):
    size = 256
    mock_password = mocker.patch.object(person, 'password', return_value='hashed_password')
    
    avatar_url = person.avatar(size)
    
    mock_password.assert_called_once_with(hashed=True)
    assert avatar_url == f'https://api.adorable.io/avatars/{size}/hashed_password.png'
