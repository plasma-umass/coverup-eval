# file: lib/ansible/utils/vars.py:58-79
# asked: {"lines": [58, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[70, 0], [70, 71], [72, 73], [72, 77]]}
# gained: {"lines": [58, 70, 71, 72, 73, 74, 75, 76, 77, 78], "branches": [[70, 0], [70, 71], [72, 73], [72, 77]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils._text import to_native
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.utils.vars import _validate_mutable_mappings

def test_validate_mutable_mappings_with_valid_dicts():
    a = {'key1': 'value1'}
    b = {'key2': 'value2'}
    try:
        _validate_mutable_mappings(a, b)
    except AnsibleError:
        pytest.fail("AnsibleError raised unexpectedly with valid dicts")

def test_validate_mutable_mappings_with_invalid_first_argument():
    a = ['not', 'a', 'dict']
    b = {'key2': 'value2'}
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings(a, b)
    assert "failed to combine variables, expected dicts but got a 'list' and a 'dict'" in str(excinfo.value)

def test_validate_mutable_mappings_with_invalid_second_argument():
    a = {'key1': 'value1'}
    b = ['not', 'a', 'dict']
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings(a, b)
    assert "failed to combine variables, expected dicts but got a 'dict' and a 'list'" in str(excinfo.value)

def test_validate_mutable_mappings_with_both_invalid_arguments():
    a = ['not', 'a', 'dict']
    b = ['also', 'not', 'a', 'dict']
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings(a, b)
    assert "failed to combine variables, expected dicts but got a 'list' and a 'list'" in str(excinfo.value)

def test_validate_mutable_mappings_with_unserializable_object(mocker):
    class Unserializable:
        def __str__(self):
            return "Unserializable instance"
    
    a = Unserializable()
    b = {'key2': 'value2'}
    
    mocker.patch('ansible.utils.vars.dumps', side_effect=TypeError("Unserializable object"))
    
    with pytest.raises(AnsibleError) as excinfo:
        _validate_mutable_mappings(a, b)
    assert "failed to combine variables, expected dicts but got a 'Unserializable' and a 'dict'" in str(excinfo.value)
    assert "Unserializable instance" in str(excinfo.value)
