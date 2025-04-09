# file: lib/ansible/module_utils/facts/system/distribution.py:677-693
# asked: {"lines": [677, 678, 679, 684, 685, 686, 687, 688, 690, 691, 693], "branches": [[687, 688], [687, 690]]}
# gained: {"lines": [677, 678, 679, 684, 685, 686, 687, 688, 690, 691, 693], "branches": [[687, 688], [687, 690]]}

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFactCollector
from ansible.module_utils.facts.system.distribution import Distribution

class MockModule:
    def __init__(self, params=None):
        self.params = params or {}

@pytest.fixture
def mock_module():
    return MockModule()

def test_collect_no_module():
    collector = DistributionFactCollector()
    result = collector.collect()
    assert result == {}

def test_collect_with_module(mock_module, mocker):
    collector = DistributionFactCollector()
    mock_distribution = mocker.patch('ansible.module_utils.facts.system.distribution.Distribution')
    mock_distribution_instance = mock_distribution.return_value
    mock_distribution_instance.get_distribution_facts.return_value = {'distribution': 'test_distro'}
    
    result = collector.collect(module=mock_module)
    
    assert result == {'distribution': 'test_distro'}
    mock_distribution.assert_called_once_with(module=mock_module)
    mock_distribution_instance.get_distribution_facts.assert_called_once()
