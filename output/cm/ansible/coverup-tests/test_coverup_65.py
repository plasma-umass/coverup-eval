# file lib/ansible/galaxy/api.py:255-286
# lines [255, 257, 258, 259, 260, 262, 263, 264, 265, 266, 267, 268, 269, 270, 272, 273, 274, 276, 277, 278, 279, 280, 282, 283, 284, 286]
# branches ['276->277', '276->282', '278->279', '278->282', '283->284', '283->286']

import os
import pytest
from unittest.mock import MagicMock, patch
from ansible.galaxy.api import GalaxyAPI
from ansible.utils.display import Display

# Mock the display object to prevent actual output during tests
@pytest.fixture
def mock_display(mocker):
    mocker.patch.object(Display, 'vvvv')
    mocker.patch.object(Display, 'debug')

# Mock the _load_cache function to prevent actual file operations
@pytest.fixture
def mock_load_cache(mocker):
    return mocker.patch('ansible.galaxy.api._load_cache', return_value={})

# Mock the makedirs_safe function to prevent actual directory creation
@pytest.fixture
def mock_makedirs_safe(mocker):
    return mocker.patch('ansible.galaxy.api.makedirs_safe')

# Mock the os.path.exists function to control its return value
@pytest.fixture
def mock_path_exists(mocker):
    return mocker.patch('os.path.exists', return_value=True)

# Mock the os.remove function to prevent actual file deletion
@pytest.fixture
def mock_os_remove(mocker):
    return mocker.patch('os.remove')

# Test function to improve coverage
def test_galaxy_api_clear_response_cache(
    mock_display, mock_load_cache, mock_makedirs_safe, mock_path_exists, mock_os_remove
):
    # Setup the GalaxyAPI instance with clear_response_cache=True
    api = GalaxyAPI(
        galaxy='test_galaxy',
        name='test_name',
        url='http://test_url',
        clear_response_cache=True,
        no_cache=False
    )

    # Assertions to verify the cache file removal and cache loading
    mock_os_remove.assert_called_once_with(api._b_cache_path)
    mock_load_cache.assert_called_once_with(api._b_cache_path)

    # Verify that the cache is not None since no_cache=False
    assert api._cache is not None

    # Cleanup after test
    if os.path.exists(api._b_cache_path):
        os.remove(api._b_cache_path)
