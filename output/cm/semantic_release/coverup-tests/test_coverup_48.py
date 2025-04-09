# file semantic_release/settings.py:64-74
# lines []
# branches ['69->74']

import os
import pytest
from unittest.mock import mock_open, patch
from semantic_release.settings import _config_from_pyproject
from tomlkit.exceptions import TOMLKitError

@pytest.fixture
def mock_pyproject_file():
    pyproject_content = ""
    return mock_open(read_data=pyproject_content)

def test_config_from_pyproject_with_empty_toml(mocker, mock_pyproject_file):
    # Mock the os.path.isfile to return True
    mocker.patch('os.path.isfile', return_value=True)
    # Mock the open function to read the empty TOML content
    mocker.patch('builtins.open', mock_pyproject_file())
    # Mock the tomlkit.loads to return an empty dictionary
    mocker.patch('tomlkit.loads', return_value={})

    # Call the function to test the empty pyproject.toml handling
    result = _config_from_pyproject('pyproject.toml')

    # Assert that the result is an empty dictionary
    assert result == {}

    # Cleanup
    mocker.stopall()
