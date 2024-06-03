# file mimesis/providers/path.py:98-108
# lines [98, 106, 107, 108]
# branches []

import pytest
from mimesis.providers.path import Path
from mimesis.data import PROJECT_NAMES
from unittest.mock import patch, MagicMock

@pytest.fixture
def path_provider():
    return Path()

def test_project_dir(path_provider, mocker):
    mock_dev_dir = "Development"
    mock_project = "Falcon"
    
    # Mock the dev_dir method to return a specific value
    mocker.patch.object(path_provider, 'dev_dir', return_value=mock_dev_dir)
    
    # Mock the random choice to return a specific project name
    mocker.patch.object(path_provider.random, 'choice', return_value=mock_project)
    
    # Mock the _pathlib_home to return a specific path
    mock_pathlib_home = mocker.patch.object(path_provider, '_pathlib_home', new_callable=MagicMock)
    mock_pathlib_home.__truediv__.return_value = mock_pathlib_home
    mock_pathlib_home.__str__.return_value = "/home/sherika/Development/Falcon"
    
    expected_path = "/home/sherika/Development/Falcon"
    result = path_provider.project_dir()
    
    assert result == expected_path
