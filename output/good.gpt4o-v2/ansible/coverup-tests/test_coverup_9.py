# file: lib/ansible/module_utils/common/parameters.py:372-463
# asked: {"lines": [372, 402, 404, 405, 406, 407, 408, 409, 410, 411, 412, 414, 415, 416, 417, 419, 420, 421, 422, 424, 426, 427, 428, 430, 431, 432, 434, 435, 436, 438, 439, 440, 442, 443, 444, 446, 447, 448, 450, 451, 452, 453, 454, 455, 456, 458, 459, 461, 463], "branches": [[402, 404], [402, 426], [405, 406], [405, 409], [407, 408], [407, 414], [409, 410], [409, 414], [411, 412], [411, 414], [414, 415], [414, 416], [416, 417], [416, 419], [419, 420], [419, 421], [421, 422], [421, 424], [426, 427], [426, 434], [427, 428], [427, 430], [434, 435], [434, 442], [435, 436], [435, 438], [442, 443], [442, 450], [443, 444], [443, 446], [450, 451], [450, 458], [452, 453], [452, 454], [454, 455], [454, 463], [455, 454], [455, 456], [458, 459], [458, 461]]}
# gained: {"lines": [372, 402, 404, 405, 406, 407, 409, 410, 411, 412, 414, 415, 416, 417, 419, 421, 422, 424, 426, 427, 428, 431, 432, 434, 435, 436, 439, 440, 442, 443, 444, 447, 448, 450, 451, 452, 453, 454, 455, 458, 459, 461, 463], "branches": [[402, 404], [402, 426], [405, 406], [405, 409], [407, 414], [409, 410], [411, 412], [414, 415], [414, 416], [416, 417], [416, 419], [419, 421], [421, 422], [421, 424], [426, 427], [426, 434], [427, 428], [434, 435], [434, 442], [435, 436], [442, 443], [442, 450], [443, 444], [450, 451], [450, 458], [452, 453], [452, 454], [454, 455], [454, 463], [455, 454], [458, 459], [458, 461]]}

import pytest
from ansible.module_utils.common.parameters import _remove_values_conditions
from ansible.module_utils.six import PY2, PY3, text_type, binary_type
import datetime

def test_remove_values_conditions_text_type(monkeypatch):
    no_log_strings = {"secret", "password"}
    deferred_removals = []

    # Test with text_type value
    value = "this is a secret"
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == "this is a ********"

    # Test with text_type value in no_log_strings
    value = "password"
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"

def test_remove_values_conditions_binary_type(monkeypatch):
    no_log_strings = {"secret", "password"}
    deferred_removals = []

    # Test with binary_type value
    value = b"this is a secret"
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == b"this is a ********"

    # Test with binary_type value in no_log_strings
    value = b"password"
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"

def test_remove_values_conditions_sequence(monkeypatch):
    no_log_strings = {"secret", "password"}
    deferred_removals = []

    # Test with Sequence value
    value = ["this is a secret", "this is not"]
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == []
    assert deferred_removals == [(["this is a secret", "this is not"], [])]

def test_remove_values_conditions_set(monkeypatch):
    no_log_strings = {"secret", "password"}
    deferred_removals = []

    # Test with Set value
    value = {"this is a secret", "this is not"}
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == set()
    assert deferred_removals == [({"this is a secret", "this is not"}, set())]

def test_remove_values_conditions_mapping(monkeypatch):
    no_log_strings = {"secret", "password"}
    deferred_removals = []

    # Test with Mapping value
    value = {"key1": "this is a secret", "key2": "this is not"}
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == {}
    assert deferred_removals == [({"key1": "this is a secret", "key2": "this is not"}, {})]

def test_remove_values_conditions_scalar(monkeypatch):
    no_log_strings = {"42", "3.14"}
    deferred_removals = []

    # Test with integer value
    value = 42
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"

    # Test with float value
    value = 3.14
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == "VALUE_SPECIFIED_IN_NO_LOG_PARAMETER"

    # Test with boolean value
    value = True
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result is True

def test_remove_values_conditions_datetime(monkeypatch):
    no_log_strings = {"2023-10-01T00:00:00"}
    deferred_removals = []

    # Test with datetime value
    value = datetime.datetime(2023, 10, 1)
    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == "2023-10-01T00:00:00"

def test_remove_values_conditions_unknown_type(monkeypatch):
    no_log_strings = {"unknown"}
    deferred_removals = []

    # Test with unknown type value
    class UnknownType:
        pass

    value = UnknownType()
    with pytest.raises(TypeError):
        _remove_values_conditions(value, no_log_strings, deferred_removals)
