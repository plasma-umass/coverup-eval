# file lib/ansible/module_utils/facts/system/env.py:26-37
# lines [26, 27, 28, 30, 31, 32, 34, 35, 37]
# branches ['34->35', '34->37']

import os
import pytest
from ansible.module_utils.facts.system.env import EnvFactCollector
from ansible.module_utils.six import iteritems

# Mocking iteritems to control the environment variables during the test
@pytest.fixture
def mock_iteritems(mocker):
    return mocker.patch('ansible.module_utils.facts.system.env.iteritems', return_value={'TEST_ENV_VAR': 'test_value'}.items())

def test_env_fact_collector(mock_iteritems):
    env_collector = EnvFactCollector()
    facts = env_collector.collect()
    assert 'env' in facts
    assert 'TEST_ENV_VAR' in facts['env']
    assert facts['env']['TEST_ENV_VAR'] == 'test_value'
    mock_iteritems.assert_called_once_with(os.environ)
