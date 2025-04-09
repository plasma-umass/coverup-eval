# file lib/ansible/module_utils/facts/ansible_collector.py:76-100
# lines [76, 77, 79, 81, 82, 84, 87, 88, 89, 90, 91, 95, 98, 100]
# branches ['81->82', '81->100']

import pytest
from ansible.module_utils.facts.ansible_collector import AnsibleFactCollector
from ansible.module_utils.facts import collector
import sys
from unittest.mock import MagicMock, patch

# Mock collector that raises an exception
class ExceptionRaisingCollector(collector.BaseFactCollector):
    def collect_with_namespace(self, module=None, collected_facts=None):
        raise Exception("Test exception")

# Mock collector that returns a simple fact
class SimpleCollector(collector.BaseFactCollector):
    def collect_with_namespace(self, module=None, collected_facts=None):
        return {'simple_fact': 'simple_value'}

@pytest.fixture
def mock_stderr(mocker):
    return mocker.patch('sys.stderr.write')

def test_ansible_fact_collector_with_exception(mock_stderr):
    # Arrange
    exception_collector = ExceptionRaisingCollector()
    simple_collector = SimpleCollector()
    fact_collector = AnsibleFactCollector([exception_collector, simple_collector])

    # Act
    facts = fact_collector.collect()

    # Assert
    # Check that the exception was written to stderr
    mock_stderr.assert_called()
    calls = mock_stderr.call_args_list
    assert any("Test exception" in str(call) for call in calls)

    # Check that the simple fact was collected despite the exception
    assert facts == {'simple_fact': 'simple_value'}
