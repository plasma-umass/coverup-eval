# file: lib/ansible/galaxy/api.py:255-286
# asked: {"lines": [277, 278, 279, 280, 284], "branches": [[276, 277], [278, 279], [278, 282], [283, 284]]}
# gained: {"lines": [277, 278, 279, 280, 284], "branches": [[276, 277], [278, 279], [283, 284]]}

import pytest
import os
from unittest import mock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def mock_cache_lock():
    with mock.patch('ansible.galaxy.api._CACHE_LOCK'):
        yield

@pytest.fixture
def mock_display_vvvv():
    with mock.patch('ansible.galaxy.api.display.vvvv') as mock_vvvv:
        yield mock_vvvv

@pytest.fixture
def mock_display_debug():
    with mock.patch('ansible.galaxy.api.display.debug') as mock_debug:
        yield mock_debug

@pytest.fixture
def mock_os_path_exists():
    with mock.patch('os.path.exists') as mock_exists:
        yield mock_exists

@pytest.fixture
def mock_os_remove():
    with mock.patch('os.remove') as mock_remove:
        yield mock_remove

@pytest.fixture
def mock_load_cache():
    with mock.patch('ansible.galaxy.api._load_cache') as mock_load:
        yield mock_load

@pytest.fixture
def mock_makedirs_safe():
    with mock.patch('ansible.galaxy.api.makedirs_safe'):
        yield

@pytest.fixture
def mock_to_bytes():
    with mock.patch('ansible.galaxy.api.to_bytes', return_value=b'/mock/cache/dir'):
        yield

@pytest.fixture
def mock_config_get_config_value():
    with mock.patch('ansible.galaxy.api.C.config.get_config_value', return_value='/mock/cache/dir'):
        yield

def test_clear_response_cache(mock_cache_lock, mock_os_path_exists, mock_os_remove, mock_display_vvvv, mock_makedirs_safe, mock_to_bytes, mock_config_get_config_value):
    mock_os_path_exists.return_value = True
    api = GalaxyAPI(galaxy=None, name='test', url='http://example.com', clear_response_cache=True)
    mock_os_path_exists.assert_called_once_with(api._b_cache_path)
    mock_display_vvvv.assert_called_once_with("Clearing cache file (%s)" % '/mock/cache/dir/api.json')
    mock_os_remove.assert_called_once_with(api._b_cache_path)

def test_no_cache(mock_load_cache, mock_makedirs_safe, mock_to_bytes, mock_config_get_config_value):
    api = GalaxyAPI(galaxy=None, name='test', url='http://example.com', no_cache=False)
    mock_load_cache.assert_called_once_with(api._b_cache_path)
    assert api._cache is not None
