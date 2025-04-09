# file lib/ansible/module_utils/common/parameters.py:503-538
# lines [505, 506, 508, 509, 510, 512, 513, 514, 516, 517, 518, 520, 521, 522, 524, 525, 526, 528, 529, 530, 532, 533, 535, 536, 538]
# branches ['505->506', '505->508', '508->509', '508->516', '509->510', '509->512', '516->517', '516->524', '517->518', '517->520', '524->525', '524->532', '525->526', '525->528', '532->533', '532->535', '535->536', '535->538']

import pytest
from ansible.module_utils.common.parameters import _sanitize_keys_conditions

def test_sanitize_keys_conditions(mocker):
    no_log_strings = []
    ignore_keys = []
    deferred_removals = []

    # Test for text_type
    assert _sanitize_keys_conditions("string", no_log_strings, ignore_keys, deferred_removals) == "string"

    # Test for binary_type
    assert _sanitize_keys_conditions(b"bytes", no_log_strings, ignore_keys, deferred_removals) == b"bytes"

    # Test for MutableSequence
    mutable_sequence = [1, 2, 3]
    result = _sanitize_keys_conditions(mutable_sequence, no_log_strings, ignore_keys, deferred_removals)
    assert result == []
    assert deferred_removals == [(mutable_sequence, [])]

    # Test for Sequence
    sequence = (1, 2, 3)
    result = _sanitize_keys_conditions(sequence, no_log_strings, ignore_keys, deferred_removals)
    assert result == []
    assert deferred_removals[-1] == (sequence, [])

    # Test for MutableSet
    mutable_set = {1, 2, 3}
    result = _sanitize_keys_conditions(mutable_set, no_log_strings, ignore_keys, deferred_removals)
    assert result == set()
    assert deferred_removals[-1] == (mutable_set, set())

    # Test for Set
    set_value = frozenset([1, 2, 3])
    result = _sanitize_keys_conditions(set_value, no_log_strings, ignore_keys, deferred_removals)
    assert result == set()
    assert deferred_removals[-1] == (set_value, set())

    # Test for MutableMapping
    mutable_mapping = {'key': 'value'}
    result = _sanitize_keys_conditions(mutable_mapping, no_log_strings, ignore_keys, deferred_removals)
    assert result == {}
    assert deferred_removals[-1] == (mutable_mapping, {})

    # Test for Mapping
    mapping = {'key': 'value'}
    result = _sanitize_keys_conditions(mapping, no_log_strings, ignore_keys, deferred_removals)
    assert result == {}
    assert deferred_removals[-1] == (mapping, {})

    # Test for integer_types, float, bool, NoneType
    assert _sanitize_keys_conditions(42, no_log_strings, ignore_keys, deferred_removals) == 42
    assert _sanitize_keys_conditions(3.14, no_log_strings, ignore_keys, deferred_removals) == 3.14
    assert _sanitize_keys_conditions(True, no_log_strings, ignore_keys, deferred_removals) == True
    assert _sanitize_keys_conditions(None, no_log_strings, ignore_keys, deferred_removals) == None

    # Test for datetime.datetime and datetime.date
    import datetime
    now = datetime.datetime.now()
    today = datetime.date.today()
    assert _sanitize_keys_conditions(now, no_log_strings, ignore_keys, deferred_removals) == now
    assert _sanitize_keys_conditions(today, no_log_strings, ignore_keys, deferred_removals) == today

    # Test for unknown type
    class CustomType:
        pass

    with pytest.raises(TypeError) as excinfo:
        _sanitize_keys_conditions(CustomType(), no_log_strings, ignore_keys, deferred_removals)
    assert 'Value of unknown type' in str(excinfo.value)
