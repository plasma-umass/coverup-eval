# file lib/ansible/galaxy/api.py:255-286
# lines []
# branches ['278->282']

import os
import pytest
from unittest import mock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def mock_cache_lock(mocker):
    return mocker.patch('ansible.galaxy.api._CACHE_LOCK', new_callable=mock.MagicMock)

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.galaxy.api.display', new_callable=mock.MagicMock)

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
def mock_to_text(mocker):
    return mocker.patch('ansible.galaxy.api.to_text', return_value='/mock/cache/dir/api.json')

def test_galaxy_api_clear_cache(mock_cache_lock, mock_display, mock_os_path_exists, mock_os_remove, mock_load_cache, mock_makedirs_safe, mock_to_bytes, mock_to_text):
    mock_os_path_exists.return_value = True

    api = GalaxyAPI(
        galaxy='test_galaxy',
        name='test_name',
        url='http://test.url',
        clear_response_cache=True,
        no_cache=True
    )

    mock_cache_lock.__enter__.assert_called_once()
    mock_cache_lock.__exit__.assert_called_once()
    mock_os_path_exists.assert_called_once_with(b'/mock/cache/dir/api.json')
    mock_display.vvvv.assert_called_once_with("Clearing cache file (/mock/cache/dir/api.json)")
    mock_os_remove.assert_called_once_with(b'/mock/cache/dir/api.json')
    assert api._cache is None

def test_galaxy_api_no_cache(mock_cache_lock, mock_display, mock_os_path_exists, mock_os_remove, mock_load_cache, mock_makedirs_safe, mock_to_bytes, mock_to_text):
    mock_os_path_exists.return_value = False

    api = GalaxyAPI(
        galaxy='test_galaxy',
        name='test_name',
        url='http://test.url',
        clear_response_cache=False,
        no_cache=False
    )

    mock_cache_lock.__enter__.assert_not_called()
    mock_cache_lock.__exit__.assert_not_called()
    mock_os_path_exists.assert_not_called()
    mock_display.vvvv.assert_not_called()
    mock_os_remove.assert_not_called()
    mock_load_cache.assert_called_once_with(b'/mock/cache/dir/api.json')
    assert api._cache is not None

def test_galaxy_api_clear_cache_no_file(mock_cache_lock, mock_display, mock_os_path_exists, mock_os_remove, mock_load_cache, mock_makedirs_safe, mock_to_bytes, mock_to_text):
    mock_os_path_exists.return_value = False

    api = GalaxyAPI(
        galaxy='test_galaxy',
        name='test_name',
        url='http://test.url',
        clear_response_cache=True,
        no_cache=True
    )

    mock_cache_lock.__enter__.assert_called_once()
    mock_cache_lock.__exit__.assert_called_once()
    mock_os_path_exists.assert_called_once_with(b'/mock/cache/dir/api.json')
    mock_display.vvvv.assert_not_called()
    mock_os_remove.assert_not_called()
    assert api._cache is None
