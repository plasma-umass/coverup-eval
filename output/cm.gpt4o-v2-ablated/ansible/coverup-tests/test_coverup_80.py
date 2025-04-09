# file: lib/ansible/vars/manager.py:54-72
# asked: {"lines": [54, 61, 62, 63, 64, 66, 68, 69, 70, 72], "branches": [[61, 62], [61, 63], [63, 64], [63, 66], [68, 69], [68, 72], [69, 68], [69, 70]]}
# gained: {"lines": [54, 61, 62, 63, 64, 66, 68, 69, 70, 72], "branches": [[61, 62], [61, 63], [63, 64], [63, 66], [68, 69], [68, 72], [69, 68], [69, 70]]}

import pytest
from ansible.errors import AnsibleError
from collections.abc import MutableMapping
from ansible.vars.manager import preprocess_vars

def test_preprocess_vars_none():
    assert preprocess_vars(None) is None

def test_preprocess_vars_not_list_not_dict():
    with pytest.raises(AnsibleError) as excinfo:
        preprocess_vars("string")
    assert "variable files must contain either a dictionary of variables, or a list of dictionaries" in str(excinfo.value)

def test_preprocess_vars_not_list_dict():
    result = preprocess_vars({"key": "value"})
    assert result == [{"key": "value"}]

def test_preprocess_vars_list_not_dict():
    with pytest.raises(AnsibleError) as excinfo:
        preprocess_vars(["string"])
    assert "variable files must contain either a dictionary of variables, or a list of dictionaries" in str(excinfo.value)

def test_preprocess_vars_list_dict():
    result = preprocess_vars([{"key": "value"}])
    assert result == [{"key": "value"}]

def test_preprocess_vars_list_mixed():
    with pytest.raises(AnsibleError) as excinfo:
        preprocess_vars([{"key": "value"}, "string"])
    assert "variable files must contain either a dictionary of variables, or a list of dictionaries" in str(excinfo.value)
