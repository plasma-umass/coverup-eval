# file: lib/ansible/galaxy/api.py:426-429
# asked: {"lines": [428, 429], "branches": []}
# gained: {"lines": [428, 429], "branches": []}

import pytest
import json
import os
from unittest.mock import mock_open, patch
from ansible.module_utils._text import to_bytes
from ansible.galaxy.api import GalaxyAPI

@pytest.fixture
def galaxy_api_instance():
    return GalaxyAPI(
        galaxy=None,
        name="test",
        url="http://test.url",
        username="user",
        password="pass",
        token="token",
        validate_certs=True,
        available_api_versions=None,
        clear_response_cache=False,
        no_cache=True,
        priority=float('inf')
    )

def test_set_cache(galaxy_api_instance, monkeypatch):
    mock_cache = {"key": "value"}
    galaxy_api_instance._cache = mock_cache
    galaxy_api_instance._b_cache_path = "/tmp/test_cache.json"

    m = mock_open()
    with patch("builtins.open", m):
        galaxy_api_instance._set_cache()

    m.assert_called_once_with("/tmp/test_cache.json", mode='wb')
    handle = m()
    handle.write.assert_called_once_with(to_bytes(json.dumps(mock_cache), errors='surrogate_or_strict'))

    # Clean up
    if os.path.exists("/tmp/test_cache.json"):
        os.remove("/tmp/test_cache.json")
