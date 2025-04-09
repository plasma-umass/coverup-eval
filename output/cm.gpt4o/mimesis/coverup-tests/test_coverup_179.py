# file mimesis/providers/path.py:73-83
# lines [81, 82, 83]
# branches []

import pytest
from mimesis import Generic
from mimesis.providers.path import Path

@pytest.fixture
def path_provider():
    return Path()

def test_users_folder(mocker, path_provider):
    mock_user = mocker.patch.object(path_provider, 'user', return_value='testuser')
    mock_folder = mocker.patch.object(path_provider.random, 'choice', return_value='Documents')
    
    result = path_provider.users_folder()
    
    assert result == str(path_provider._pathlib_home / 'testuser' / 'Documents')
    mock_user.assert_called_once()
    mock_folder.assert_called_once()
