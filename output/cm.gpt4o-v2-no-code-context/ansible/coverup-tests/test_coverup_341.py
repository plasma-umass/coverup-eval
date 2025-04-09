# file: lib/ansible/plugins/lookup/random_choice.py:42-53
# asked: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}
# gained: {"lines": [42, 44, 46, 47, 48, 49, 50, 51, 53], "branches": [[47, 48], [47, 53]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.random_choice import LookupModule
import random

def test_run_with_terms(monkeypatch):
    terms = ['a', 'b', 'c']
    lookup = LookupModule()

    def mock_choice(seq):
        return 'a'

    monkeypatch.setattr(random, 'choice', mock_choice)
    result = lookup.run(terms)
    assert result == ['a']

def test_run_with_empty_terms():
    terms = []
    lookup = LookupModule()
    result = lookup.run(terms)
    assert result == []

def test_run_with_exception(monkeypatch):
    terms = ['a', 'b', 'c']
    lookup = LookupModule()

    def mock_choice(seq):
        raise ValueError("mocked error")

    monkeypatch.setattr(random, 'choice', mock_choice)
    with pytest.raises(AnsibleError, match="Unable to choose random term: mocked error"):
        lookup.run(terms)
