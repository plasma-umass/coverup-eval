# file: lib/ansible/module_utils/common/parameters.py:503-538
# asked: {"lines": [503, 505, 506, 508, 509, 510, 512, 513, 514, 516, 517, 518, 520, 521, 522, 524, 525, 526, 528, 529, 530, 532, 533, 535, 536, 538], "branches": [[505, 506], [505, 508], [508, 509], [508, 516], [509, 510], [509, 512], [516, 517], [516, 524], [517, 518], [517, 520], [524, 525], [524, 532], [525, 526], [525, 528], [532, 533], [532, 535], [535, 536], [535, 538]]}
# gained: {"lines": [503, 505, 506, 508, 509, 510, 512, 513, 514, 516, 517, 518, 520, 521, 522, 524, 525, 526, 528, 529, 530, 532, 533, 535, 536, 538], "branches": [[505, 506], [505, 508], [508, 509], [508, 516], [509, 510], [509, 512], [516, 517], [516, 524], [517, 518], [517, 520], [524, 525], [524, 532], [525, 526], [525, 528], [532, 533], [532, 535], [535, 536], [535, 538]]}

import pytest
from collections import deque
from ansible.module_utils.common.parameters import _sanitize_keys_conditions
from ansible.module_utils.six import text_type, binary_type
from ansible.module_utils.common._collections_compat import Set, Sequence, Mapping, MutableMapping, MutableSet, MutableSequence
import datetime

def test_sanitize_keys_conditions_string():
    value = "test_string"
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == value
    assert deferred_removals == []

def test_sanitize_keys_conditions_binary():
    value = b"test_binary"
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == value
    assert deferred_removals == []

def test_sanitize_keys_conditions_mutable_sequence():
    value = [1, 2, 3]
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == []
    assert deferred_removals == [(value, [])]

def test_sanitize_keys_conditions_immutable_sequence():
    value = (1, 2, 3)
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == []
    assert deferred_removals == [(value, [])]

def test_sanitize_keys_conditions_mutable_set():
    value = {1, 2, 3}
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == set()
    assert deferred_removals == [(value, set())]

def test_sanitize_keys_conditions_immutable_set():
    value = frozenset([1, 2, 3])
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == set()
    assert deferred_removals == [(value, set())]

def test_sanitize_keys_conditions_mutable_mapping():
    value = {"key": "value"}
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == {}
    assert deferred_removals == [(value, {})]

def test_sanitize_keys_conditions_immutable_mapping():
    class ImmutableMapping(Mapping):
        def __init__(self, *args, **kwargs):
            self._data = dict(*args, **kwargs)
        def __getitem__(self, key):
            return self._data[key]
        def __iter__(self):
            return iter(self._data)
        def __len__(self):
            return len(self._data)
    value = ImmutableMapping(key="value")
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == {}
    assert deferred_removals == [(value, {})]

def test_sanitize_keys_conditions_integer():
    value = 42
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == value
    assert deferred_removals == []

def test_sanitize_keys_conditions_float():
    value = 3.14
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == value
    assert deferred_removals == []

def test_sanitize_keys_conditions_bool():
    value = True
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == value
    assert deferred_removals == []

def test_sanitize_keys_conditions_none():
    value = None
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == value
    assert deferred_removals == []

def test_sanitize_keys_conditions_datetime():
    value = datetime.datetime.now()
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == value
    assert deferred_removals == []

def test_sanitize_keys_conditions_date():
    value = datetime.date.today()
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == value
    assert deferred_removals == []

def test_sanitize_keys_conditions_unknown_type():
    class UnknownType:
        pass
    value = UnknownType()
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    with pytest.raises(TypeError):
        _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
