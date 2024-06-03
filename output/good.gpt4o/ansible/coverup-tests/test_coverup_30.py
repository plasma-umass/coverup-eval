# file lib/ansible/plugins/filter/mathstuff.py:199-246
# lines [199, 208, 209, 211, 214, 216, 217, 218, 219, 221, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 238, 239, 240, 241, 242, 244, 246]
# branches ['208->209', '208->211', '216->217', '216->218', '218->219', '218->221', '223->224', '223->246', '224->225', '224->227', '238->239', '238->244', '239->240', '239->241', '241->223', '241->242']

import pytest
from ansible.plugins.filter.mathstuff import rekey_on_member
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from collections.abc import Mapping, Iterable
from ansible.module_utils._text import to_native, text_type, binary_type

def test_rekey_on_member_invalid_duplicates():
    with pytest.raises(AnsibleFilterError, match="duplicates parameter to rekey_on_member has unknown value: invalid"):
        rekey_on_member([{'a': 1}], 'a', duplicates='invalid')

def test_rekey_on_member_invalid_data_type():
    with pytest.raises(AnsibleFilterTypeError, match="Type is not a valid list, set, or dict"):
        rekey_on_member("invalid_data", 'a')

def test_rekey_on_member_list_item_not_dict():
    with pytest.raises(AnsibleFilterTypeError, match="List item is not a valid dict"):
        rekey_on_member([1, 2, 3], 'a')

def test_rekey_on_member_key_not_found():
    with pytest.raises(AnsibleFilterError, match="Key b was not found"):
        rekey_on_member([{'a': 1}], 'b')

def test_rekey_on_member_key_not_unique_error():
    with pytest.raises(AnsibleFilterError, match="Key 1 is not unique, cannot correctly turn into dict"):
        rekey_on_member([{'a': 1}, {'a': 1}], 'a', duplicates='error')

def test_rekey_on_member_key_not_unique_overwrite():
    result = rekey_on_member([{'a': 1, 'b': 2}, {'a': 1, 'b': 3}], 'a', duplicates='overwrite')
    assert result == {1: {'a': 1, 'b': 3}}

def test_rekey_on_member_success():
    result = rekey_on_member([{'a': 1, 'b': 2}, {'a': 2, 'b': 3}], 'a')
    assert result == {1: {'a': 1, 'b': 2}, 2: {'a': 2, 'b': 3}}
