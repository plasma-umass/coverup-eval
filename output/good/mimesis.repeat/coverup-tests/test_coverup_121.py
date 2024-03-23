# file mimesis/providers/person.py:495-502
# lines [495, 501, 502]
# branches []

import pytest
from mimesis.providers import Person

# Mocking Person's password method to control its output
def test_avatar_with_mocked_password(mocker):
    # Arrange
    size = 256
    expected_hashed_password = "hashed_password"
    person_provider = Person()

    # Mock the password method of the Person to return a specific hashed password
    mocker.patch.object(Person, 'password', return_value=expected_hashed_password)

    # Act
    avatar_url = person_provider.avatar(size=size)

    # Assert
    expected_url = f'https://api.adorable.io/avatars/{size}/{expected_hashed_password}.png'
    assert avatar_url == expected_url
    # Verify that the password method was called with the correct parameters
    Person.password.assert_called_once_with(hashed=True)
