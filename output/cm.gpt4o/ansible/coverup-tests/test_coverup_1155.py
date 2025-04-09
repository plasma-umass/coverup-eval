# file lib/ansible/galaxy/api.py:255-286
# lines [277, 278, 279, 280, 284]
# branches ['276->277', '278->279', '278->282', '283->284']

import os
import pytest
from unittest import mock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def mock_cache_lock(mocker):
    return mocker.patch('ansible.galaxy.api._CACHE_LOCK', mock.MagicMock())

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.galaxy.api.display')

@pytest.fixture
def mock_os_path_exists(mocker):
    return mocker.patch('os.path.exists')

@pytest.fixture
def mock_os_remove(mocker):
    return mocker.patch('os.remove')

@pytest.fixture
def mock_load_cache(mocker):
    return mocker.patch('ansible.galaxy.api._load_cache')

@pytest.fixture
def mock_makedirs_safe(mocker):
    return mocker.patch('ansible.galaxy.api.makedirs_safe')

@pytest.fixture
def mock_to_bytes(mocker):
    return mocker.patch('ansible.galaxy.api.to_bytes', return_value=b'/mock/cache/dir')

@pytest.fixture
def mock_config(mocker):
    mock_config = mocker.patch('ansible.galaxy.api.C.config.get_config_value')
    mock_config.return_value = '/mock/cache/dir'
    return mock_config

def test_galaxy_api_clear_cache(mock_cache_lock, mock_display, mock_os_path_exists, mock_os_remove, mock_makedirs_safe, mock_to_bytes, mock_config):
    mock_os_path_exists.return_value = True
    api = GalaxyAPI(galaxy='test_galaxy', name='test_name', url='http://test.url', clear_response_cache=True)
    
    mock_cache_lock.__enter__.assert_called_once()
    mock_cache_lock.__exit__.assert_called_once()
    mock_os_path_exists.assert_called_once_with(b'/mock/cache/dir/api.json')
    mock_display.vvvv.assert_called_once_with("Clearing cache file (/mock/cache/dir/api.json)")
    mock_os_remove.assert_called_once_with(b'/mock/cache/dir/api.json')

def test_galaxy_api_load_cache(mock_cache_lock, mock_display, mock_os_path_exists, mock_load_cache, mock_makedirs_safe, mock_to_bytes, mock_config):
    api = GalaxyAPI(galaxy='test_galaxy', name='test_name', url='http://test.url', no_cache=False)
    
    mock_load_cache.assert_called_once_with(b'/mock/cache/dir/api.json')
    assert api._cache == mock_load_cache.return_value
