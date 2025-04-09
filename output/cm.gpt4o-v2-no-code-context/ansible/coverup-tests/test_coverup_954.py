# file: lib/ansible/plugins/lookup/sequence.py:245-269
# asked: {"lines": [246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 259, 260, 261, 262, 263, 264, 265, 266, 269], "branches": [[248, 249], [248, 269], [252, 253], [252, 259], [260, 248], [260, 261]]}
# gained: {"lines": [246, 248, 249, 250, 251, 252, 253, 254, 256, 257, 259, 260, 261, 262, 263, 264, 265, 266, 269], "branches": [[248, 249], [248, 269], [252, 253], [260, 248], [260, 261]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

class MockLookupBase:
    def reset(self):
        pass

    def parse_simple_args(self, term):
        return False

    def parse_kv_args(self, kv):
        pass

    def sanity_check(self):
        pass

    def generate_sequence(self):
        return [1, 2, 3]

    @property
    def stride(self):
        return 1

@pytest.fixture
def lookup_module(monkeypatch):
    module = LookupModule()
    monkeypatch.setattr(module, 'reset', MockLookupBase().reset)
    monkeypatch.setattr(module, 'parse_simple_args', MockLookupBase().parse_simple_args)
    monkeypatch.setattr(module, 'parse_kv_args', MockLookupBase().parse_kv_args)
    monkeypatch.setattr(module, 'sanity_check', MockLookupBase().sanity_check)
    monkeypatch.setattr(module, 'generate_sequence', MockLookupBase().generate_sequence)
    monkeypatch.setattr(module, 'stride', MockLookupBase().stride, raising=False)
    return module

def test_run_with_valid_term(lookup_module):
    terms = ['valid_term']
    result = lookup_module.run(terms, {})
    assert result == [1, 2, 3]

def test_run_with_invalid_term(lookup_module, monkeypatch):
    def mock_parse_simple_args(term):
        raise Exception("mock exception")

    monkeypatch.setattr(lookup_module, 'parse_simple_args', mock_parse_simple_args)
    terms = ['invalid_term']
    with pytest.raises(AnsibleError, match="unknown error parsing with_sequence arguments: 'invalid_term'. Error was: mock exception"):
        lookup_module.run(terms, {})

def test_run_with_stride_zero(lookup_module, monkeypatch):
    monkeypatch.setattr(lookup_module, 'stride', 0, raising=False)
    terms = ['valid_term']
    result = lookup_module.run(terms, {})
    assert result == []

def test_run_with_generate_sequence_exception(lookup_module, monkeypatch):
    def mock_generate_sequence():
        raise Exception("mock generate sequence exception")

    monkeypatch.setattr(lookup_module, 'generate_sequence', mock_generate_sequence)
    terms = ['valid_term']
    with pytest.raises(AnsibleError, match="unknown error generating sequence: mock generate sequence exception"):
        lookup_module.run(terms, {})
