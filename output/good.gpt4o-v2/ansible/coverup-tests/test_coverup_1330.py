# file: lib/ansible/module_utils/facts/collector.py:120-196
# asked: {"lines": [133, 136, 139, 141, 144, 145, 151, 152, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 177, 179, 180, 184, 185, 186, 188, 189, 191, 192, 194, 196], "branches": [[157, 158], [157, 191], [159, 160], [159, 162], [162, 163], [162, 165], [165, 166], [165, 175], [167, 168], [167, 170], [170, 171], [170, 173], [177, 179], [177, 184], [184, 185], [184, 188], [191, 192], [191, 194]]}
# gained: {"lines": [133, 136, 139, 141, 144, 145, 151, 152, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 177, 179, 180, 184, 185, 186, 188, 189, 191, 192, 194, 196], "branches": [[157, 158], [157, 191], [159, 160], [159, 162], [162, 163], [162, 165], [165, 166], [165, 175], [167, 168], [167, 170], [170, 171], [170, 173], [177, 179], [177, 184], [184, 185], [184, 188], [191, 192], [191, 194]]}

import pytest
from collections import defaultdict
from ansible.module_utils.facts.collector import get_collector_names

def test_get_collector_names_default():
    result = get_collector_names()
    assert result == set()

def test_get_collector_names_with_valid_subsets():
    valid_subsets = frozenset(['all', 'network'])
    result = get_collector_names(valid_subsets=valid_subsets)
    assert result == valid_subsets

def test_get_collector_names_with_minimal_gather_subset():
    minimal_gather_subset = frozenset(['min'])
    result = get_collector_names(minimal_gather_subset=minimal_gather_subset)
    assert result == minimal_gather_subset

def test_get_collector_names_with_gather_subset():
    gather_subset = ['network']
    valid_subsets = frozenset(['network'])
    result = get_collector_names(gather_subset=gather_subset, valid_subsets=valid_subsets)
    assert result == set(gather_subset)

def test_get_collector_names_with_aliases_map():
    aliases_map = defaultdict(set, {'hardware': {'devices', 'dmi'}})
    gather_subset = ['!hardware']
    result = get_collector_names(gather_subset=gather_subset, aliases_map=aliases_map)
    assert result == set()

def test_get_collector_names_with_exclude_min():
    gather_subset = ['!min']
    minimal_gather_subset = frozenset(['min'])
    result = get_collector_names(gather_subset=gather_subset, minimal_gather_subset=minimal_gather_subset)
    assert result == set()

def test_get_collector_names_with_exclude_all():
    gather_subset = ['!all']
    valid_subsets = frozenset(['all', 'network'])
    minimal_gather_subset = frozenset(['min'])
    result = get_collector_names(gather_subset=gather_subset, valid_subsets=valid_subsets, minimal_gather_subset=minimal_gather_subset)
    assert result == minimal_gather_subset

def test_get_collector_names_with_invalid_subset():
    gather_subset = ['invalid']
    valid_subsets = frozenset(['all', 'network'])
    with pytest.raises(TypeError, match="Bad subset 'invalid' given to Ansible. gather_subset options allowed: all, all, network"):
        get_collector_names(gather_subset=gather_subset, valid_subsets=valid_subsets)
