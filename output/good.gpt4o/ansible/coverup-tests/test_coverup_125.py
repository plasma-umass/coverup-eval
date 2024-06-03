# file lib/ansible/module_utils/facts/collector.py:345-400
# lines [345, 346, 347, 348, 349, 350, 355, 357, 359, 361, 364, 366, 370, 372, 374, 379, 381, 384, 385, 386, 387, 388, 390, 392, 394, 395, 397, 398, 400]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from collections import defaultdict
from ansible.module_utils.facts.collector import collector_classes_from_gather_subset

@pytest.fixture
def mock_platform_info():
    return {'system': 'Linux'}

@pytest.fixture
def mock_all_collector_classes():
    return [MagicMock(name='Collector1'), MagicMock(name='Collector2')]

@pytest.fixture
def mock_valid_subsets():
    return frozenset(['all', 'hardware'])

@pytest.fixture
def mock_minimal_gather_subset():
    return frozenset(['minimal'])

@pytest.fixture
def mock_gather_subset():
    return frozenset(['all'])

@pytest.fixture
def mock_gather_timeout():
    return 10

@pytest.fixture
def mock_platform():
    with patch('ansible.module_utils.facts.collector.platform') as mock_platform:
        mock_platform.system.return_value = 'Linux'
        yield mock_platform

@pytest.fixture
def mock_timeout():
    with patch('ansible.module_utils.facts.collector.timeout') as mock_timeout:
        mock_timeout.DEFAULT_GATHER_TIMEOUT = 5
        yield mock_timeout

@pytest.fixture
def mock_find_collectors_for_platform():
    with patch('ansible.module_utils.facts.collector.find_collectors_for_platform') as mock_func:
        mock_func.return_value = [MagicMock(name='Collector1'), MagicMock(name='Collector2')]
        yield mock_func

@pytest.fixture
def mock_build_fact_id_to_collector_map():
    with patch('ansible.module_utils.facts.collector.build_fact_id_to_collector_map') as mock_func:
        mock_func.return_value = ({'all': MagicMock(name='Collector1'), 'hardware': MagicMock(name='Collector2')}, defaultdict(set))
        yield mock_func

@pytest.fixture
def mock_get_collector_names():
    with patch('ansible.module_utils.facts.collector.get_collector_names') as mock_func:
        mock_func.return_value = ['all', 'hardware']
        yield mock_func

@pytest.fixture
def mock_solve_deps():
    with patch('ansible.module_utils.facts.collector._solve_deps') as mock_func:
        mock_func.return_value = ['all', 'hardware']
        yield mock_func

@pytest.fixture
def mock_build_dep_data():
    with patch('ansible.module_utils.facts.collector.build_dep_data') as mock_func:
        mock_func.return_value = {'all': [], 'hardware': []}
        yield mock_func

@pytest.fixture
def mock_tsort():
    with patch('ansible.module_utils.facts.collector.tsort') as mock_func:
        mock_func.return_value = [('all', []), ('hardware', [])]
        yield mock_func

@pytest.fixture
def mock_select_collector_classes():
    with patch('ansible.module_utils.facts.collector.select_collector_classes') as mock_func:
        mock_func.return_value = [MagicMock(name='Collector1'), MagicMock(name='Collector2')]
        yield mock_func

def test_collector_classes_from_gather_subset(mock_platform_info, mock_all_collector_classes, mock_valid_subsets,
                                              mock_minimal_gather_subset, mock_gather_subset, mock_gather_timeout,
                                              mock_platform, mock_timeout, mock_find_collectors_for_platform,
                                              mock_build_fact_id_to_collector_map, mock_get_collector_names,
                                              mock_solve_deps, mock_build_dep_data, mock_tsort,
                                              mock_select_collector_classes):
    result = collector_classes_from_gather_subset(
        all_collector_classes=mock_all_collector_classes,
        valid_subsets=mock_valid_subsets,
        minimal_gather_subset=mock_minimal_gather_subset,
        gather_subset=mock_gather_subset,
        gather_timeout=mock_gather_timeout,
        platform_info=mock_platform_info
    )

    assert len(result) == 2
    assert result[0]._mock_name == 'Collector1'
    assert result[1]._mock_name == 'Collector2'
    assert mock_timeout.GATHER_TIMEOUT == mock_gather_timeout
