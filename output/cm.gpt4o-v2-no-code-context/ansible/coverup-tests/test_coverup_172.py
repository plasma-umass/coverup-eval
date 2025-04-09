# file: lib/ansible/vars/manager.py:54-72
# asked: {"lines": [54, 61, 62, 63, 64, 66, 68, 69, 70, 72], "branches": [[61, 62], [61, 63], [63, 64], [63, 66], [68, 69], [68, 72], [69, 68], [69, 70]]}
# gained: {"lines": [54, 61, 62, 63, 64, 66, 68, 69, 70, 72], "branches": [[61, 62], [61, 63], [63, 64], [63, 66], [68, 69], [68, 72], [69, 68], [69, 70]]}

import pytest
from ansible.vars.manager import preprocess_vars
from ansible.errors import AnsibleError
from collections.abc import MutableMapping

def test_preprocess_vars_none():
    assert preprocess_vars(None) is None

def test_preprocess_vars_not_list(monkeypatch):
    class MockMutableMapping(dict, MutableMapping):
        pass

    mock_data = MockMutableMapping({"key": "value"})
    result = preprocess_vars(mock_data)
    assert isinstance(result, list)
    assert result == [mock_data]

def test_preprocess_vars_list_of_dicts(monkeypatch):
    class MockMutableMapping(dict, MutableMapping):
        pass

    mock_data = [MockMutableMapping({"key1": "value1"}), MockMutableMapping({"key2": "value2"})]
    result = preprocess_vars(mock_data)
    assert isinstance(result, list)
    assert result == mock_data

def test_preprocess_vars_invalid_type():
    with pytest.raises(AnsibleError, match="variable files must contain either a dictionary of variables, or a list of dictionaries. Got:"):
        preprocess_vars("invalid_string")

def test_preprocess_vars_list_with_invalid_type():
    with pytest.raises(AnsibleError, match="variable files must contain either a dictionary of variables, or a list of dictionaries. Got:"):
        preprocess_vars(["valid_dict", 123])
