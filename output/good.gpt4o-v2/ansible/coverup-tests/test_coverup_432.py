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
    input_list = ['FOO', 123, 'BAR', None, 'BAZ', 45.6]
    expected_output = ['foo', 123, 'bar', None, 'baz', 45.6]
    assert lenient_lowercase(input_list) == expected_output

def test_lenient_lowercase_empty_list():
    input_list = []
    expected_output = []
    assert lenient_lowercase(input_list) == expected_output

def test_lenient_lowercase_no_strings():
    input_list = [123, None, 45.6]
    expected_output = [123, None, 45.6]
    assert lenient_lowercase(input_list) == expected_output
