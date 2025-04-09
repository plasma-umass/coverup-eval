# file lib/ansible/module_utils/common/text/formatters.py:25-36
# lines [25, 30, 31, 32, 33, 34, 35, 36]
# branches ['31->32', '31->36']

import pytest
from ansible.module_utils.common.text.formatters import lenient_lowercase

def test_lenient_lowercase_with_strings():
    input_list = ['STRING', 'TeSt', 'lower']
    expected_output = ['string', 'test', 'lower']
    assert lenient_lowercase(input_list) == expected_output

def test_lenient_lowercase_with_non_strings():
    input_list = ['STRING', 42, 'lower', None, True]
    expected_output = ['string', 42, 'lower', None, True]
    assert lenient_lowercase(input_list) == expected_output
