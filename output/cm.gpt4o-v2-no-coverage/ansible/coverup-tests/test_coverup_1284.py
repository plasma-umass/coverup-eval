# file: lib/ansible/galaxy/api.py:255-286
# asked: {"lines": [279, 280, 284], "branches": [[278, 279], [283, 284]]}
# gained: {"lines": [279, 280, 284], "branches": [[278, 279], [283, 284]]}

import pytest
import os
from unittest.mock import patch, MagicMock
from ansible.galaxy.api import GalaxyAPI
from ansible import constants as C
from ansible.module_utils._text import to_bytes

@pytest.fixture
def mock_config(monkeypatch):
    mock_config = MagicMock()
    mock_config.get_config_value.return_value = '/tmp/galaxy_cache'
    monkeypatch.setattr(C, 'config', mock_config)

@pytest.fixture
def mock_display(monkeypatch):
    mock_display = MagicMock()
    monkeypatch.setattr('ansible.galaxy.api.display', mock_display)
    return mock_display

@pytest.fixture
def mock_cache_lock(monkeypatch):
    mock_lock = MagicMock()
    monkeypatch.setattr('ansible.galaxy.api._CACHE_LOCK', mock_lock)
    return mock_lock

@pytest.fixture
def mock_load_cache(monkeypatch):
    mock_load = MagicMock()
    monkeypatch.setattr('ansible.galaxy.api._load_cache', mock_load)
    return mock_load

def test_galaxy_api_init_no_cache(mock_config, mock_display, mock_cache_lock, mock_load_cache):
    api = GalaxyAPI(galaxy='test_galaxy', name='test_name', url='http://test_url', no_cache=True)
    assert api.galaxy == 'test_galaxy'
    assert api.name == 'test_name'
    assert api.api_server == 'http://test_url'
    assert api._cache is None
    mock_display.debug.assert_called_with('Validate TLS certificates for http://test_url: True')

def test_galaxy_api_init_with_cache(mock_config, mock_display, mock_cache_lock, mock_load_cache):
    mock_load_cache.return_value = {'key': 'value'}
    api = GalaxyAPI(galaxy='test_galaxy', name='test_name', url='http://test_url', no_cache=False)
    assert api._cache == {'key': 'value'}
    mock_load_cache.assert_called_once()

def test_galaxy_api_init_clear_cache(mock_config, mock_display, mock_cache_lock, mock_load_cache):
    with patch('os.path.exists', return_value=True), patch('os.remove') as mock_remove:
        api = GalaxyAPI(galaxy='test_galaxy', name='test_name', url='http://test_url', clear_response_cache=True)
        mock_remove.assert_called_once_with(to_bytes('/tmp/galaxy_cache/api.json'))
        mock_display.vvvv.assert_called_with('Clearing cache file (/tmp/galaxy_cache/api.json)')
