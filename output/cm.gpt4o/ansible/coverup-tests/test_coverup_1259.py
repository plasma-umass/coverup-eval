# file lib/ansible/galaxy/token.py:161-187
# lines [178]
# branches ['177->178']

import pytest
from ansible.galaxy.token import BasicAuthToken

def test_basic_auth_token_get_with_existing_token(mocker):
    # Arrange
    username = 'test_user'
    password = 'test_pass'
    token = BasicAuthToken(username, password)
    
    # Mock the _encode_token method to ensure it is not called
    mocker.patch.object(token, '_encode_token', return_value='mocked_token')
    
    # Set the _token attribute directly to simulate an existing token
    token._token = 'existing_token'
    
    # Act
    result = token.get()
    
    # Assert
    assert result == 'existing_token'
    token._encode_token.assert_not_called()
