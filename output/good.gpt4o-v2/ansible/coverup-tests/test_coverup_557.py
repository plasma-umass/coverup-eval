# file: lib/ansible/vars/fact_cache.py:22-28
# asked: {"lines": [22, 24, 25, 26, 28], "branches": [[25, 26], [25, 28]]}
# gained: {"lines": [22, 24, 25, 26, 28], "branches": [[25, 26], [25, 28]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.loader import cache_loader
from ansible import constants as C
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.vars.fact_cache import FactCache

class MockCacheLoader:
    def __init__(self, plugin):
        self.plugin = plugin

    def get(self, plugin_name):
        return self.plugin

@pytest.fixture
def mock_cache_loader(monkeypatch):
    def mock_get(plugin_name):
        if plugin_name == "valid_plugin":
            return "plugin_instance"
        return None

    monkeypatch.setattr(cache_loader, "get", mock_get)

def test_fact_cache_init_success(mock_cache_loader):
    C.CACHE_PLUGIN = "valid_plugin"
    fact_cache = FactCache()
    assert fact_cache._plugin == "plugin_instance"

def test_fact_cache_init_failure(mock_cache_loader):
    C.CACHE_PLUGIN = "invalid_plugin"
    with pytest.raises(AnsibleError, match="Unable to load the facts cache plugin"):
        FactCache()
