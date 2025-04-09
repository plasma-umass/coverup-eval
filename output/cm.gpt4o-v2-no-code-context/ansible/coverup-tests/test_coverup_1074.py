# file: lib/ansible/module_utils/common/parameters.py:503-538
# asked: {"lines": [528], "branches": [[525, 528]]}
# gained: {"lines": [528], "branches": [[525, 528]]}

import pytest
from collections.abc import Mapping
from ansible.module_utils.common.parameters import _sanitize_keys_conditions

def test_sanitize_keys_conditions_mapping():
    class CustomMapping(Mapping):
        def __init__(self, data):
            self._data = data

        def __getitem__(self, key):
            return self._data[key]

        def __iter__(self):
            return iter(self._data)

        def __len__(self):
            return len(self._data)

    value = CustomMapping({'key': 'value'})
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []

    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)

    assert result == {}
    assert deferred_removals == [(value, {})]
