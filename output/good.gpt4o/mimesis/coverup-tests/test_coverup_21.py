# file mimesis/providers/base.py:105-118
# lines [105, 112, 113, 114, 115, 117, 118]
# branches ['112->113', '112->118', '113->114', '113->117']

import pytest
from mimesis.providers.base import BaseDataProvider
import collections.abc

@pytest.fixture
def base_data_provider():
    return BaseDataProvider()

def test_update_dict_with_nested_dicts(base_data_provider):
    initial = {
        'a': 1,
        'b': {
            'c': 2,
            'd': 3,
        },
        'e': 4,
    }
    other = {
        'b': {
            'c': 20,
            'f': 30,
        },
        'g': 5,
    }
    expected = {
        'a': 1,
        'b': {
            'c': 20,
            'd': 3,
            'f': 30,
        },
        'e': 4,
        'g': 5,
    }
    result = base_data_provider._update_dict(initial, other)
    assert result == expected

def test_update_dict_with_non_dict_values(base_data_provider):
    initial = {
        'a': 1,
        'b': 2,
    }
    other = {
        'b': 3,
        'c': 4,
    }
    expected = {
        'a': 1,
        'b': 3,
        'c': 4,
    }
    result = base_data_provider._update_dict(initial, other)
    assert result == expected

def test_update_dict_with_empty_initial(base_data_provider):
    initial = {}
    other = {
        'a': 1,
        'b': {
            'c': 2,
        },
    }
    expected = {
        'a': 1,
        'b': {
            'c': 2,
        },
    }
    result = base_data_provider._update_dict(initial, other)
    assert result == expected

def test_update_dict_with_empty_other(base_data_provider):
    initial = {
        'a': 1,
        'b': {
            'c': 2,
        },
    }
    other = {}
    expected = {
        'a': 1,
        'b': {
            'c': 2,
        },
    }
    result = base_data_provider._update_dict(initial, other)
    assert result == expected
