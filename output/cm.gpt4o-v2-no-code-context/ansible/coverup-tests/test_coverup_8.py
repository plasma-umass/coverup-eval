# file: lib/ansible/module_utils/common/parameters.py:372-463
# asked: {"lines": [372, 402, 404, 405, 406, 407, 408, 409, 410, 411, 412, 414, 415, 416, 417, 419, 420, 421, 422, 424, 426, 427, 428, 430, 431, 432, 434, 435, 436, 438, 439, 440, 442, 443, 444, 446, 447, 448, 450, 451, 452, 453, 454, 455, 456, 458, 459, 461, 463], "branches": [[402, 404], [402, 426], [405, 406], [405, 409], [407, 408], [407, 414], [409, 410], [409, 414], [411, 412], [411, 414], [414, 415], [414, 416], [416, 417], [416, 419], [419, 420], [419, 421], [421, 422], [421, 424], [426, 427], [426, 434], [427, 428], [427, 430], [434, 435], [434, 442], [435, 436], [435, 438], [442, 443], [442, 450], [443, 444], [443, 446], [450, 451], [450, 458], [452, 453], [452, 454], [454, 455], [454, 463], [455, 454], [455, 456], [458, 459], [458, 461]]}
# gained: {"lines": [372, 402, 404, 405, 406, 407, 409, 410, 411, 412, 414, 415, 426, 427, 428, 431, 432, 434, 435, 436, 439, 440, 442, 443, 444, 447, 448, 450, 451, 452, 453, 458, 459, 461, 463], "branches": [[402, 404], [402, 426], [405, 406], [405, 409], [407, 414], [409, 410], [411, 412], [414, 415], [426, 427], [426, 434], [427, 428], [434, 435], [434, 442], [435, 436], [442, 443], [442, 450], [443, 444], [450, 451], [450, 458], [452, 453], [458, 459], [458, 461]]}

import pytest
from ansible.module_utils.common.parameters import _remove_values_conditions
from collections.abc import MutableSequence, MutableSet, MutableMapping
from datetime import datetime, date
import sys

def test_remove_values_conditions_text_type(monkeypatch):
    value = "sensitive_data"
    no_log_strings = {"sensitive_data"}
    deferred_removals = []

    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'

def test_remove_values_conditions_binary_type(monkeypatch):
    value = b"sensitive_data"
    no_log_strings = {b"sensitive_data"}
    deferred_removals = []

    if sys.version_info[0] == 2:
        from ansible.module_utils._text import to_bytes
        value = to_bytes(value)

    # Convert no_log_strings to text for replacement
    no_log_strings_text = {value.decode('utf-8') for value in no_log_strings}

    result = _remove_values_conditions(value, no_log_strings_text, deferred_removals)
    assert result == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'

def test_remove_values_conditions_sequence(monkeypatch):
    value = ["sensitive_data"]
    no_log_strings = {"sensitive_data"}
    deferred_removals = []

    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == []
    assert deferred_removals == [(["sensitive_data"], [])]

def test_remove_values_conditions_set(monkeypatch):
    value = {"sensitive_data"}
    no_log_strings = {"sensitive_data"}
    deferred_removals = []

    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == set()
    assert deferred_removals == [({"sensitive_data"}, set())]

def test_remove_values_conditions_mapping(monkeypatch):
    value = {"key": "sensitive_data"}
    no_log_strings = {"sensitive_data"}
    deferred_removals = []

    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == {}
    assert deferred_removals == [({"key": "sensitive_data"}, {})]

def test_remove_values_conditions_integer(monkeypatch):
    value = 12345
    no_log_strings = {"12345"}
    deferred_removals = []

    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'

def test_remove_values_conditions_float(monkeypatch):
    value = 123.45
    no_log_strings = {"123.45"}
    deferred_removals = []

    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'

def test_remove_values_conditions_bool(monkeypatch):
    value = True
    no_log_strings = {"True"}
    deferred_removals = []

    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'

def test_remove_values_conditions_none(monkeypatch):
    value = None
    no_log_strings = {"None"}
    deferred_removals = []

    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == 'VALUE_SPECIFIED_IN_NO_LOG_PARAMETER'

def test_remove_values_conditions_datetime(monkeypatch):
    value = datetime(2023, 1, 1)
    no_log_strings = set()
    deferred_removals = []

    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == '2023-01-01T00:00:00'

def test_remove_values_conditions_date(monkeypatch):
    value = date(2023, 1, 1)
    no_log_strings = set()
    deferred_removals = []

    result = _remove_values_conditions(value, no_log_strings, deferred_removals)
    assert result == '2023-01-01'

def test_remove_values_conditions_unknown_type(monkeypatch):
    class UnknownType:
        pass

    value = UnknownType()
    no_log_strings = set()
    deferred_removals = []

    with pytest.raises(TypeError):
        _remove_values_conditions(value, no_log_strings, deferred_removals)
