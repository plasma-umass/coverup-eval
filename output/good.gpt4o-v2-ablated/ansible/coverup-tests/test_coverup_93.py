# file: lib/ansible/module_utils/facts/utils.py:63-76
# asked: {"lines": [63, 65, 66, 67, 68, 70, 71, 73, 75, 76], "branches": [[66, 67], [66, 75], [67, 68], [67, 70], [70, 71], [70, 73]]}
# gained: {"lines": [63, 65, 66, 67, 68, 70, 71, 73, 75, 76], "branches": [[66, 67], [66, 75], [67, 68], [67, 70], [70, 71], [70, 73]]}

import pytest
from unittest.mock import mock_open, patch

# Assuming get_file_content is defined elsewhere in the module
from ansible.module_utils.facts.utils import get_file_lines

@pytest.fixture
def mock_get_file_content(monkeypatch):
    def _mock_get_file_content(return_value):
        def mock_function(path, strip=True):
            return return_value
        monkeypatch.setattr('ansible.module_utils.facts.utils.get_file_content', mock_function)
    return _mock_get_file_content

def test_get_file_lines_with_data_and_default_sep(mock_get_file_content):
    mock_get_file_content("line1\nline2\nline3")
    result = get_file_lines("dummy_path")
    assert result == ["line1", "line2", "line3"]

def test_get_file_lines_with_data_and_custom_sep(mock_get_file_content):
    mock_get_file_content("line1,line2,line3")
    result = get_file_lines("dummy_path", line_sep=",")
    assert result == ["line1", "line2", "line3"]

def test_get_file_lines_with_data_and_custom_sep_multiple_chars(mock_get_file_content):
    mock_get_file_content("line1--line2--line3")
    result = get_file_lines("dummy_path", line_sep="--")
    assert result == ["line1", "line2", "line3"]

def test_get_file_lines_with_empty_data(mock_get_file_content):
    mock_get_file_content("")
    result = get_file_lines("dummy_path")
    assert result == []

def test_get_file_lines_with_none_data(mock_get_file_content):
    mock_get_file_content(None)
    result = get_file_lines("dummy_path")
    assert result == []
