# file: lib/ansible/module_utils/facts/collector.py:297-305
# asked: {"lines": [297, 298, 299, 300, 301, 302, 303, 304, 305], "branches": [[299, 300], [299, 305], [301, 302], [301, 304], [302, 301], [302, 303]]}
# gained: {"lines": [297, 298, 299, 300, 301, 302, 303, 304, 305], "branches": [[299, 300], [299, 305], [301, 302], [301, 304], [302, 301], [302, 303]]}

import pytest
from collections import defaultdict
from unittest.mock import MagicMock

# Assuming the build_dep_data function is defined in ansible/module_utils/facts/collector.py
from ansible.module_utils.facts.collector import build_dep_data

def test_build_dep_data(monkeypatch):
    # Mock data
    collector_names = ['collector1', 'collector2']
    collector1 = MagicMock()
    collector1.required_facts = ['fact1', 'fact2']
    collector2 = MagicMock()
    collector2.required_facts = ['fact3']
    
    all_fact_subsets = {
        'collector1': [collector1],
        'collector2': [collector2]
    }
    
    # Expected result
    expected_dep_map = {
        'collector1': {'fact1', 'fact2'},
        'collector2': {'fact3'}
    }
    
    # Run the function
    result = build_dep_data(collector_names, all_fact_subsets)
    
    # Assertions
    assert result == expected_dep_map

    # Clean up
    monkeypatch.undo()
