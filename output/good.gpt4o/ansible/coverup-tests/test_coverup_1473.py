# file lib/ansible/module_utils/common/parameters.py:503-538
# lines [528]
# branches ['525->528']

import pytest
from ansible.module_utils.common.parameters import _sanitize_keys_conditions
from collections.abc import Mapping

class ImmutableMapping(Mapping):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)

def test_sanitize_keys_conditions_immutable_mapping():
    value = ImmutableMapping({"key1": "value1", "key2": "value2"})
    no_log_strings = []
    ignore_keys = []
    deferred_removals = []

    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)

    assert result == {}
    assert deferred_removals == [(value, {})]

@pytest.fixture(autouse=True)
def cleanup():
    yield
    # Add any necessary cleanup code here
