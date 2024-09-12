# file: lib/ansible/vars/manager.py:54-72
# asked: {"lines": [54, 61, 62, 63, 64, 66, 68, 69, 70, 72], "branches": [[61, 62], [61, 63], [63, 64], [63, 66], [68, 69], [68, 72], [69, 68], [69, 70]]}
# gained: {"lines": [54, 61, 62, 63, 64, 66, 68, 69, 70, 72], "branches": [[61, 62], [61, 63], [63, 64], [63, 66], [68, 69], [68, 72], [69, 68], [69, 70]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.vars.manager import preprocess_vars

def test_preprocess_vars_none():
    assert preprocess_vars(None) is None

def test_preprocess_vars_not_list():
    result = preprocess_vars({'key': 'value'})
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == {'key': 'value'}

def test_preprocess_vars_list():
    result = preprocess_vars([{'key1': 'value1'}, {'key2': 'value2'}])
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == {'key1': 'value1'}
    assert result[1] == {'key2': 'value2'}

def test_preprocess_vars_invalid_type():
    with pytest.raises(AnsibleError, match=r"variable files must contain either a dictionary of variables, or a list of dictionaries. Got: .*"):
        preprocess_vars([{'key': 'value'}, 'invalid'])

def test_preprocess_vars_invalid_single_type():
    with pytest.raises(AnsibleError, match=r"variable files must contain either a dictionary of variables, or a list of dictionaries. Got: .*"):
        preprocess_vars('invalid')
