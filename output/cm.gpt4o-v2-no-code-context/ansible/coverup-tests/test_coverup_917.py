# file: lib/ansible/plugins/filter/mathstuff.py:199-246
# asked: {"lines": [208, 209, 211, 214, 216, 217, 218, 219, 221, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 238, 239, 240, 241, 242, 244, 246], "branches": [[208, 209], [208, 211], [216, 217], [216, 218], [218, 219], [218, 221], [223, 224], [223, 246], [224, 225], [224, 227], [238, 239], [238, 244], [239, 240], [239, 241], [241, 223], [241, 242]]}
# gained: {"lines": [208, 209, 211, 214, 216, 218, 219, 221, 223, 224, 225, 227, 228, 229, 230, 238, 239, 240, 241, 242, 244, 246], "branches": [[208, 209], [208, 211], [216, 218], [218, 219], [218, 221], [223, 224], [223, 246], [224, 225], [224, 227], [238, 239], [238, 244], [239, 240], [239, 241], [241, 242]]}

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.plugins.filter.mathstuff import rekey_on_member

def test_rekey_on_member_invalid_duplicates():
    with pytest.raises(AnsibleFilterError, match="duplicates parameter to rekey_on_member has unknown value: invalid"):
        rekey_on_member([], 'key', duplicates='invalid')

def test_rekey_on_member_non_iterable_data():
    with pytest.raises(AnsibleFilterTypeError, match="Type is not a valid list, set, or dict"):
        rekey_on_member(123, 'key')

def test_rekey_on_member_list_item_not_dict():
    with pytest.raises(AnsibleFilterTypeError, match="List item is not a valid dict"):
        rekey_on_member([1, 2, 3], 'key')

def test_rekey_on_member_key_not_found():
    with pytest.raises(AnsibleFilterError, match="Key missing_key was not found"):
        rekey_on_member([{'key1': 'value1'}], 'missing_key')

def test_rekey_on_member_key_type_error():
    with pytest.raises(AnsibleFilterError, match="Key None was not found"):
        rekey_on_member([{'key1': 'value1'}], None)

def test_rekey_on_member_key_not_unique_error():
    data = [{'key': 'value1'}, {'key': 'value1'}]
    with pytest.raises(AnsibleFilterError, match="Key value1 is not unique, cannot correctly turn into dict"):
        rekey_on_member(data, 'key', duplicates='error')

def test_rekey_on_member_key_not_unique_overwrite():
    data = [{'key': 'value1', 'data': 1}, {'key': 'value1', 'data': 2}]
    result = rekey_on_member(data, 'key', duplicates='overwrite')
    assert result == {'value1': {'key': 'value1', 'data': 2}}

def test_rekey_on_member_success():
    data = [{'key': 'value1', 'data': 1}, {'key': 'value2', 'data': 2}]
    result = rekey_on_member(data, 'key')
    assert result == {'value1': {'key': 'value1', 'data': 1}, 'value2': {'key': 'value2', 'data': 2}}
