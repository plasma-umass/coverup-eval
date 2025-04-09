# file lib/ansible/module_utils/facts/system/distribution.py:677-693
# lines [677, 678, 679, 684, 685, 686, 687, 688, 690, 691, 693]
# branches ['687->688', '687->690']

import pytest
from ansible.module_utils.facts.system.distribution import DistributionFactCollector
from unittest.mock import Mock

@pytest.fixture
def mock_module():
    return Mock()

def test_distribution_fact_collector_no_module():
    collector = DistributionFactCollector()
    result = collector.collect(module=None)
    assert result == {}

def test_distribution_fact_collector_with_module(mock_module, mocker):
    mock_distribution = mocker.patch('ansible.module_utils.facts.system.distribution.Distribution')
    mock_distribution_instance = mock_distribution.return_value
    mock_distribution_instance.get_distribution_facts.return_value = {
        'distribution_version': '1.0',
        'distribution_release': '1',
        'distribution_major_version': '1',
        'os_family': 'Linux'
    }

    collector = DistributionFactCollector()
    result = collector.collect(module=mock_module)
    
    assert result == {
        'distribution_version': '1.0',
        'distribution_release': '1',
        'distribution_major_version': '1',
        'os_family': 'Linux'
    }
    mock_distribution.assert_called_once_with(module=mock_module)
    mock_distribution_instance.get_distribution_facts.assert_called_once()
