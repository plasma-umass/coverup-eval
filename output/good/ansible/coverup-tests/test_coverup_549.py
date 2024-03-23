# file lib/ansible/vars/fact_cache.py:22-28
# lines [22, 24, 25, 26, 28]
# branches ['25->26', '25->28']

import pytest
from ansible.errors import AnsibleError
from ansible.vars.fact_cache import FactCache
from ansible.plugins.loader import cache_loader
from unittest.mock import MagicMock

# Assuming C is a configuration module that needs to be mocked
class C:
    CACHE_PLUGIN = 'nonexistent_plugin'

@pytest.fixture
def mock_cache_loader(mocker):
    mocker.patch.object(cache_loader, 'get', return_value=None)

def test_fact_cache_initialization_failure(mock_cache_loader):
    with pytest.raises(AnsibleError) as excinfo:
        FactCache()
    assert 'Unable to load the facts cache plugin' in str(excinfo.value)
