# file: lib/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule
import random

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_run_with_terms(lookup_module, monkeypatch):
    terms = ['a', 'b', 'c']
    
    def mock_choice(seq):
        return 'a'
    
    monkeypatch.setattr(random, 'choice', mock_choice)
    result = lookup_module.run(terms)
    assert result == ['a']

def test_run_with_empty_terms(lookup_module):
    terms = []
    result = lookup_module.run(terms)
    assert result == []

def test_run_with_exception(lookup_module, monkeypatch):
    terms = ['a', 'b', 'c']
    
    def mock_choice(seq):
        raise ValueError("mocked error")
    
    monkeypatch.setattr(random, 'choice', mock_choice)
    
    with pytest.raises(AnsibleError) as excinfo:
        lookup_module.run(terms)
    
    assert "Unable to choose random term: mocked error" in str(excinfo.value)
