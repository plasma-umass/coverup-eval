# file: lib/ansible/vars/fact_cache.py:22-28
# asked: {"lines": [22, 24, 25, 26, 28], "branches": [[25, 26], [25, 28]]}
# gained: {"lines": [22, 24, 25, 26, 28], "branches": [[25, 26], [25, 28]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.vars.fact_cache import FactCache
from ansible.errors import AnsibleError
from ansible.plugins.loader import cache_loader

@pytest.fixture
def mock_cache_loader(monkeypatch):
    mock_loader = MagicMock()
    monkeypatch.setattr(cache_loader, 'get', mock_loader)
    return mock_loader

def test_fact_cache_initialization_success(mock_cache_loader):
    mock_cache_loader.return_value = MagicMock()
    fact_cache = FactCache()
    assert fact_cache._plugin is not None

def test_fact_cache_initialization_failure(mock_cache_loader):
    mock_cache_loader.return_value = None
    with pytest.raises(AnsibleError, match='Unable to load the facts cache plugin'):
        FactCache()
