# file lib/ansible/module_utils/facts/utils.py:63-76
# lines [63, 65, 66, 67, 68, 70, 71, 73, 75, 76]
# branches ['66->67', '66->75', '67->68', '67->70', '70->71', '70->73']

import pytest
from unittest import mock
from ansible.module_utils.facts.utils import get_file_lines

def test_get_file_lines(mocker):
    mocker.patch('ansible.module_utils.facts.utils.get_file_content', return_value="line1\nline2\nline3\n")

    # Test default behavior with strip=True and line_sep=None
    result = get_file_lines('dummy_path')
    assert result == ['line1', 'line2', 'line3']

    # Test with line_sep as a single character
    result = get_file_lines('dummy_path', line_sep='\n')
    assert result == ['line1', 'line2', 'line3']

    # Test with line_sep as a multi-character string
    mocker.patch('ansible.module_utils.facts.utils.get_file_content', return_value="line1SEPline2SEPline3SEP")
    result = get_file_lines('dummy_path', line_sep='SEP')
    assert result == ['line1', 'line2', 'line3', '']

    # Test with empty data
    mocker.patch('ansible.module_utils.facts.utils.get_file_content', return_value="")
    result = get_file_lines('dummy_path')
    assert result == []

    # Test with strip=False
    mocker.patch('ansible.module_utils.facts.utils.get_file_content', return_value=" line1 \n line2 \n line3 \n")
    result = get_file_lines('dummy_path', strip=False)
    assert result == [' line1 ', ' line2 ', ' line3 ']
