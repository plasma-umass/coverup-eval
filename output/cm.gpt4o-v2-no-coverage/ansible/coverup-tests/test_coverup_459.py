# file: lib/ansible/parsing/splitter.py:141-152
# asked: {"lines": [141, 146, 147, 148, 149, 151, 152], "branches": [[147, 148], [147, 152], [148, 149], [148, 151]]}
# gained: {"lines": [141, 146, 147, 148, 149, 151, 152], "branches": [[147, 148], [147, 152], [148, 149], [148, 151]]}

import pytest

from ansible.parsing.splitter import join_args

def test_join_args_empty_list():
    assert join_args([]) == ''

def test_join_args_single_element():
    assert join_args(['arg1']) == 'arg1'

def test_join_args_multiple_elements_no_newline():
    assert join_args(['arg1', 'arg2', 'arg3']) == 'arg1 arg2 arg3'

def test_join_args_multiple_elements_with_newline():
    assert join_args(['arg1\n', 'arg2', 'arg3']) == 'arg1\narg2 arg3'

def test_join_args_multiple_elements_with_newline_in_middle():
    assert join_args(['arg1', 'arg2\n', 'arg3']) == 'arg1 arg2\narg3'

def test_join_args_multiple_elements_with_newline_at_end():
    assert join_args(['arg1', 'arg2', 'arg3\n']) == 'arg1 arg2 arg3\n'
