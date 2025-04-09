# file: lib/ansible/module_utils/facts/system/distribution.py:677-693
# asked: {"lines": [677, 678, 679, 684, 685, 686, 687, 688, 690, 691, 693], "branches": [[687, 688], [687, 690]]}
# gained: {"lines": [677, 678, 679, 684, 685, 686, 687, 688, 690, 691, 693], "branches": [[687, 688], [687, 690]]}

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFactCollector, Distribution
from ansible.module_utils.basic import AnsibleModule

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock(spec=AnsibleModule)
    return module

def test_collect_with_module(mock_module):
    collector = DistributionFactCollector()
    collected_facts = {}
    result = collector.collect(module=mock_module, collected_facts=collected_facts)
    
    assert isinstance(result, dict)
    assert 'distribution' in result

def test_collect_without_module():
    collector = DistributionFactCollector()
    collected_facts = {}
    result = collector.collect(module=None, collected_facts=collected_facts)
    
    assert result == {}

def test_distribution_get_facts(mock_module):
    distribution = Distribution(module=mock_module)
    facts = distribution.get_distribution_facts()
    
    assert isinstance(facts, dict)
