# file lib/ansible/plugins/filter/core.py:240-250
# lines [241, 242, 243, 244, 245, 247, 248, 249, 250]
# branches ['243->244', '243->247']

import pytest
from ansible.plugins.filter.core import randomize_list
from unittest.mock import patch

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
    mylist = [1, 2, 3, 4, 5]
    mocker.patch('ansible.plugins.filter.core.shuffle', side_effect=Exception('Test Exception'))
    result = randomize_list(mylist)
    assert result == mylist
