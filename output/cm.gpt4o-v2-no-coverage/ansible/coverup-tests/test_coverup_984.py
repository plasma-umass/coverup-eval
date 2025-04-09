# file: lib/ansible/vars/fact_cache.py:54-55
# asked: {"lines": [54, 55], "branches": []}
# gained: {"lines": [54, 55], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.errors import AnsibleError
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def mock_cache_loader(mocker):
    mocker.patch('ansible.vars.fact_cache.cache_loader.get', return_value=MagicMock())

def test_fact_cache_keys(mock_cache_loader):
    fact_cache = FactCache()
    keys = fact_cache.keys()
    assert keys == fact_cache._plugin.keys()
