# file: lib/ansible/plugins/filter/mathstuff.py:199-246
# asked: {"lines": [199, 208, 209, 211, 214, 216, 217, 218, 219, 221, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 238, 239, 240, 241, 242, 244, 246], "branches": [[208, 209], [208, 211], [216, 217], [216, 218], [218, 219], [218, 221], [223, 224], [223, 246], [224, 225], [224, 227], [238, 239], [238, 244], [239, 240], [239, 241], [241, 223], [241, 242]]}
# gained: {"lines": [199, 208, 209, 211, 214, 216, 217, 218, 219, 221, 223, 224, 225, 227, 228, 229, 230, 238, 239, 240, 241, 242, 244, 246], "branches": [[208, 209], [208, 211], [216, 217], [216, 218], [218, 219], [218, 221], [223, 224], [223, 246], [224, 225], [224, 227], [238, 239], [238, 244], [239, 240], [239, 241], [241, 242]]}

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.plugins.filter.mathstuff import rekey_on_member

def test_rekey_on_member_dict():
    data = {
        'a': {'id': 1, 'value': 'foo'},
        'b': {'id': 2, 'value': 'bar'}
    }
    key = 'id'
    result = rekey_on_member(data, key)
    assert result == {1: {'id': 1, 'value': 'foo'}, 2: {'id': 2, 'value': 'bar'}}

def test_rekey_on_member_list():
    data = [
        {'id': 1, 'value': 'foo'},
        {'id': 2, 'value': 'bar'}
    ]
    key = 'id'
    result = rekey_on_member(data, key)
    assert result == {1: {'id': 1, 'value': 'foo'}, 2: {'id': 2, 'value': 'bar'}}

def test_rekey_on_member_duplicates_error():
    data = [
        {'id': 1, 'value': 'foo'},
        {'id': 1, 'value': 'bar'}
    ]
    key = 'id'
    with pytest.raises(AnsibleFilterError, match="Key 1 is not unique, cannot correctly turn into dict"):
        rekey_on_member(data, key, duplicates='error')

def test_rekey_on_member_duplicates_overwrite():
    data = [
        {'id': 1, 'value': 'foo'},
        {'id': 1, 'value': 'bar'}
    ]
    key = 'id'
    result = rekey_on_member(data, key, duplicates='overwrite')
    assert result == {1: {'id': 1, 'value': 'bar'}}

def test_rekey_on_member_invalid_duplicates():
    data = [
        {'id': 1, 'value': 'foo'}
    ]
    key = 'id'
    with pytest.raises(AnsibleFilterError, match="duplicates parameter to rekey_on_member has unknown value: invalid"):
        rekey_on_member(data, key, duplicates='invalid')

def test_rekey_on_member_key_not_found():
    data = [
        {'id': 1, 'value': 'foo'}
    ]
    key = 'nonexistent'
    with pytest.raises(AnsibleFilterError, match="Key nonexistent was not found"):
        rekey_on_member(data, key)

def test_rekey_on_member_invalid_data_type():
    data = "invalid"
    key = 'id'
    with pytest.raises(AnsibleFilterTypeError, match="Type is not a valid list, set, or dict"):
        rekey_on_member(data, key)

def test_rekey_on_member_invalid_item_type():
    data = [
        {'id': 1, 'value': 'foo'},
        'invalid'
    ]
    key = 'id'
    with pytest.raises(AnsibleFilterTypeError, match="List item is not a valid dict"):
        rekey_on_member(data, key)
