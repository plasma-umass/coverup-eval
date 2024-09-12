# file: lib/ansible/galaxy/api.py:426-429
# asked: {"lines": [426, 427, 428, 429], "branches": []}
# gained: {"lines": [426, 427, 428, 429], "branches": []}

import pytest
import json
import os
from unittest import mock
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api(tmp_path):
    class MockGalaxyAPI(GalaxyAPI):
        def __init__(self):
            self._b_cache_path = tmp_path / "cache.json"
            self._cache = {"key": "value"}
    
    return MockGalaxyAPI()

def test_set_cache(galaxy_api, monkeypatch):
    mock_open = mock.mock_open()
    monkeypatch.setattr("builtins.open", mock_open)
    
    galaxy_api._set_cache()
    
    mock_open.assert_called_once_with(galaxy_api._b_cache_path, mode='wb')
    handle = mock_open()
    handle.write.assert_called_once_with(b'{"key": "value"}')
    
    # Clean up
    if os.path.exists(galaxy_api._b_cache_path):
        os.remove(galaxy_api._b_cache_path)
