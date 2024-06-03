# file lib/ansible/plugins/filter/core.py:489-532
# lines [499, 506, 524, 525]
# branches ['498->499', '505->506']

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.plugins.filter.core import subelements

def test_subelements_dict():
    obj = {"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}
    result = subelements([obj], 'groups')
    assert result == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]

def test_subelements_list_of_dicts():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    result = subelements(obj, 'groups')
    assert result == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]

def test_subelements_list_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    result = subelements(obj, ['groups'])
    assert result == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]

def test_subelements_skip_missing():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    result = subelements(obj, 'nonexistent', skip_missing=True)
    assert result == []

def test_subelements_key_error():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    with pytest.raises(AnsibleFilterError, match="could not find 'nonexistent' key in iterated item"):
        subelements(obj, 'nonexistent')

def test_subelements_type_error():
    obj = [{"name": "alice", "groups": "wheel", "authorized": ["/tmp/alice/onekey.pub"]}]
    with pytest.raises(AnsibleFilterTypeError, match="the key 'groups' should point to a list, got 'wheel'"):
        subelements(obj, 'groups')

def test_subelements_nested_type_error():
    obj = [{"name": "alice", "groups": {"nested": "wheel"}, "authorized": ["/tmp/alice/onekey.pub"]}]
    with pytest.raises(AnsibleFilterTypeError, match="the key 'nested' should point to a list, got 'wheel'"):
        subelements(obj, 'groups.nested')
