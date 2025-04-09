# file: lib/ansible/galaxy/api.py:426-429
# asked: {"lines": [426, 427, 428, 429], "branches": []}
# gained: {"lines": [426, 427, 428, 429], "branches": []}

import pytest
import json
import os
from unittest import mock
from ansible.galaxy.api import GalaxyAPI
from ansible.module_utils._text import to_bytes

@pytest.fixture
def galaxy_api_instance(tmp_path):
    class MockGalaxyAPI(GalaxyAPI):
        def __init__(self):
            self._b_cache_path = tmp_path / "cache_file"
            self._cache = {"key": "value"}

    return MockGalaxyAPI()

def test_set_cache(galaxy_api_instance, mocker):
    mocker.patch("ansible.galaxy.api.cache_lock", lambda x: x)
    galaxy_api_instance._set_cache()
    
    with open(galaxy_api_instance._b_cache_path, mode='rb') as fd:
        data = fd.read()
    
    assert data == to_bytes(json.dumps(galaxy_api_instance._cache), errors='surrogate_or_strict')
