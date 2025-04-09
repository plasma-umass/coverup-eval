# file lib/ansible/module_utils/common/parameters.py:503-538
# lines [503, 505, 506, 508, 509, 510, 512, 513, 514, 516, 517, 518, 520, 521, 522, 524, 525, 526, 528, 529, 530, 532, 533, 535, 536, 538]
# branches ['505->506', '505->508', '508->509', '508->516', '509->510', '509->512', '516->517', '516->524', '517->518', '517->520', '524->525', '524->532', '525->526', '525->528', '532->533', '532->535', '535->536', '535->538']

import pytest
from ansible.module_utils.common.parameters import _sanitize_keys_conditions
from collections.abc import MutableSequence, MutableSet, MutableMapping, Sequence, Set, Mapping
from ansible.module_utils.six import text_type, binary_type, integer_types
from types import NoneType
import datetime

@pytest.fixture
def cleanup_deferred_removals():
    deferred_removals = []
    yield deferred_removals
    del deferred_removals[:]

def test_sanitize_keys_conditions_with_mutable_sequence(cleanup_deferred_removals):
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = cleanup_deferred_removals
    value = [1, 2, 3]

    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert isinstance(result, MutableSequence)
    assert len(deferred_removals) == 1
    assert deferred_removals[0] == (value, result)

def test_sanitize_keys_conditions_with_immutable_sequence(cleanup_deferred_removals):
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = cleanup_deferred_removals
    value = (1, 2, 3)

    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert isinstance(result, list)  # Immutable sequences become lists
    assert len(deferred_removals) == 1
    assert deferred_removals[0] == (value, result)

def test_sanitize_keys_conditions_with_mutable_set(cleanup_deferred_removals):
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = cleanup_deferred_removals
    value = {1, 2, 3}

    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert isinstance(result, MutableSet)
    assert len(deferred_removals) == 1
    assert deferred_removals[0] == (value, result)

def test_sanitize_keys_conditions_with_immutable_set(cleanup_deferred_removals):
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = cleanup_deferred_removals
    value = frozenset([1, 2, 3])

    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert isinstance(result, set)  # Immutable sets become mutable sets
    assert len(deferred_removals) == 1
    assert deferred_removals[0] == (value, result)

def test_sanitize_keys_conditions_with_mutable_mapping(cleanup_deferred_removals):
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = cleanup_deferred_removals
    value = {'a': 1, 'b': 2}

    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert isinstance(result, MutableMapping)
    assert len(deferred_removals) == 1
    assert deferred_removals[0] == (value, result)

def test_sanitize_keys_conditions_with_immutable_mapping(cleanup_deferred_removals):
    from types import MappingProxyType
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = cleanup_deferred_removals
    value = MappingProxyType({'a': 1, 'b': 2})

    result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
    assert isinstance(result, dict)  # Immutable mappings become dicts
    assert len(deferred_removals) == 1
    assert deferred_removals[0] == (value, result)

def test_sanitize_keys_conditions_with_simple_types(cleanup_deferred_removals):
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = cleanup_deferred_removals
    simple_values = [42, 3.14, True, None, datetime.datetime.now(), datetime.date.today()]

    for value in simple_values:
        result = _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
        assert result == value

def test_sanitize_keys_conditions_with_unknown_type(cleanup_deferred_removals):
    no_log_strings = set()
    ignore_keys = set()
    deferred_removals = cleanup_deferred_removals
    value = object()

    with pytest.raises(TypeError):
        _sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals)
