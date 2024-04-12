# file lib/ansible/galaxy/api.py:426-429
# lines [426, 427, 428, 429]
# branches []

import json
import pytest
from unittest.mock import MagicMock, mock_open, patch
from ansible.galaxy.api import GalaxyAPI
from ansible.module_utils._text import to_bytes

# Assuming cache_lock is a decorator that needs to be mocked for testing
@pytest.fixture
def mock_cache_lock(mocker):
    mocker.patch('ansible.galaxy.api.cache_lock', lambda x: x)

@pytest.fixture
def galaxy_api_instance(tmp_path, mock_cache_lock):
    # Setup a temporary file to act as the cache file
    cache_file = tmp_path / "cache.json"
    # Create a GalaxyAPI instance with the temporary cache file path
    # Mock the required arguments for GalaxyAPI constructor
    galaxy = MagicMock()
    name = "test_name"
    url = "http://test_url"
    api_instance = GalaxyAPI(galaxy, name, url)
    api_instance._b_cache_path = str(cache_file)
    api_instance._cache = {'test': 'data'}
    return api_instance

def test_set_cache(galaxy_api_instance):
    # Mock the open function to use an in-memory file instead of disk I/O
    with patch("builtins.open", mock_open()) as mocked_file:
        # Call the method that should write to the cache
        galaxy_api_instance._set_cache()

        # Assert that open was called with the correct arguments
        mocked_file.assert_called_once_with(galaxy_api_instance._b_cache_path, mode='wb')

        # Retrieve the file handle to the mocked file
        handle = mocked_file()

        # Assert that the correct data was written to the file
        expected_data = to_bytes(json.dumps(galaxy_api_instance._cache), errors='surrogate_or_strict')
        handle.write.assert_called_once_with(expected_data)

        # No cleanup is necessary as we are using a mock and a temporary path fixture
