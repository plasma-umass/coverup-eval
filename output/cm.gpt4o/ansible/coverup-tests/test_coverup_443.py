# file lib/ansible/module_utils/common/text/formatters.py:25-36
# lines [25, 30, 31, 32, 33, 34, 35, 36]
# branches ['31->32', '31->36']

import pytest

from ansible.module_utils.common.text.formatters import lenient_lowercase

def test_lenient_lowercase():
    # Test with a list of strings
    input_data = ['Hello', 'WORLD', 'PyThOn']
    expected_output = ['hello', 'world', 'python']
    assert lenient_lowercase(input_data) == expected_output

    # Test with a list of mixed types
    input_data = ['Hello', 123, 'WORLD', None, 'PyThOn', 45.6]
    expected_output = ['hello', 123, 'world', None, 'python', 45.6]
    assert lenient_lowercase(input_data) == expected_output

    # Test with an empty list
    input_data = []
    expected_output = []
    assert lenient_lowercase(input_data) == expected_output

    # Test with a list of non-string types
    input_data = [123, None, 45.6, True, False]
    expected_output = [123, None, 45.6, True, False]
    assert lenient_lowercase(input_data) == expected_output
