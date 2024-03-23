# file mimesis/providers/base.py:105-118
# lines [105, 112, 113, 114, 115, 117, 118]
# branches ['112->113', '112->118', '113->114', '113->117']

import pytest
from mimesis.providers.base import BaseDataProvider
from typing import Mapping

def test_update_dict_recursive():
    provider = BaseDataProvider()

    initial = {'a': 1, 'b': {'c': 2}}
    other = {'b': {'d': 3}, 'e': 4}

    expected = {'a': 1, 'b': {'c': 2, 'd': 3}, 'e': 4}
    result = provider._update_dict(initial, other)
    assert result == expected, "The dictionary was not updated correctly."

def test_update_dict_with_new_key():
    provider = BaseDataProvider()

    initial = {'a': 1}
    other = {'b': 2}

    expected = {'a': 1, 'b': 2}
    result = provider._update_dict(initial, other)
    assert result == expected, "The dictionary was not updated with the new key."

def test_update_dict_overwrite_value():
    provider = BaseDataProvider()

    initial = {'a': 1}
    other = {'a': 2}

    expected = {'a': 2}
    result = provider._update_dict(initial, other)
    assert result == expected, "The dictionary value for key 'a' was not overwritten."

def test_update_dict_empty_other():
    provider = BaseDataProvider()

    initial = {'a': 1}
    other = {}

    expected = {'a': 1}
    result = provider._update_dict(initial, other)
    assert result == expected, "The dictionary should not change when 'other' is empty."

def test_update_dict_empty_initial():
    provider = BaseDataProvider()

    initial = {}
    other = {'a': 1}

    expected = {'a': 1}
    result = provider._update_dict(initial, other)
    assert result == expected, "The dictionary should be updated with 'other' when 'initial' is empty."

def test_update_dict_nested_empty_initial():
    provider = BaseDataProvider()

    initial = {}
    other = {'a': {'b': 1}}

    expected = {'a': {'b': 1}}
    result = provider._update_dict(initial, other)
    assert result == expected, "The nested dictionary should be updated with 'other' when 'initial' is empty."
