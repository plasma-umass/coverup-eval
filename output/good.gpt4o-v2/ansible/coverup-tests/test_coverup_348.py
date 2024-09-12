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

def test_collect_with_module(mock_module, mocker):
    collector = DistributionFactCollector()
    collected_facts = {'some_fact': 'some_value'}
    
    mocker.patch.object(Distribution, 'get_distribution_facts', return_value={'distribution': 'test_distro'})
    
    result = collector.collect(module=mock_module, collected_facts=collected_facts)
    
    assert result == {'distribution': 'test_distro'}

def test_collect_without_module():
    collector = DistributionFactCollector()
    collected_facts = {'some_fact': 'some_value'}
    
    result = collector.collect(module=None, collected_facts=collected_facts)
    
    assert result == {}
