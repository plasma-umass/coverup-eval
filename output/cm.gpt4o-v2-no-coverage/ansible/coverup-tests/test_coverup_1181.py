# file: lib/ansible/plugins/filter/core.py:489-532
# asked: {"lines": [499, 506, 524, 525], "branches": [[498, 499], [505, 506]]}
# gained: {"lines": [499], "branches": [[498, 499]]}

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.module_utils.six import string_types
from ansible.plugins.filter.core import subelements

def test_subelements_dict():
    obj = {"item1": {"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}}
    result = subelements(obj, 'groups')
    assert result == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]

def test_subelements_list():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    result = subelements(obj, 'groups')
    assert result == [({'name': 'alice', 'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}, 'wheel')]

def test_subelements_invalid_obj():
    with pytest.raises(AnsibleFilterError, match="obj must be a list of dicts or a nested dict"):
        subelements("invalid_obj", 'groups')

def test_subelements_invalid_subelements():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    with pytest.raises(AnsibleFilterTypeError, match="subelements must be a list or a string"):
        subelements(obj, 123)

def test_subelements_key_error_skip_missing():
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

def test_subelements_nested_dict():
    obj = [{"name": "alice", "details": {"groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}}]
    result = subelements(obj, 'details.groups')
    assert result == [({'name': 'alice', 'details': {'groups': ['wheel'], 'authorized': ['/tmp/alice/onekey.pub']}}, 'wheel')]

def test_subelements_type_error_nested():
    obj = [{"name": "alice", "details": {"groups": "wheel", "authorized": ["/tmp/alice/onekey.pub"]}}]
    with pytest.raises(AnsibleFilterTypeError, match="the key 'groups' should point to a list, got 'wheel'"):
        subelements(obj, 'details.groups')
