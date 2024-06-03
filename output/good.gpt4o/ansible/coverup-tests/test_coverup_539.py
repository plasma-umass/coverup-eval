# file lib/ansible/vars/fact_cache.py:22-28
# lines [22, 24, 25, 26, 28]
# branches ['25->26', '25->28']

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.vars.fact_cache import FactCache

@pytest.fixture
def mock_cache_loader(mocker):
    return mocker.patch('ansible.vars.fact_cache.cache_loader')

@pytest.fixture
def mock_constants(mocker):
    return mocker.patch('ansible.vars.fact_cache.C')

def test_fact_cache_initialization_success(mock_cache_loader, mock_constants):
    mock_constants.CACHE_PLUGIN = 'some_plugin'
    mock_cache_loader.get.return_value = MagicMock()

    fact_cache = FactCache()
    assert isinstance(fact_cache, FactCache)

def test_fact_cache_initialization_failure(mock_cache_loader, mock_constants):
    mock_constants.CACHE_PLUGIN = 'some_plugin'
    mock_cache_loader.get.return_value = None

    with pytest.raises(AnsibleError, match='Unable to load the facts cache plugin'):
        FactCache()
