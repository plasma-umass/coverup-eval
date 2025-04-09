# file: lib/ansible/module_utils/common/parameters.py:503-538
# asked: {"lines": [505, 506, 508, 509, 510, 512, 513, 514, 516, 517, 518, 520, 521, 522, 524, 525, 526, 528, 529, 530, 532, 533, 535, 536, 538], "branches": [[505, 506], [505, 508], [508, 509], [508, 516], [509, 510], [509, 512], [516, 517], [516, 524], [517, 518], [517, 520], [524, 525], [524, 532], [525, 526], [525, 528], [532, 533], [532, 535], [535, 536], [535, 538]]}
# gained: {"lines": [505, 506, 508, 509, 510, 512, 513, 514, 516, 517, 518, 520, 521, 522, 524, 525, 526, 529, 530, 532, 533, 535, 536, 538], "branches": [[505, 506], [505, 508], [508, 509], [508, 516], [509, 510], [509, 512], [516, 517], [516, 524], [517, 518], [517, 520], [524, 525], [524, 532], [525, 526], [532, 533], [532, 535], [535, 536], [535, 538]]}

import pytest
from ansible.module_utils.common.parameters import _sanitize_keys_conditions
from ansible.module_utils.six import text_type, binary_type
from collections.abc import MutableSequence, MutableSet, MutableMapping
import datetime

def test_sanitize_keys_conditions_text_type():
    value = text_type("test")
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == value
    assert deferred_removals == []

def test_sanitize_keys_conditions_binary_type():
    value = binary_type(b"test")
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert result == value
    assert deferred_removals == []

def test_sanitize_keys_conditions_mutable_sequence():
    class CustomMutableSequence(MutableSequence):
        def __init__(self, *args):
            self._data = list(args)
        def __getitem__(self, index):
            return self._data[index]
        def __setitem__(self, index, value):
            self._data[index] = value
        def __delitem__(self, index):
            del self._data[index]
        def __len__(self):
            return len(self._data)
        def insert(self, index, value):
            self._data.insert(index, value)
    
    value = CustomMutableSequence(1, 2, 3)
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert isinstance(result, CustomMutableSequence)
    assert deferred_removals == [(value, result)]

def test_sanitize_keys_conditions_immutable_sequence():
    value = (1, 2, 3)
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert isinstance(result, list)
    assert deferred_removals == [(value, result)]

def test_sanitize_keys_conditions_mutable_set():
    class CustomMutableSet(MutableSet):
        def __init__(self, *args):
            self._data = set(args)
        def __contains__(self, value):
            return value in self._data
        def __iter__(self):
            return iter(self._data)
        def __len__(self):
            return len(self._data)
        def add(self, value):
            self._data.add(value)
        def discard(self, value):
            self._data.discard(value)
    
    value = CustomMutableSet(1, 2, 3)
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert isinstance(result, CustomMutableSet)
    assert deferred_removals == [(value, result)]

def test_sanitize_keys_conditions_immutable_set():
    value = frozenset([1, 2, 3])
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert isinstance(result, set)
    assert deferred_removals == [(value, result)]

def test_sanitize_keys_conditions_mutable_mapping():
    class CustomMutableMapping(MutableMapping):
        def __init__(self, *args, **kwargs):
            self._data = dict(*args, **kwargs)
        def __getitem__(self, key):
            return self._data[key]
        def __setitem__(self, key, value):
            self._data[key] = value
        def __delitem__(self, key):
            del self._data[key]
        def __iter__(self):
            return iter(self._data)
        def __len__(self):
            return len(self._data)
    
    value = CustomMutableMapping(a=1, b=2, c=3)
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert isinstance(result, CustomMutableMapping)
    assert deferred_removals == [(value, result)]

def test_sanitize_keys_conditions_immutable_mapping():
    value = {'a': 1, 'b': 2, 'c': 3}
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = []
    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert isinstance(result, dict)
    assert deferred_removals == [(value, result)]

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
    with pytest.raises(TypeError, match="Value of unknown type:"):
        _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
