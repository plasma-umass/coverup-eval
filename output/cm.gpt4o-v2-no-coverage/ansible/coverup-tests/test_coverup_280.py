# file: lib/ansible/module_utils/facts/utils.py:63-76
# asked: {"lines": [63, 65, 66, 67, 68, 70, 71, 73, 75, 76], "branches": [[66, 67], [66, 75], [67, 68], [67, 70], [70, 71], [70, 73]]}
# gained: {"lines": [63, 65, 66, 67, 68, 70, 71, 75, 76], "branches": [[66, 67], [66, 75], [67, 68], [67, 70], [70, 71]]}

import pytest
from unittest.mock import mock_open, patch
from ansible.module_utils.facts.utils import get_file_lines

# Mocking get_file_content to control its output
@pytest.fixture
def mock_get_file_content(monkeypatch):
    def _mock_get_file_content(path, strip=True):
        if path == "empty_file":
            return ""
        elif path == "single_line_file":
            return "single line content"
        elif path == "multi_line_file":
            return "line1\nline2\nline3"
        elif path == "custom_sep_file":
            return "line1|line2|line3"
        return None

    monkeypatch.setattr("ansible.module_utils.facts.utils.get_file_content", _mock_get_file_content)

def test_get_file_lines_empty_file(mock_get_file_content):
    result = get_file_lines("empty_file")
    assert result == []

def test_get_file_lines_single_line(mock_get_file_content):
    result = get_file_lines("single_line_file")
    assert result == ["single line content"]

def test_get_file_lines_multi_line(mock_get_file_content):
    result = get_file_lines("multi_line_file")
    assert result == ["line1", "line2", "line3"]

def test_get_file_lines_custom_separator(mock_get_file_content):
    result = get_file_lines("custom_sep_file", line_sep="|")
    assert result == ["line1", "line2", "line3"]

def test_get_file_lines_custom_separator_strip(mock_get_file_content):
    result = get_file_lines("custom_sep_file", line_sep="|", strip=True)
    assert result == ["line1", "line2", "line3"]

def test_get_file_lines_custom_separator_no_strip(mock_get_file_content):
    result = get_file_lines("custom_sep_file", line_sep="|", strip=False)
    assert result == ["line1", "line2", "line3"]
