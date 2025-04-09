# file: lib/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule

def test_run_with_terms(monkeypatch):
    def mock_choice(seq):
        return seq[0]
    
    monkeypatch.setattr('random.choice', mock_choice)
    
    lookup = LookupModule()
    terms = ['a', 'b', 'c']
    result = lookup.run(terms)
    
    assert result == ['a']

def test_run_without_terms():
    lookup = LookupModule()
    terms = []
    result = lookup.run(terms)
    
    assert result == []

def test_run_with_exception(monkeypatch):
    def mock_choice(seq):
        raise Exception("Test exception")
    
    monkeypatch.setattr('random.choice', mock_choice)
    
    lookup = LookupModule()
    terms = ['a', 'b', 'c']
    
    with pytest.raises(AnsibleError, match="Unable to choose random term: Test exception"):
        lookup.run(terms)
