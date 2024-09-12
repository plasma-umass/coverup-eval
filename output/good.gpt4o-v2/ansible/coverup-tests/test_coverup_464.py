# file: lib/ansible/utils/vars.py:82-94
# asked: {"lines": [82, 87, 88, 91, 92, 93, 94], "branches": [[87, 88], [87, 91]]}
# gained: {"lines": [82, 87, 88, 91, 92, 93, 94], "branches": [[87, 88], [87, 91]]}

import pytest
from ansible.utils.vars import combine_vars
from ansible import constants as C
from ansible.errors import AnsibleError

def test_combine_vars_merge(monkeypatch):
    def mock_merge_hash(a, b, recursive=True, list_merge='replace'):
        return {'merged': True}

    monkeypatch.setattr('ansible.utils.vars.merge_hash', mock_merge_hash)
    C.DEFAULT_HASH_BEHAVIOUR = 'merge'
    a = {'key1': 'value1'}
    b = {'key2': 'value2'}
    result = combine_vars(a, b)
    assert result == {'merged': True}

def test_combine_vars_replace(monkeypatch):
    def mock_validate_mutable_mappings(a, b):
        pass

    monkeypatch.setattr('ansible.utils.vars._validate_mutable_mappings', mock_validate_mutable_mappings)
    C.DEFAULT_HASH_BEHAVIOUR = 'replace'
    a = {'key1': 'value1'}
    b = {'key2': 'value2'}
    result = combine_vars(a, b)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_combine_vars_invalid_merge(monkeypatch):
    def mock_validate_mutable_mappings(a, b):
        pass

    monkeypatch.setattr('ansible.utils.vars._validate_mutable_mappings', mock_validate_mutable_mappings)
    a = {'key1': 'value1'}
    b = {'key2': 'value2'}
    result = combine_vars(a, b, merge=False)
    assert result == {'key1': 'value1', 'key2': 'value2'}

def test_combine_vars_invalid_types():
    a = {'key1': 'value1'}
    b = ['not', 'a', 'dict']
    with pytest.raises(AnsibleError):
        combine_vars(a, b)
