# file: lib/ansible/plugins/filter/core.py:240-250
# asked: {"lines": [248, 249], "branches": []}
# gained: {"lines": [248, 249], "branches": []}

import pytest
from ansible.plugins.filter.core import randomize_list

def test_randomize_list_with_seed():
    mylist = [1, 2, 3, 4, 5]
    seed = 123
    result = randomize_list(mylist, seed)
    assert result != mylist
    assert sorted(result) == sorted(mylist)

def test_randomize_list_without_seed():
    mylist = [1, 2, 3, 4, 5]
    result = randomize_list(mylist)
    assert result != mylist
    assert sorted(result) == sorted(mylist)

def test_randomize_list_with_non_iterable():
    mylist = None
    result = randomize_list(mylist)
    assert result is None

def test_randomize_list_with_exception(mocker):
    mocker.patch('ansible.plugins.filter.core.list', side_effect=Exception("Test Exception"))
    mylist = [1, 2, 3, 4, 5]
    result = randomize_list(mylist)
    assert result == mylist
