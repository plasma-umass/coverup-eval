# file mimesis/providers/base.py:105-118
# lines [105, 112, 113, 114, 115, 117, 118]
# branches ['112->113', '112->118', '113->114', '113->117']

import pytest
from mimesis.providers.base import BaseDataProvider
from typing import Mapping

def test_update_dict_recursive():
    provider = BaseDataProvider()

    initial = {'level1': {'level2': {'item1': 'value1'}}}
    other = {'level1': {'level2': {'item2': 'value2'}, 'new_level2': 'new_value'}}

    expected = {
        'level1': {
            'level2': {
                'item1': 'value1',
                'item2': 'value2'
            },
            'new_level2': 'new_value'
        }
    }

    result = provider._update_dict(initial, other)
    assert result == expected, "The dictionary was not updated recursively as expected."

def test_update_dict_non_recursive():
    provider = BaseDataProvider()

    initial = {'item1': 'value1'}
    other = {'item2': 'value2'}

    expected = {'item1': 'value1', 'item2': 'value2'}

    result = provider._update_dict(initial, other)
    assert result == expected, "The dictionary was not updated correctly with non-recursive data."
