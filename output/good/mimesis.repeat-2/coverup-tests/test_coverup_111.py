# file mimesis/providers/person.py:495-502
# lines [495, 501, 502]
# branches []

import pytest
from mimesis.providers import Person

# This test will execute the avatar method and check if the URL is correctly formatted
def test_avatar(mocker):
    # Arrange
    size = 256
    expected_hashed_password = "hashed_password"
    person = Person()

    # Mock the password method of the Person class
    mocker.patch.object(Person, 'password', return_value=expected_hashed_password)

    # Act
    avatar_url = person.avatar(size)

    # Assert
    expected_url = f'https://api.adorable.io/avatars/{size}/{expected_hashed_password}.png'
    assert avatar_url == expected_url
    # Verify that the password method was called with the correct parameters
    Person.password.assert_called_once_with(hashed=True)
