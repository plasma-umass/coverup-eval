# file: lib/ansible/galaxy/api.py:426-429
# asked: {"lines": [426, 427, 428, 429], "branches": []}
# gained: {"lines": [426, 427, 428, 429], "branches": []}

import pytest
import json
from unittest import mock
from ansible.module_utils._text import to_bytes
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api_instance(tmp_path):
    class MockGalaxyAPI(GalaxyAPI):
        def __init__(self):
            self._b_cache_path = tmp_path / "cache.json"
            self._cache = {"key": "value"}
    
    return MockGalaxyAPI()

def test_set_cache(galaxy_api_instance):
    with mock.patch("ansible.galaxy.api._CACHE_LOCK"):
        galaxy_api_instance._set_cache()
    
    with open(galaxy_api_instance._b_cache_path, mode='rb') as fd:
        data = json.loads(fd.read().decode('utf-8'))
    
    assert data == galaxy_api_instance._cache
