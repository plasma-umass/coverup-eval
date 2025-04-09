# file lib/ansible/module_utils/facts/collector.py:345-400
# lines [345, 346, 347, 348, 349, 350, 355, 357, 359, 361, 364, 366, 370, 372, 374, 379, 381, 384, 385, 386, 387, 388, 390, 392, 394, 395, 397, 398, 400]
# branches []

import pytest
from ansible.module_utils.facts.collector import collector_classes_from_gather_subset
from ansible.module_utils.facts.timeout import DEFAULT_GATHER_TIMEOUT
from collections import defaultdict
import platform

# Mocks for the functions used within collector_classes_from_gather_subset
def mock_find_collectors_for_platform(all_collector_classes, compat_platforms):
    return all_collector_classes

def mock_build_fact_id_to_collector_map(collectors_for_platform):
    return ({'network': 'NetworkCollector', 'hardware': 'HardwareCollector'}, defaultdict(set))

def mock_get_collector_names(valid_subsets, minimal_gather_subset, gather_subset, aliases_map, platform_info):
    return gather_subset

def mock__solve_deps(collector_names, all_fact_subsets):
    return collector_names

def mock_build_dep_data(complete_collector_names, all_fact_subsets):
    return {name: set() for name in complete_collector_names}

def mock_tsort(dep_map):
    return [(name, set()) for name in dep_map]

def mock_select_collector_classes(ordered_collector_names, all_fact_subsets):
    return [all_fact_subsets[name] for name in ordered_collector_names]

@pytest.fixture
def mock_dependencies(mocker):
    mocker.patch('ansible.module_utils.facts.collector.find_collectors_for_platform', side_effect=mock_find_collectors_for_platform)
    mocker.patch('ansible.module_utils.facts.collector.build_fact_id_to_collector_map', side_effect=mock_build_fact_id_to_collector_map)
    mocker.patch('ansible.module_utils.facts.collector.get_collector_names', side_effect=mock_get_collector_names)
    mocker.patch('ansible.module_utils.facts.collector._solve_deps', side_effect=mock__solve_deps)
    mocker.patch('ansible.module_utils.facts.collector.build_dep_data', side_effect=mock_build_dep_data)
    mocker.patch('ansible.module_utils.facts.collector.tsort', side_effect=mock_tsort)
    mocker.patch('ansible.module_utils.facts.collector.select_collector_classes', side_effect=mock_select_collector_classes)

def test_collector_classes_from_gather_subset(mock_dependencies):
    all_collector_classes = ['NetworkCollector', 'HardwareCollector']
    valid_subsets = frozenset(['network', 'hardware'])
    minimal_gather_subset = frozenset(['network'])
    gather_subset = ['network']
    gather_timeout = 10
    platform_info = {'system': 'Linux'}

    # Call the function with the mocked dependencies
    selected_collector_classes = collector_classes_from_gather_subset(
        all_collector_classes=all_collector_classes,
        valid_subsets=valid_subsets,
        minimal_gather_subset=minimal_gather_subset,
        gather_subset=gather_subset,
        gather_timeout=gather_timeout,
        platform_info=platform_info
    )

    # Assertions to verify the postconditions
    assert selected_collector_classes == ['NetworkCollector']
    assert DEFAULT_GATHER_TIMEOUT == gather_timeout  # Verify that the timeout was set correctly
