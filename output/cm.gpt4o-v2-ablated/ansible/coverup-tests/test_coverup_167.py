# file: lib/ansible/module_utils/common/text/formatters.py:25-36
# asked: {"lines": [25, 30, 31, 32, 33, 34, 35, 36], "branches": [[31, 32], [31, 36]]}
# gained: {"lines": [25, 30, 31, 32, 33, 34, 35, 36], "branches": [[31, 32], [31, 36]]}

import pytest

from ansible.module_utils.common.text.formatters import lenient_lowercase

def test_lenient_lowercase_all_strings():
    input_list = ['Hello', 'WORLD', 'PyThOn']
    expected_output = ['hello', 'world', 'python']
    assert lenient_lowercase(input_list) == expected_output

def test_lenient_lowercase_mixed_types():
    input_list = ['Hello', 123, 'WORLD', None, 'PyThOn', 45.6]
    expected_output = ['hello', 123, 'world', None, 'python', 45.6]
    assert lenient_lowercase(input_list) == expected_output

def test_lenient_lowercase_empty_list():
    input_list = []
    expected_output = []
    assert lenient_lowercase(input_list) == expected_output

def test_lenient_lowercase_no_strings():
    input_list = [123, None, 45.6, True]
    expected_output = [123, None, 45.6, True]
    assert lenient_lowercase(input_list) == expected_output
