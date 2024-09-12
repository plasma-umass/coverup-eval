# file: lib/ansible/module_utils/facts/utils.py:63-76
# asked: {"lines": [63, 65, 66, 67, 68, 70, 71, 73, 75, 76], "branches": [[66, 67], [66, 75], [67, 68], [67, 70], [70, 71], [70, 73]]}
# gained: {"lines": [63, 65, 66, 67, 68, 70, 71, 75, 76], "branches": [[66, 67], [66, 75], [67, 68], [67, 70], [70, 71]]}

import pytest
from unittest.mock import mock_open, patch
from ansible.module_utils.facts.utils import get_file_lines

# Mock data for the tests
mock_file_content = "line1\nline2\nline3"
mock_file_content_with_sep = "line1,line2,line3"

@patch('ansible.module_utils.facts.utils.get_file_content', return_value=mock_file_content)
def test_get_file_lines_default(mock_get_file_content):
    result = get_file_lines('dummy_path')
    assert result == ['line1', 'line2', 'line3']

@patch('ansible.module_utils.facts.utils.get_file_content', return_value=mock_file_content)
def test_get_file_lines_custom_sep(mock_get_file_content):
    result = get_file_lines('dummy_path', line_sep='\n')
    assert result == ['line1', 'line2', 'line3']

@patch('ansible.module_utils.facts.utils.get_file_content', return_value=mock_file_content_with_sep)
def test_get_file_lines_single_char_sep(mock_get_file_content):
    result = get_file_lines('dummy_path', line_sep=',')
    assert result == ['line1', 'line2', 'line3']

@patch('ansible.module_utils.facts.utils.get_file_content', return_value=mock_file_content_with_sep)
def test_get_file_lines_multi_char_sep(mock_get_file_content):
    result = get_file_lines('dummy_path', line_sep=',')
    assert result == ['line1', 'line2', 'line3']

@patch('ansible.module_utils.facts.utils.get_file_content', return_value='')
def test_get_file_lines_empty(mock_get_file_content):
    result = get_file_lines('dummy_path')
    assert result == []

