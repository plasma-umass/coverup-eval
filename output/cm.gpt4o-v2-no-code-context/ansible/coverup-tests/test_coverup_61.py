# file: lib/ansible/module_utils/common/parameters.py:827-868
# asked: {"lines": [827, 841, 843, 844, 846, 847, 849, 850, 851, 852, 856, 857, 859, 860, 861, 862, 863, 864, 866, 868], "branches": [[846, 847], [846, 868], [849, 850], [849, 859], [850, 846], [850, 851], [851, 852], [851, 856], [859, 846], [859, 860], [861, 862], [861, 863], [863, 864], [863, 866]]}
# gained: {"lines": [827, 841, 843, 844, 846, 847, 849, 850, 851, 852, 856, 857, 859, 860, 861, 862, 863, 864, 866, 868], "branches": [[846, 847], [846, 868], [849, 850], [849, 859], [850, 846], [850, 851], [851, 852], [851, 856], [859, 846], [859, 860], [861, 862], [861, 863], [863, 864], [863, 866]]}

import pytest
from collections import deque
from ansible.module_utils.common.parameters import sanitize_keys

def test_sanitize_keys_dict(monkeypatch):
    def mock_to_native(s, errors='surrogate_or_strict'):
        return s

    def mock_sanitize_keys_conditions(obj, no_log_strings, ignore_keys, deferred_removals):
        if isinstance(obj, dict):
            new_data = {}
            deferred_removals.append((obj, new_data))
            return new_data
        return obj

    def mock_remove_values_conditions(key, no_log_strings, _):
        return key.replace('secret', 'sanitized')

    monkeypatch.setattr('ansible.module_utils.common.parameters.to_native', mock_to_native)
    monkeypatch.setattr('ansible.module_utils.common.parameters._sanitize_keys_conditions', mock_sanitize_keys_conditions)
    monkeypatch.setattr('ansible.module_utils.common.parameters._remove_values_conditions', mock_remove_values_conditions)

    obj = {'secret_key': 'value', 'normal_key': 'value'}
    no_log_strings = {'secret'}
    ignore_keys = frozenset({'normal_key'})

    result = sanitize_keys(obj, no_log_strings, ignore_keys)

    assert 'sanitized_key' in result
    assert 'normal_key' in result
    assert result['sanitized_key'] == 'value'
    assert result['normal_key'] == 'value'

def test_sanitize_keys_list(monkeypatch):
    def mock_to_native(s, errors='surrogate_or_strict'):
        return s

    def mock_sanitize_keys_conditions(obj, no_log_strings, ignore_keys, deferred_removals):
        if isinstance(obj, list):
            new_data = []
            deferred_removals.append((obj, new_data))
            return new_data
        return obj

    monkeypatch.setattr('ansible.module_utils.common.parameters.to_native', mock_to_native)
    monkeypatch.setattr('ansible.module_utils.common.parameters._sanitize_keys_conditions', mock_sanitize_keys_conditions)

    obj = ['secret_value', 'normal_value']
    no_log_strings = {'secret'}
    ignore_keys = frozenset()

    result = sanitize_keys(obj, no_log_strings, ignore_keys)

    assert 'secret_value' in result
    assert 'normal_value' in result

def test_sanitize_keys_set(monkeypatch):
    def mock_to_native(s, errors='surrogate_or_strict'):
        return s

    def mock_sanitize_keys_conditions(obj, no_log_strings, ignore_keys, deferred_removals):
        if isinstance(obj, set):
            new_data = set()
            deferred_removals.append((obj, new_data))
            return new_data
        return obj

    monkeypatch.setattr('ansible.module_utils.common.parameters.to_native', mock_to_native)
    monkeypatch.setattr('ansible.module_utils.common.parameters._sanitize_keys_conditions', mock_sanitize_keys_conditions)

    obj = {'secret_value', 'normal_value'}
    no_log_strings = {'secret'}
    ignore_keys = frozenset()

    result = sanitize_keys(obj, no_log_strings, ignore_keys)

    assert 'secret_value' in result
    assert 'normal_value' in result

def test_sanitize_keys_unknown_container(monkeypatch):
    def mock_to_native(s, errors='surrogate_or_strict'):
        return s

    def mock_sanitize_keys_conditions(obj, no_log_strings, ignore_keys, deferred_removals):
        if isinstance(obj, tuple):
            new_data = ()
            deferred_removals.append((obj, new_data))
            return new_data
        return obj

    monkeypatch.setattr('ansible.module_utils.common.parameters.to_native', mock_to_native)
    monkeypatch.setattr('ansible.module_utils.common.parameters._sanitize_keys_conditions', mock_sanitize_keys_conditions)

    obj = ('secret_value', 'normal_value')
    no_log_strings = {'secret'}
    ignore_keys = frozenset()

    with pytest.raises(TypeError, match='Unknown container type encountered when removing private values from keys'):
        sanitize_keys(obj, no_log_strings, ignore_keys)
