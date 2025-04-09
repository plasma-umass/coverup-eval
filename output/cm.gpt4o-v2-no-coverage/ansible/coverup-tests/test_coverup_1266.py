# file: lib/ansible/module_utils/common/parameters.py:372-463
# asked: {"lines": [408, 420, 430, 438, 446], "branches": [[407, 408], [409, 414], [411, 414], [419, 420], [427, 430], [435, 438], [443, 446], [454, 463], [455, 454]]}
# gained: {"lines": [430, 438], "branches": [[427, 430], [435, 438], [454, 463], [455, 454]]}

import pytest
from ansible.module_utils.common.parameters import _remove_values_conditions
from ansible.module_utils.six import PY2, PY3
import datetime

def test_remove_values_conditions_text_type(monkeypatch):
    no_log_strings = {"secret", "password"}
    deferred_removals = []

    # Test with text_type
    value = "this is a secret"
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == "this is a ********"

    # Test with binary_type
    value = b"this is a password"
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == b"this is a ********"

    # Test with text_type in no_log_strings
    value = "password"
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"

    # Test with binary_type in no_log_strings
    value = b"secret"
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"

def test_remove_values_conditions_sequence():
    no_log_strings = {"secret", "password"}
    deferred_removals = []

    # Test with MutableSequence
    value = ["this is a secret", "this is not"]
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == []
    assert deferred_removals == [(["this is a secret", "this is not"], [])]

    # Test with Sequence
    value = ("this is a secret", "this is not")
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == []
    assert deferred_removals == [(["this is a secret", "this is not"], []), (("this is a secret", "this is not"), [])]

def test_remove_values_conditions_set():
    no_log_strings = {"secret", "password"}
    deferred_removals = []

    # Test with MutableSet
    value = {"this is a secret", "this is not"}
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == set()
    assert deferred_removals == [({"this is a secret", "this is not"}, set())]

    # Test with Set
    value = frozenset({"this is a secret", "this is not"})
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == set()
    assert deferred_removals == [({"this is a secret", "this is not"}, set()), (frozenset({"this is a secret", "this is not"}), set())]

def test_remove_values_conditions_mapping():
    no_log_strings = {"secret", "password"}
    deferred_removals = []

    # Test with MutableMapping
    value = {"key": "this is a secret"}
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == {}
    assert deferred_removals == [({"key": "this is a secret"}, {})]

    # Test with Mapping
    value = {"key": "this is a secret"}
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == {}
    assert deferred_removals == [({"key": "this is a secret"}, {}), ({"key": "this is a secret"}, {})]

def test_remove_values_conditions_scalar():
    no_log_strings = {"secret", "password"}
    deferred_removals = []

    # Test with integer
    value = 12345
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == 12345

    # Test with float
    value = 123.45
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == 123.45

    # Test with boolean
    value = True
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result is True

    # Test with None
    value = None
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result is None

    # Test with integer in no_log_strings
    value = 12345
    no_log_strings.add("12345")
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"

def test_remove_values_conditions_datetime():
    no_log_strings = {"secret", "password"}
    deferred_removals = []

    # Test with datetime
    value = datetime.datetime(2023, 1, 1, 12, 0, 0)
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == "2023-01-01T12:00:00"

    # Test with date
    value = datetime.date(2023, 1, 1)
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == "2023-01-01"

def test_remove_values_conditions_unknown_type():
    no_log_strings = {"secret", "password"}
    deferred_removals = []

    # Test with unknown type
    class UnknownType:
        pass

    value = UnknownType()
    with pytest.raises(TypeError):
        _remove_values_conditions(value, no_log_strings, deferred_removals)
