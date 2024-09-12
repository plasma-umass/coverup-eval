# file: lib/ansible/plugins/filter/core.py:489-532
# asked: {"lines": [489, 498, 499, 500, 501, 503, 505, 506, 507, 508, 510, 512, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 529, 530, 532], "branches": [[498, 499], [498, 500], [500, 501], [500, 503], [505, 506], [505, 507], [507, 508], [507, 510], [514, 515], [514, 532], [516, 517], [516, 526], [520, 521], [520, 523], [526, 527], [526, 529], [529, 514], [529, 530]]}
# gained: {"lines": [489, 498, 500, 501, 503, 505, 507, 508, 510, 512, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 526, 527, 529, 530, 532], "branches": [[498, 500], [500, 501], [500, 503], [505, 507], [507, 508], [507, 510], [514, 515], [514, 532], [516, 517], [516, 526], [520, 521], [520, 523], [526, 527], [526, 529], [529, 514], [529, 530]]}

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.module_utils.six import string_types
from ansible.plugins.filter.core import subelements

def test_subelements_dict():
    obj = {"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}
    result = subelements([obj], 'groups')
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

def test_subelements_key_error_no_skip():
    obj = [{"name": "alice", "groups": ["wheel"], "authorized": ["/tmp/alice/onekey.pub"]}]
    with pytest.raises(AnsibleFilterError, match="could not find 'nonexistent' key in iterated item"):
        subelements(obj, 'nonexistent')

def test_subelements_type_error():
    obj = [{"name": "alice", "groups": "wheel", "authorized": ["/tmp/alice/onekey.pub"]}]
    with pytest.raises(AnsibleFilterTypeError, match="the key 'groups' should point to a list, got 'wheel'"):
        subelements(obj, 'groups')

def test_subelements_nested_key_error():
    obj = [{"name": "alice", "details": {"groups": ["wheel"]}, "authorized": ["/tmp/alice/onekey.pub"]}]
    with pytest.raises(AnsibleFilterError, match="could not find 'nonexistent' key in iterated item"):
        subelements(obj, 'details.nonexistent')

def test_subelements_nested_type_error():
    obj = [{"name": "alice", "details": {"groups": "wheel"}, "authorized": ["/tmp/alice/onekey.pub"]}]
    with pytest.raises(AnsibleFilterTypeError, match="the key 'groups' should point to a list, got 'wheel'"):
        subelements(obj, 'details.groups')
