# file lib/ansible/module_utils/facts/collector.py:120-196
# lines [120, 121, 122, 123, 124, 133, 136, 139, 141, 144, 145, 151, 152, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 175, 177, 179, 180, 184, 185, 186, 188, 189, 191, 192, 194, 196]
# branches ['157->158', '157->191', '159->160', '159->162', '162->163', '162->165', '165->166', '165->175', '167->168', '167->170', '170->171', '170->173', '177->179', '177->184', '184->185', '184->188', '191->192', '191->194']

import pytest
from collections import defaultdict
from ansible.module_utils.facts.collector import get_collector_names

def test_get_collector_names():
    valid_subsets = frozenset(['all', 'network', 'hardware'])
    minimal_gather_subset = frozenset(['min'])
    gather_subset = ['!all', 'network']
    aliases_map = defaultdict(set, {'hardware': {'devices', 'dmi'}})
    
    result = get_collector_names(valid_subsets=valid_subsets,
                                 minimal_gather_subset=minimal_gather_subset,
                                 gather_subset=gather_subset,
                                 aliases_map=aliases_map)
    
    assert result == {'network', 'min'}

def test_get_collector_names_invalid_subset():
    valid_subsets = frozenset(['all', 'network', 'hardware'])
    gather_subset = ['invalid_subset']
    
    with pytest.raises(TypeError, match="Bad subset 'invalid_subset' given to Ansible. gather_subset options allowed: all, all, hardware, network"):
        get_collector_names(valid_subsets=valid_subsets, gather_subset=gather_subset)

def test_get_collector_names_with_minimal_gather_subset():
    valid_subsets = frozenset(['all', 'network', 'hardware'])
    minimal_gather_subset = frozenset(['min'])
    gather_subset = ['!all']
    
    result = get_collector_names(valid_subsets=valid_subsets,
                                 minimal_gather_subset=minimal_gather_subset,
                                 gather_subset=gather_subset)
    
    assert result == {'min'}

def test_get_collector_names_with_aliases():
    valid_subsets = frozenset(['all', 'network', 'hardware'])
    gather_subset = ['!hardware']
    aliases_map = defaultdict(set, {'hardware': {'devices', 'dmi'}})
    
    result = get_collector_names(valid_subsets=valid_subsets,
                                 gather_subset=gather_subset,
                                 aliases_map=aliases_map)
    
    assert result == {'all', 'network'}

def test_get_collector_names_default_parameters():
    result = get_collector_names()
    
    assert result == set()
