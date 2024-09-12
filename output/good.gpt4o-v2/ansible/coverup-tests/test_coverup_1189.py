# file: lib/ansible/plugins/filter/core.py:240-250
# asked: {"lines": [241, 242, 243, 244, 245, 247, 248, 249, 250], "branches": [[243, 244], [243, 247]]}
# gained: {"lines": [241, 242, 243, 244, 245, 247, 250], "branches": [[243, 244], [243, 247]]}

import pytest
from ansible.plugins.filter.core import randomize_list

def test_randomize_list_with_seed():
    original_list = [1, 2, 3, 4, 5]
    seed = 123
    randomized_list = randomize_list(original_list, seed=seed)
    assert randomized_list != original_list
    assert sorted(randomized_list) == sorted(original_list)

def test_randomize_list_without_seed(mocker):
    original_list = [1, 2, 3, 4, 5]
    mocker.patch('ansible.plugins.filter.core.shuffle', side_effect=lambda x: x.reverse())
    randomized_list = randomize_list(original_list)
    assert randomized_list == original_list[::-1]
    assert sorted(randomized_list) == sorted(original_list)

def test_randomize_list_with_non_iterable():
    non_iterable = 12345
    result = randomize_list([non_iterable])
    assert result == [12345]

def test_randomize_list_with_empty_list():
    empty_list = []
    result = randomize_list(empty_list)
    assert result == []

@pytest.mark.parametrize("input_list", [
    (1, 2, 3, 4, 5),
    {1, 2, 3, 4, 5},
    "12345"
])
def test_randomize_list_with_various_iterables(input_list):
    result = randomize_list(input_list)
    assert sorted(result) == sorted(list(input_list))
