# file lib/ansible/galaxy/api.py:426-429
# lines [426, 427, 428, 429]
# branches []

import pytest
import json
import os
from unittest import mock
from ansible.galaxy.api import GalaxyAPI
from ansible.module_utils._text import to_bytes

@pytest.fixture
def mock_cache_lock(mocker):
    return mocker.patch('ansible.galaxy.api.cache_lock')

@pytest.fixture
def temp_cache_file(tmp_path):
    return tmp_path / "cache_file"

@pytest.fixture
def galaxy_api_instance(temp_cache_file, mock_cache_lock):
    class TestGalaxyAPI(GalaxyAPI):
        def __init__(self, cache, cache_path):
            self._cache = cache
            self._b_cache_path = cache_path

    return TestGalaxyAPI({"key": "value"}, temp_cache_file)

def test_set_cache(galaxy_api_instance, temp_cache_file):
    galaxy_api_instance._set_cache()
    
    assert temp_cache_file.exists()
    with open(temp_cache_file, 'rb') as fd:
        data = fd.read()
        assert data == to_bytes(json.dumps({"key": "value"}), errors='surrogate_or_strict')
