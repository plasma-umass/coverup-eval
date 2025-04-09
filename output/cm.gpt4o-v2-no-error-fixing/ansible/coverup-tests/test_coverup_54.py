# file: lib/ansible/plugins/lookup/sequence.py:245-269
# asked: {"lines": [245, 246, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 259, 260, 261, 262, 263, 264, 265, 266, 269], "branches": [[248, 249], [248, 269], [252, 253], [252, 259], [260, 248], [260, 261]]}
# gained: {"lines": [245, 246, 248, 249, 250, 251, 252, 253, 254, 255, 259, 260, 261, 262, 263, 264, 265, 266, 269], "branches": [[248, 249], [248, 269], [252, 253], [252, 259], [260, 261]]}

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.lookup.sequence import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

def test_run_with_valid_simple_args(lookup_module):
    terms = ["1-5"]
    variables = {}
    result = lookup_module.run(terms, variables)
    assert result == ['1', '2', '3', '4', '5']

def test_run_with_invalid_simple_args(lookup_module):
    terms = ["1-a"]
    variables = {}
    with pytest.raises(AnsibleError, match="can't parse end=a as integer"):
        lookup_module.run(terms, variables)

def test_run_with_valid_kv_args(lookup_module):
    terms = ["start=1 end=5 stride=1"]
    variables = {}
    result = lookup_module.run(terms, variables)
    assert result == ['1', '2', '3', '4', '5']

def test_run_with_invalid_kv_args(lookup_module):
    terms = ["start=1 end=a"]
    variables = {}
    with pytest.raises(AnsibleError, match="can't parse end=a as integer"):
        lookup_module.run(terms, variables)

def test_run_with_sanity_check_error(lookup_module):
    terms = ["start=1"]
    variables = {}
    with pytest.raises(AnsibleError, match="must specify count or end in with_sequence"):
        lookup_module.run(terms, variables)

def test_run_with_generate_sequence_error(lookup_module, monkeypatch):
    def mock_generate_sequence():
        raise ValueError("mock error")
    monkeypatch.setattr(lookup_module, "generate_sequence", mock_generate_sequence)
    terms = ["1-5"]
    variables = {}
    with pytest.raises(AnsibleError, match="unknown error generating sequence: mock error"):
        lookup_module.run(terms, variables)
