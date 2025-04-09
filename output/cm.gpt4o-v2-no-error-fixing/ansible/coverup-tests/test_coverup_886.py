# file: lib/ansible/module_utils/facts/collector.py:266-280
# asked: {"lines": [272, 274, 275, 276, 277, 278, 280], "branches": [[274, 275], [274, 280], [276, 274], [276, 277], [277, 276], [277, 278]]}
# gained: {"lines": [272, 274, 275, 276, 277, 278, 280], "branches": [[274, 275], [274, 280], [276, 274], [276, 277], [277, 276], [277, 278]]}

import pytest
from ansible.module_utils.facts.collector import find_unresolved_requires, CollectorNotFoundError

class MockCollectorClass:
    def __init__(self, required_facts):
        self.required_facts = required_facts

def test_find_unresolved_requires(monkeypatch):
    def mock_get_requires_by_collector_name(collector_name, all_fact_subsets):
        if collector_name == "collector1":
            return {"fact1", "fact2"}
        elif collector_name == "collector2":
            return {"fact3"}
        return set()

    monkeypatch.setattr('ansible.module_utils.facts.collector._get_requires_by_collector_name', mock_get_requires_by_collector_name)

    collector_names = {"collector1", "collector2"}
    all_fact_subsets = {
        "collector1": [MockCollectorClass({"fact1", "fact2"})],
        "collector2": [MockCollectorClass({"fact3"})]
    }

    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert unresolved == {"fact1", "fact2", "fact3"}

def test_find_unresolved_requires_with_no_unresolved(monkeypatch):
    def mock_get_requires_by_collector_name(collector_name, all_fact_subsets):
        if collector_name == "collector1":
            return {"fact1"}
        elif collector_name == "collector2":
            return {"fact2"}
        return set()

    monkeypatch.setattr('ansible.module_utils.facts.collector._get_requires_by_collector_name', mock_get_requires_by_collector_name)

    collector_names = {"collector1", "collector2", "fact1", "fact2"}
    all_fact_subsets = {
        "collector1": [MockCollectorClass({"fact1"})],
        "collector2": [MockCollectorClass({"fact2"})]
    }

    unresolved = find_unresolved_requires(collector_names, all_fact_subsets)
    assert unresolved == set()

def test_find_unresolved_requires_with_collector_not_found(monkeypatch):
    def mock_get_requires_by_collector_name(collector_name, all_fact_subsets):
        raise CollectorNotFoundError(f'Fact collector "{collector_name}" not found')

    monkeypatch.setattr('ansible.module_utils.facts.collector._get_requires_by_collector_name', mock_get_requires_by_collector_name)

    collector_names = {"collector1"}
    all_fact_subsets = {}

    with pytest.raises(CollectorNotFoundError, match='Fact collector "collector1" not found'):
        find_unresolved_requires(collector_names, all_fact_subsets)
