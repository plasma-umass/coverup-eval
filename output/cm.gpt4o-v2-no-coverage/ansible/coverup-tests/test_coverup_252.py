# file: lib/ansible/vars/manager.py:54-72
# asked: {"lines": [54, 61, 62, 63, 64, 66, 68, 69, 70, 72], "branches": [[61, 62], [61, 63], [63, 64], [63, 66], [68, 69], [68, 72], [69, 68], [69, 70]]}
# gained: {"lines": [54, 61, 62, 63, 64, 66, 68, 69, 70, 72], "branches": [[61, 62], [61, 63], [63, 64], [63, 66], [68, 69], [68, 72], [69, 68], [69, 70]]}

import pytest
from ansible.errors import AnsibleError
from ansible.module_utils.common._collections_compat import MutableMapping
from ansible.vars.manager import preprocess_vars

class MockMutableMapping(MutableMapping):
    def __init__(self, *args, **kwargs):
        self.store = dict(*args, **kwargs)

    def __getitem__(self, key):
        return self.store[key]

    def __setitem__(self, key, value):
        self.store[key] = value

    def __delitem__(self, key):
        del self.store[key]

    def __iter__(self):
        return iter(self.store)

    def __len__(self):
        return len(self.store)

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
    with pytest.raises(AnsibleError, match="variable files must contain either a dictionary of variables, or a list of dictionaries. Got:"):
        preprocess_vars([1, 2, 3])

def test_preprocess_vars_valid_mutable_mapping():
    mock_mapping = MockMutableMapping(key='value')
    result = preprocess_vars(mock_mapping)
    assert isinstance(result, list)
    assert len(result) == 1
    assert result[0] == mock_mapping

def test_preprocess_vars_list_with_valid_mutable_mapping():
    mock_mapping1 = MockMutableMapping(key1='value1')
    mock_mapping2 = MockMutableMapping(key2='value2')
    result = preprocess_vars([mock_mapping1, mock_mapping2])
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0] == mock_mapping1
    assert result[1] == mock_mapping2
