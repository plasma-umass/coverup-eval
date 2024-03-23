# file mimesis/providers/path.py:85-96
# lines [93, 94, 95, 96]
# branches []

import pytest
from mimesis.providers import Path
from mimesis.enums import Gender
from unittest.mock import patch
from pathlib import Path as pathlib_Path

# Constants to be used for mocking
MOCKED_USER = "mocked_user"
MOCKED_FOLDER = "Development"
MOCKED_STACK = "Python"
MOCKED_HOME_PATH = pathlib_Path("/home")

@pytest.fixture
def path_provider():
    return Path()

def test_dev_dir(path_provider, mocker):
    # Mock the user method to return a constant user name
    mocker.patch.object(path_provider, 'user', return_value=MOCKED_USER)
    # Mock the random.choice method to return constant values for folder and stack
    mocker.patch.object(path_provider.random, 'choice', side_effect=[MOCKED_FOLDER, MOCKED_STACK])
    # Mock the _pathlib_home attribute to return a constant path
    mocker.patch.object(path_provider, '_pathlib_home', MOCKED_HOME_PATH)

    expected_path = str(MOCKED_HOME_PATH / MOCKED_USER / MOCKED_FOLDER / MOCKED_STACK)
    generated_path = path_provider.dev_dir()

    assert generated_path == expected_path, f"Expected path {expected_path}, but got {generated_path}"
