# file: lib/ansible/module_utils/common/parameters.py:827-868
# asked: {"lines": [841, 843, 844, 846, 847, 849, 850, 851, 852, 856, 857, 859, 860, 861, 862, 863, 864, 866, 868], "branches": [[846, 847], [846, 868], [849, 850], [849, 859], [850, 846], [850, 851], [851, 852], [851, 856], [859, 846], [859, 860], [861, 862], [861, 863], [863, 864], [863, 866]]}
# gained: {"lines": [841, 843, 844, 846, 847, 849, 850, 851, 852, 856, 857, 859, 860, 861, 862, 863, 864, 868], "branches": [[846, 847], [846, 868], [849, 850], [849, 859], [850, 846], [850, 851], [851, 852], [851, 856], [859, 846], [859, 860], [861, 862], [861, 863], [863, 864]]}

import pytest
from collections import deque
from ansible.module_utils.common.parameters import sanitize_keys
from ansible.module_utils.common._collections_compat import MutableSet, MutableSequence, Mapping

def test_sanitize_keys_with_mapping(monkeypatch):
    # Mocking _sanitize_keys_conditions and _remove_values_conditions
    def mock_sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals):
        if isinstance(value, dict):
            new_value = {}
            deferred_removals.append((value, new_value))
            return new_value
        return value

    def mock_remove_values_conditions(value, no_log_strings, deferred_removals):
        return value

    monkeypatch.setattr('ansible.module_utils.common.parameters._sanitize_keys_conditions', mock_sanitize_keys_conditions)
    monkeypatch.setattr('ansible.module_utils.common.parameters._remove_values_conditions', mock_remove_values_conditions)

    obj = {'key1': 'value1', 'key2': 'value2'}
    no_log_strings = {'value1'}
    ignore_keys = frozenset({'key2'})

    result = sanitize_keys(obj, no_log_strings, ignore_keys)

    assert 'key1' in result
    assert 'key2' in result
    assert result['key2'] == 'value2'

def test_sanitize_keys_with_sequence(monkeypatch):
    def mock_sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals):
        if isinstance(value, list):
            new_value = []
            deferred_removals.append((value, new_value))
            return new_value
        return value

    def mock_remove_values_conditions(value, no_log_strings, deferred_removals):
        return value

    monkeypatch.setattr('ansible.module_utils.common.parameters._sanitize_keys_conditions', mock_sanitize_keys_conditions)
    monkeypatch.setattr('ansible.module_utils.common.parameters._remove_values_conditions', mock_remove_values_conditions)

    obj = ['value1', 'value2']
    no_log_strings = {'value1'}
    ignore_keys = frozenset()

    result = sanitize_keys(obj, no_log_strings, ignore_keys)

    assert 'value1' in result
    assert 'value2' in result

def test_sanitize_keys_with_set(monkeypatch):
    def mock_sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals):
        if isinstance(value, set):
            new_value = set()
            deferred_removals.append((value, new_value))
            return new_value
        return value

    def mock_remove_values_conditions(value, no_log_strings, deferred_removals):
        return value

    monkeypatch.setattr('ansible.module_utils.common.parameters._sanitize_keys_conditions', mock_sanitize_keys_conditions)
    monkeypatch.setattr('ansible.module_utils.common.parameters._remove_values_conditions', mock_remove_values_conditions)

    obj = {'value1', 'value2'}
    no_log_strings = {'value1'}
    ignore_keys = frozenset()

    result = sanitize_keys(obj, no_log_strings, ignore_keys)

    assert 'value1' in result
    assert 'value2' in result

def test_sanitize_keys_with_unknown_type(monkeypatch):
    def mock_sanitize_keys_conditions(value, no_log_strings, ignore_keys, deferred_removals):
        raise TypeError('Value of unknown type: %s, %s' % (type(value), value))

    monkeypatch.setattr('ansible.module_utils.common.parameters._sanitize_keys_conditions', mock_sanitize_keys_conditions)

    obj = 12345
    no_log_strings = {'value1'}
    ignore_keys = frozenset()

    with pytest.raises(TypeError):
        sanitize_keys(obj, no_log_strings, ignore_keys)
