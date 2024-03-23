# file lib/ansible/plugins/filter/core.py:240-250
# lines [240, 241, 242, 243, 244, 245, 247, 248, 249, 250]
# branches ['243->244', '243->247']

import pytest
from ansible.plugins.filter.core import randomize_list
from unittest.mock import patch
from random import Random

def test_randomize_list_with_seed():
    test_list = [1, 2, 3, 4, 5]
    seed = 12345
    r = Random(seed)
    expected_list = test_list[:]
    r.shuffle(expected_list)  # Shuffle with the given seed to determine expected list
    result = randomize_list(test_list, seed)
    assert result == expected_list, "The list was not shuffled as expected with the given seed."

def test_randomize_list_without_seed():
    test_list = [1, 2, 3, 4, 5]
    result = randomize_list(test_list)
    assert set(result) == set(test_list), "The shuffled list does not contain the same elements as the original list."

def test_randomize_list_exception_handling():
    with patch('ansible.plugins.filter.core.shuffle', side_effect=Exception):
        test_list = [1, 2, 3, 4, 5]
        result = randomize_list(test_list)
        assert result == test_list, "The list should not be modified if an exception occurs during shuffling."
