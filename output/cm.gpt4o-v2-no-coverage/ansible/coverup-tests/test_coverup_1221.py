# file: lib/ansible/module_utils/facts/utils.py:63-76
# asked: {"lines": [73], "branches": [[70, 73]]}
# gained: {"lines": [73], "branches": [[70, 73]]}

import pytest
from unittest.mock import mock_open, patch
from ansible.module_utils.facts.utils import get_file_lines

# Mock for get_file_content
def mock_get_file_content(path, strip=True):
    if path == "empty_file":
        return ""
    elif path == "single_line_file":
        return "single line content"
    elif path == "multi_line_file":
        return "line1\nline2\nline3"
    elif path == "custom_sep_file":
        return "line1|line2|line3"
    return None

@patch('ansible.module_utils.facts.utils.get_file_content', side_effect=mock_get_file_content)
def test_get_file_lines_empty_file(mock_get_file_content):
    result = get_file_lines("empty_file")
    assert result == []

@patch('ansible.module_utils.facts.utils.get_file_content', side_effect=mock_get_file_content)
def test_get_file_lines_single_line(mock_get_file_content):
    result = get_file_lines("single_line_file")
    assert result == ["single line content"]

@patch('ansible.module_utils.facts.utils.get_file_content', side_effect=mock_get_file_content)
def test_get_file_lines_multi_line(mock_get_file_content):
    result = get_file_lines("multi_line_file")
    assert result == ["line1", "line2", "line3"]

@patch('ansible.module_utils.facts.utils.get_file_content', side_effect=mock_get_file_content)
def test_get_file_lines_custom_sep(mock_get_file_content):
    result = get_file_lines("custom_sep_file", line_sep="|")
    assert result == ["line1", "line2", "line3"]

@patch('ansible.module_utils.facts.utils.get_file_content', side_effect=mock_get_file_content)
def test_get_file_lines_custom_sep_multi_char(mock_get_file_content):
    result = get_file_lines("custom_sep_file", line_sep="|line")
    assert result == ["line1", "2", "3"]
