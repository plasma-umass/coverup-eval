# file: lib/ansible/parsing/splitter.py:141-152
# asked: {"lines": [141, 146, 147, 148, 149, 151, 152], "branches": [[147, 148], [147, 152], [148, 149], [148, 151]]}
# gained: {"lines": [141, 146, 147, 148, 149, 151, 152], "branches": [[147, 148], [147, 152], [148, 149], [148, 151]]}

import pytest
from ansible.parsing.splitter import join_args, split_args

def test_join_args_with_newlines():
    input_data = ["echo", "hello", "\n", "world"]
    expected_output = "echo hello \nworld"
    assert join_args(input_data) == expected_output

def test_join_args_without_newlines():
    input_data = ["echo", "hello", "world"]
    expected_output = "echo hello world"
    assert join_args(input_data) == expected_output

def test_join_args_empty():
    input_data = []
    expected_output = ""
    assert join_args(input_data) == expected_output

def test_join_args_single_element():
    input_data = ["echo"]
    expected_output = "echo"
    assert join_args(input_data) == expected_output

def test_join_args_with_multiple_newlines():
    input_data = ["echo", "hello", "\n", "world", "\n", "again"]
    expected_output = "echo hello \nworld \nagain"
    assert join_args(input_data) == expected_output

def test_join_args_with_trailing_space():
    input_data = ["echo", "hello", " ", "world"]
    expected_output = "echo hello   world"
    assert join_args(input_data) == expected_output
