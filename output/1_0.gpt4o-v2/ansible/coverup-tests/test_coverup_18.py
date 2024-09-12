# file: lib/ansible/module_utils/facts/system/env.py:26-37
# asked: {"lines": [26, 27, 28, 30, 31, 32, 34, 35, 37], "branches": [[34, 35], [34, 37]]}
# gained: {"lines": [26, 27, 28, 30, 31, 32, 34, 35, 37], "branches": [[34, 35], [34, 37]]}

import os
import pytest
from ansible.module_utils.six import iteritems
from ansible.module_utils.facts.collector import BaseFactCollector
from ansible.module_utils.facts.system.env import EnvFactCollector

@pytest.fixture
def mock_environ(monkeypatch):
    mock_env = {
        'TEST_ENV_VAR': 'test_value',
        'ANOTHER_ENV_VAR': 'another_value'
    }
    monkeypatch.setattr(os, 'environ', mock_env)
    return mock_env

def test_env_fact_collector_collect(mock_environ):
    collector = EnvFactCollector()
    collected_facts = collector.collect()
    
    assert 'env' in collected_facts
    assert collected_facts['env'] == mock_environ
