# file: lib/ansible/vars/fact_cache.py:22-28
# asked: {"lines": [22, 24, 25, 26, 28], "branches": [[25, 26], [25, 28]]}
# gained: {"lines": [22, 24, 25, 26, 28], "branches": [[25, 26], [25, 28]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.loader import cache_loader
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def mock_cache_loader():
    with patch('ansible.plugins.loader.cache_loader.get') as mock_get:
        yield mock_get

def test_fact_cache_init_success(mock_cache_loader):
    mock_plugin = MagicMock()
    mock_cache_loader.return_value = mock_plugin

    fact_cache = FactCache()
    assert fact_cache._plugin == mock_plugin

def test_fact_cache_init_failure(mock_cache_loader):
    mock_cache_loader.return_value = None

    with pytest.raises(AnsibleError, match='Unable to load the facts cache plugin'):
        FactCache()
