# file thefuck/conf.py:58-65
# lines [60, 62, 63, 64, 65]
# branches ['63->64', '63->65']

import pytest
from unittest import mock
from pathlib import Path
from thefuck.conf import Settings

@pytest.fixture
def mock_user_dir_path(mocker):
    mock_path = mocker.patch('thefuck.conf.Settings._get_user_dir_path')
    mock_user_dir = mock.Mock(spec=Path)
    mock_path.return_value = mock_user_dir
    return mock_user_dir

def test_setup_user_dir_creates_rules_dir_if_not_exists(mock_user_dir_path):
    settings = Settings()
    
    rules_dir = mock_user_dir_path.joinpath('rules')
    rules_dir.is_dir.return_value = False
    
    settings._setup_user_dir()
    
    rules_dir.mkdir.assert_called_once_with(parents=True)
    assert settings.user_dir == mock_user_dir_path

def test_setup_user_dir_does_not_create_rules_dir_if_exists(mock_user_dir_path):
    settings = Settings()
    
    rules_dir = mock_user_dir_path.joinpath('rules')
    rules_dir.is_dir.return_value = True
    
    settings._setup_user_dir()
    
    rules_dir.mkdir.assert_not_called()
    assert settings.user_dir == mock_user_dir_path
