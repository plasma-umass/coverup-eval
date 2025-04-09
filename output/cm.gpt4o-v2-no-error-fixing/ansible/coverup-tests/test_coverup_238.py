# file: lib/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule

def test_run_with_empty_terms():
    lookup = LookupModule()
    result = lookup.run([])
    assert result == []

def test_run_with_non_empty_terms(monkeypatch):
    lookup = LookupModule()
    terms = ['a', 'b', 'c']

    def mock_choice(seq):
        return 'a'

    monkeypatch.setattr('random.choice', mock_choice)
    result = lookup.run(terms)
    assert result == ['a']

def test_run_with_exception(monkeypatch):
    lookup = LookupModule()
    terms = ['a', 'b', 'c']

    def mock_choice(seq):
        raise Exception("Test exception")

    monkeypatch.setattr('random.choice', mock_choice)
    with pytest.raises(AnsibleError, match="Unable to choose random term: Test exception"):
        lookup.run(terms)
