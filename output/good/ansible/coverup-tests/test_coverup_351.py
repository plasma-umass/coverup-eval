# file lib/ansible/module_utils/facts/system/distribution.py:677-693
# lines [677, 678, 679, 684, 685, 686, 687, 688, 690, 691, 693]
# branches ['687->688', '687->690']

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFactCollector
from unittest.mock import MagicMock

# Mock the Distribution class to return a specific set of facts
class MockDistribution:
    def __init__(self, module):
        pass

    def get_distribution_facts(self):
        return {
            'distribution_version': '20.04',
            'distribution_release': 'focal',
            'distribution_major_version': '20',
            'os_family': 'Debian'
        }

@pytest.fixture
def mock_distribution(mocker):
    mocker.patch(
        'ansible.module_utils.facts.system.distribution.Distribution',
        new=MockDistribution
    )

def test_distribution_fact_collector(mock_distribution):
    module_mock = MagicMock()
    fact_collector = DistributionFactCollector()

    # Call the collect method and check the returned facts
    facts = fact_collector.collect(module=module_mock)
    assert facts['distribution_version'] == '20.04'
    assert facts['distribution_release'] == 'focal'
    assert facts['distribution_major_version'] == '20'
    assert facts['os_family'] == 'Debian'

    # Call the collect method without a module and check for empty dict
    facts_without_module = fact_collector.collect(module=None)
    assert facts_without_module == {}
