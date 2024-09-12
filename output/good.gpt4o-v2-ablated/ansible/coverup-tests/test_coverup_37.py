# file: lib/ansible/module_utils/facts/collector.py:345-400
# asked: {"lines": [345, 346, 347, 348, 349, 350, 355, 357, 359, 361, 364, 366, 370, 372, 374, 379, 381, 384, 385, 386, 387, 388, 390, 392, 394, 395, 397, 398, 400], "branches": []}
# gained: {"lines": [345, 346, 347, 348, 349, 350, 355, 357, 359, 361, 364, 366, 370, 372, 374, 379, 381, 384, 385, 386, 387, 388, 390, 392, 394, 395, 397, 398, 400], "branches": []}

import pytest
from unittest.mock import patch, MagicMock, create_autospec
from collections import defaultdict
import platform
from ansible.module_utils.facts.collector import collector_classes_from_gather_subset

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

def test_collector_classes_from_gather_subset_all_defaults(mock_timeout, mock_find_collectors_for_platform, 
                                                           mock_build_fact_id_to_collector_map, mock_get_collector_names, 
                                                           mock_solve_deps, mock_build_dep_data, mock_tsort, 
                                                           mock_select_collector_classes):
    mock_find_collectors_for_platform.return_value = []
    mock_build_fact_id_to_collector_map.return_value = ({}, defaultdict(set))
    mock_get_collector_names.return_value = set()
    mock_solve_deps.return_value = set()
    mock_build_dep_data.return_value = {}
    mock_tsort.return_value = []
    mock_select_collector_classes.return_value = []

    result = collector_classes_from_gather_subset()

    assert result == []
    mock_timeout.GATHER_TIMEOUT = mock_timeout.DEFAULT_GATHER_TIMEOUT

def test_collector_classes_from_gather_subset_with_params(mock_timeout, mock_find_collectors_for_platform, 
                                                          mock_build_fact_id_to_collector_map, mock_get_collector_names, 
                                                          mock_solve_deps, mock_build_dep_data, mock_tsort, 
                                                          mock_select_collector_classes):
    all_collector_classes = [MagicMock()]
    valid_subsets = frozenset(['test_subset'])
    minimal_gather_subset = frozenset(['minimal'])
    gather_subset = frozenset(['gather'])
    gather_timeout = 10
    platform_info = {'system': 'Linux'}

    mock_find_collectors_for_platform.return_value = all_collector_classes
    mock_build_fact_id_to_collector_map.return_value = ({'test_subset': MagicMock()}, defaultdict(set))
    mock_get_collector_names.return_value = {'test_subset'}
    mock_solve_deps.return_value = {'test_subset'}
    mock_build_dep_data.return_value = {'test_subset': []}
    mock_tsort.return_value = [('test_subset', [])]
    mock_select_collector_classes.return_value = [MagicMock()]

    result = collector_classes_from_gather_subset(all_collector_classes, valid_subsets, minimal_gather_subset, 
                                                  gather_subset, gather_timeout, platform_info)

    assert len(result) == 1
    assert mock_timeout.GATHER_TIMEOUT == gather_timeout
