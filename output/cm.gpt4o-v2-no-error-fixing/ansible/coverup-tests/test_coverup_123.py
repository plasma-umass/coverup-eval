# file: lib/ansible/vars/manager.py:54-72
# asked: {"lines": [54, 61, 62, 63, 64, 66, 68, 69, 70, 72], "branches": [[61, 62], [61, 63], [63, 64], [63, 66], [68, 69], [68, 72], [69, 68], [69, 70]]}
# gained: {"lines": [54, 61, 62, 63, 64, 66, 68, 69, 70, 72], "branches": [[61, 62], [61, 63], [63, 64], [63, 66], [68, 69], [68, 72], [69, 68], [69, 70]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.vars.manager import preprocess_vars

def test_preprocess_vars_none():
    assert preprocess_vars(None) is None

def test_preprocess_vars_not_list(mocker):
    mocker.patch('ansible.vars.manager.MutableMapping', dict)
    assert preprocess_vars({'key': 'value'}) == [{'key': 'value'}]

def test_preprocess_vars_list(mocker):
    mocker.patch('ansible.vars.manager.MutableMapping', dict)
    assert preprocess_vars([{'key': 'value'}]) == [{'key': 'value'}]

def test_preprocess_vars_invalid_type():
    with pytest.raises(AnsibleError, match="variable files must contain either a dictionary of variables, or a list of dictionaries. Got: .*"):
        preprocess_vars([1, 2, 3])
