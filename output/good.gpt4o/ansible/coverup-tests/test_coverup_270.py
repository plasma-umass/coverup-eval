# file lib/ansible/module_utils/facts/ansible_collector.py:76-100
# lines [76, 77, 79, 81, 82, 84, 87, 88, 89, 90, 91, 95, 98, 100]
# branches ['81->82', '81->100']

import pytest
import sys
from unittest import mock
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.facts.collector import BaseFactCollector

class MockCollector(BaseFactCollector):
    def collect_with_namespace(self, module=None, collected_facts=None):
        return {"mock_fact": "value"}

class ExceptionCollector(BaseFactCollector):
    def collect_with_namespace(self, module=None, collected_facts=None):
        raise Exception("Test exception")

@pytest.fixture
def mock_collectors():
    return [MockCollector(), ExceptionCollector()]

@pytest.fixture
def ansible_fact_collector(mock_collectors):
    collector = AnsibleFactCollector()
    collector.collectors = mock_collectors
    return collector

def test_collect_with_exception_handling(ansible_fact_collector, mocker):
    mock_stderr_write = mocker.patch('sys.stderr.write')
    collected_facts = ansible_fact_collector.collect()
    
    # Verify that the facts were collected correctly
    assert collected_facts == {"mock_fact": "value"}
    
    # Verify that the exception was caught and written to stderr
    mock_stderr_write.assert_any_call("Exception('Test exception')")
    mock_stderr_write.assert_any_call('\n')
