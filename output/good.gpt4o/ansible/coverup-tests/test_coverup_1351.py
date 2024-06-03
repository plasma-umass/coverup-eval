# file lib/ansible/module_utils/common/json.py:26-39
# lines []
# branches ['36->39']

import pytest
from ansible.module_utils.common.json import _preprocess_unsafe_encode
from collections.abc import Mapping

class CustomMapping(Mapping):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

def test_preprocess_unsafe_encode_with_mapping():
    # Create a custom mapping object
    custom_mapping = CustomMapping({'key1': 'value1', 'key2': 'value2'})

    # Call the function with the custom mapping
    result = _preprocess_unsafe_encode(custom_mapping)

    # Verify the result is a dictionary with the same items
    assert isinstance(result, dict)
    assert result == {'key1': 'value1', 'key2': 'value2'}
