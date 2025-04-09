# file: lib/ansible/module_utils/common/parameters.py:503-538
# asked: {"lines": [503, 505, 506, 508, 509, 510, 512, 513, 514, 516, 517, 518, 520, 521, 522, 524, 525, 526, 528, 529, 530, 532, 533, 535, 536, 538], "branches": [[505, 506], [505, 508], [508, 509], [508, 516], [509, 510], [509, 512], [516, 517], [516, 524], [517, 518], [517, 520], [524, 525], [524, 532], [525, 526], [525, 528], [532, 533], [532, 535], [535, 536], [535, 538]]}
# gained: {"lines": [503, 505, 506, 508, 509, 510, 512, 513, 514, 516, 517, 518, 520, 521, 522, 524, 525, 526, 529, 530, 532, 533, 535, 536, 538], "branches": [[505, 506], [505, 508], [508, 509], [508, 516], [509, 510], [509, 512], [516, 517], [516, 524], [517, 518], [517, 520], [524, 525], [524, 532], [525, 526], [532, 533], [532, 535], [535, 536], [535, 538]]}

import pytest
from ansible.module_utils.common.parameters import _sanitize_keys_conditions
from collections.abc import MutableSequence, MutableSet, MutableMapping
from collections import UserList, UserDict, UserString
import datetime

def test_sanitize_keys_conditions_text_type():
    value = "test_string"
    result = _sanitize_keys_conditions(value, [], [], [])
    assert result == value

def test_sanitize_keys_conditions_binary_type():
    value = b"test_bytes"
    result = _sanitize_keys_conditions(value, [], [], [])
    assert result == value

def test_sanitize_keys_conditions_mutable_sequence():
    value = UserList([1, 2, 3])
    deferred_removals = []
    result = _sanitize_keys_conditions(value, [], [], deferred_removals)
    assert result == type(value)()
    assert deferred_removals == [(value, result)]

def test_sanitize_keys_conditions_immutable_sequence():
    value = (1, 2, 3)
    deferred_removals = []
    result = _sanitize_keys_conditions(value, [], [], deferred_removals)
    assert result == []
    assert deferred_removals == [(value, result)]

def test_sanitize_keys_conditions_mutable_set():
    value = set([1, 2, 3])
    deferred_removals = []
    result = _sanitize_keys_conditions(value, [], [], deferred_removals)
    assert result == set()
    assert deferred_removals == [(value, result)]

def test_sanitize_keys_conditions_immutable_set():
    value = frozenset([1, 2, 3])
    deferred_removals = []
    result = _sanitize_keys_conditions(value, [], [], deferred_removals)
    assert result == set()
    assert deferred_removals == [(value, result)]

def test_sanitize_keys_conditions_mutable_mapping():
    value = UserDict({'key': 'value'})
    deferred_removals = []
    result = _sanitize_keys_conditions(value, [], [], deferred_removals)
    assert result == type(value)()
    assert deferred_removals == [(value, result)]

def test_sanitize_keys_conditions_immutable_mapping():
    value = {'key': 'value'}
    deferred_removals = []
    result = _sanitize_keys_conditions(value, [], [], deferred_removals)
    assert result == {}
    assert deferred_removals == [(value, result)]

def test_sanitize_keys_conditions_integer():
    value = 42
    result = _sanitize_keys_conditions(value, [], [], [])
    assert result == value

def test_sanitize_keys_conditions_float():
    value = 3.14
    result = _sanitize_keys_conditions(value, [], [], [])
    assert result == value

def test_sanitize_keys_conditions_boolean():
    value = True
    result = _sanitize_keys_conditions(value, [], [], [])
    assert result == value

def test_sanitize_keys_conditions_none():
    value = None
    result = _sanitize_keys_conditions(value, [], [], [])
    assert result == value

def test_sanitize_keys_conditions_datetime():
    value = datetime.datetime.now()
    result = _sanitize_keys_conditions(value, [], [], [])
    assert result == value

def test_sanitize_keys_conditions_date():
    value = datetime.date.today()
    result = _sanitize_keys_conditions(value, [], [], [])
    assert result == value

def test_sanitize_keys_conditions_unknown_type():
    class CustomType:
        pass
    value = CustomType()
    with pytest.raises(TypeError):
        _sanitize_keys_conditions(value, [], [], [])
