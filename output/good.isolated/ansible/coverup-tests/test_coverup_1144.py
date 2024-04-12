# file lib/ansible/plugins/filter/mathstuff.py:199-246
# lines [208, 209, 211, 214, 216, 217, 218, 219, 221, 223, 224, 225, 227, 228, 229, 230, 231, 232, 233, 234, 238, 239, 240, 241, 242, 244, 246]
# branches ['208->209', '208->211', '216->217', '216->218', '218->219', '218->221', '223->224', '223->246', '224->225', '224->227', '238->239', '238->244', '239->240', '239->241', '241->223', '241->242']

import pytest
from ansible.errors import AnsibleFilterError, AnsibleFilterTypeError
from ansible.plugins.filter.mathstuff import rekey_on_member
from collections.abc import Mapping, Iterable
from ansible.module_utils._text import to_native
from ansible.module_utils.six import text_type, binary_type

def test_rekey_on_member():
    # Test with duplicates='error' and a duplicate key
    data = [{'id': 1, 'value': 'A'}, {'id': 1, 'value': 'B'}]
    key = 'id'
    with pytest.raises(AnsibleFilterError) as excinfo:
        rekey_on_member(data, key, duplicates='error')
    assert "Key 1 is not unique" in str(excinfo.value)

    # Test with duplicates='overwrite' and a duplicate key
    expected_result = {1: {'id': 1, 'value': 'B'}}
    result = rekey_on_member(data, key, duplicates='overwrite')
    assert result == expected_result

    # Test with an invalid duplicates parameter
    with pytest.raises(AnsibleFilterError) as excinfo:
        rekey_on_member(data, key, duplicates='invalid')
    assert "duplicates parameter to rekey_on_member has unknown value" in str(excinfo.value)

    # Test with a non-Mapping, non-Iterable data
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        rekey_on_member(None, key)
    assert "Type is not a valid list, set, or dict" in str(excinfo.value)

    # Test with a list item that is not a valid dict
    data = [1, 2, 3]
    with pytest.raises(AnsibleFilterTypeError) as excinfo:
        rekey_on_member(data, key)
    assert "List item is not a valid dict" in str(excinfo.value)

    # Test with a key not found in the list of dicts
    data = [{'id': 1, 'value': 'A'}, {'id': 2, 'value': 'B'}]
    key = 'nonexistent_key'
    with pytest.raises(AnsibleFilterError) as excinfo:
        rekey_on_member(data, key)
    assert "Key nonexistent_key was not found" in str(excinfo.value)
