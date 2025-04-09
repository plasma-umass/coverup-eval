# file: lib/ansible/module_utils/common/text/formatters.py:25-36
# asked: {"lines": [25, 30, 31, 32, 33, 34, 35, 36], "branches": [[31, 32], [31, 36]]}
# gained: {"lines": [25, 30, 31, 32, 33, 34, 35, 36], "branches": [[31, 32], [31, 36]]}

import pytest

from ansible.module_utils.common.text.formatters import lenient_lowercase

def test_lenient_lowercase_all_strings():
    input_list = ['FOO', 'BAR', 'BAZ']
    expected_output = ['foo', 'bar', 'baz']
    assert lenient_lowercase(input_list) == expected_output

def test_lenient_lowercase_mixed_types():
    input_list = ['FOO', 123, 'BAZ']
    expected_output = ['foo', 123, 'baz']
    assert lenient_lowercase(input_list) == expected_output

def test_lenient_lowercase_non_string():
    input_list = [123, 456, 789]
    expected_output = [123, 456, 789]
    assert lenient_lowercase(input_list) == expected_output

def test_lenient_lowercase_empty_list():
    input_list = []
    expected_output = []
    assert lenient_lowercase(input_list) == expected_output
