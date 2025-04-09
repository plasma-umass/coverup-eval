# file: lib/ansible/module_utils/facts/collector.py:297-305
# asked: {"lines": [298, 299, 300, 301, 302, 303, 304, 305], "branches": [[299, 300], [299, 305], [301, 302], [301, 304], [302, 301], [302, 303]]}
# gained: {"lines": [298, 299, 300, 301, 302, 303, 304, 305], "branches": [[299, 300], [299, 305], [301, 302], [301, 304], [302, 301], [302, 303]]}

import pytest
from collections import defaultdict

# Assuming the build_dep_data function is imported from the module
from ansible.module_utils.facts.collector import build_dep_data

def test_build_dep_data_empty():
    collector_names = []
    all_fact_subsets = {}
    result = build_dep_data(collector_names, all_fact_subsets)
    assert result == defaultdict(set)

def test_build_dep_data_single_collector(monkeypatch):
    class MockCollector:
        required_facts = ['fact1', 'fact2']

    collector_names = ['collector1']
    all_fact_subsets = {
        'collector1': [MockCollector()]
    }
    result = build_dep_data(collector_names, all_fact_subsets)
    assert result == {'collector1': {'fact1', 'fact2'}}

def test_build_dep_data_multiple_collectors(monkeypatch):
    class MockCollector1:
        required_facts = ['fact1', 'fact2']

    class MockCollector2:
        required_facts = ['fact3']

    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [MockCollector1()],
        'collector2': [MockCollector2()]
    }
    result = build_dep_data(collector_names, all_fact_subsets)
    assert result == {
        'collector1': {'fact1', 'fact2'},
        'collector2': {'fact3'}
    }

def test_build_dep_data_multiple_collectors_with_shared_facts(monkeypatch):
    class MockCollector1:
        required_facts = ['fact1', 'fact2']

    class MockCollector2:
        required_facts = ['fact2', 'fact3']

    collector_names = ['collector1', 'collector2']
    all_fact_subsets = {
        'collector1': [MockCollector1()],
        'collector2': [MockCollector2()]
    }
    result = build_dep_data(collector_names, all_fact_subsets)
    assert result == {
        'collector1': {'fact1', 'fact2'},
        'collector2': {'fact2', 'fact3'}
    }
