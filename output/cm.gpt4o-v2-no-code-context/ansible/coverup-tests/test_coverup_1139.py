# file: lib/ansible/module_utils/facts/collector.py:345-400
# asked: {"lines": [355, 357, 359, 361, 364, 366, 370, 372, 374, 379, 381, 384, 385, 386, 387, 388, 390, 392, 394, 395, 397, 398, 400], "branches": []}
# gained: {"lines": [355, 357, 359, 361, 364, 366, 370, 372, 374, 379, 381, 384, 385, 386, 387, 388, 390, 392, 394, 395, 397, 398, 400], "branches": []}

import pytest
from unittest.mock import patch, MagicMock
from ansible.module_utils.facts.collector import collector_classes_from_gather_subset

@pytest.fixture
def mock_platform():
    with patch('ansible.module_utils.facts.collector.platform') as mock_platform:
        yield mock_platform

@pytest.fixture
def mock_timeout():
    with patch('ansible.module_utils.facts.collector.timeout') as mock_timeout:
        yield mock_timeout

@pytest.fixture
def mock_find_collectors_for_platform():
    with patch('ansible.module_utils.facts.collector.find_collectors_for_platform') as mock_find:
        yield mock_find

@pytest.fixture
def mock_build_fact_id_to_collector_map():
    with patch('ansible.module_utils.facts.collector.build_fact_id_to_collector_map') as mock_build:
        yield mock_build

@pytest.fixture
def mock_get_collector_names():
    with patch('ansible.module_utils.facts.collector.get_collector_names') as mock_get:
        yield mock_get

@pytest.fixture
def mock_solve_deps():
    with patch('ansible.module_utils.facts.collector._solve_deps') as mock_solve:
        yield mock_solve

@pytest.fixture
def mock_build_dep_data():
    with patch('ansible.module_utils.facts.collector.build_dep_data') as mock_build_dep:
        yield mock_build_dep

@pytest.fixture
def mock_tsort():
    with patch('ansible.module_utils.facts.collector.tsort') as mock_tsort:
        yield mock_tsort

@pytest.fixture
def mock_select_collector_classes():
    with patch('ansible.module_utils.facts.collector.select_collector_classes') as mock_select:
        yield mock_select

def test_collector_classes_from_gather_subset_all_lines(mock_platform, mock_timeout, mock_find_collectors_for_platform,
                                                        mock_build_fact_id_to_collector_map, mock_get_collector_names,
                                                        mock_solve_deps, mock_build_dep_data, mock_tsort,
                                                        mock_select_collector_classes):
    mock_platform.system.return_value = 'Linux'
    mock_timeout.DEFAULT_GATHER_TIMEOUT = 10
    mock_find_collectors_for_platform.return_value = ['collector1', 'collector2']
    mock_build_fact_id_to_collector_map.return_value = ({'subset1': 'collector1', 'subset2': 'collector2'}, {'alias1': 'subset1'})
    mock_get_collector_names.return_value = ['collector1', 'collector2']
    mock_solve_deps.return_value = ['collector1', 'collector2']
    mock_build_dep_data.return_value = {'collector1': [], 'collector2': []}
    mock_tsort.return_value = [('collector1', []), ('collector2', [])]
    mock_select_collector_classes.return_value = ['collector1_class', 'collector2_class']

    result = collector_classes_from_gather_subset(
        all_collector_classes=['collector1', 'collector2'],
        valid_subsets={'subset1', 'subset2'},
        minimal_gather_subset={'subset1'},
        gather_subset={'subset1', 'subset2'},
        gather_timeout=5,
        platform_info=None  # Set to None to trigger the default platform_info
    )

    assert result == ['collector1_class', 'collector2_class']
    mock_platform.system.assert_called_once()
    assert mock_timeout.GATHER_TIMEOUT == 5
    mock_find_collectors_for_platform.assert_called_once_with(['collector1', 'collector2'], [{'system': 'Linux'}, {'system': 'Generic'}])
    mock_build_fact_id_to_collector_map.assert_called_once_with(['collector1', 'collector2'])
    mock_get_collector_names.assert_called_once_with(valid_subsets={'subset1', 'subset2'},
                                                     minimal_gather_subset={'subset1'},
                                                     gather_subset={'subset1', 'subset2'},
                                                     aliases_map={'alias1': 'subset1'},
                                                     platform_info={'system': 'Linux'})
    mock_solve_deps.assert_called_once_with(['collector1', 'collector2'], {'subset1': 'collector1', 'subset2': 'collector2'})
    mock_build_dep_data.assert_called_once_with(['collector1', 'collector2'], {'subset1': 'collector1', 'subset2': 'collector2'})
    mock_tsort.assert_called_once_with({'collector1': [], 'collector2': []})
    mock_select_collector_classes.assert_called_once_with(['collector1', 'collector2'], {'subset1': 'collector1', 'subset2': 'collector2'})
