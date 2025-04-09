# file: lib/ansible/module_utils/facts/system/distribution.py:677-693
# asked: {"lines": [677, 678, 679, 684, 685, 686, 687, 688, 690, 691, 693], "branches": [[687, 688], [687, 690]]}
# gained: {"lines": [677, 678, 679, 684, 685, 686, 687, 688, 690, 691, 693], "branches": [[687, 688], [687, 690]]}

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFactCollector
from unittest.mock import Mock

@pytest.fixture
def mock_module():
    return Mock()

def test_collect_with_module(mock_module, monkeypatch):
    # Mock the Distribution class and its get_distribution_facts method
    mock_distribution = Mock()
    mock_distribution.get_distribution_facts.return_value = {'key': 'value'}
    monkeypatch.setattr('ansible.module_utils.facts.system.distribution.Distribution', lambda module: mock_distribution)

    collector = DistributionFactCollector()
    result = collector.collect(module=mock_module)
    
    assert result == {'key': 'value'}
    mock_distribution.get_distribution_facts.assert_called_once()

def test_collect_without_module():
    collector = DistributionFactCollector()
    result = collector.collect(module=None)
    
    assert result == {}
