# file: lib/ansible/module_utils/facts/utils.py:63-76
# asked: {"lines": [63, 65, 66, 67, 68, 70, 71, 73, 75, 76], "branches": [[66, 67], [66, 75], [67, 68], [67, 70], [70, 71], [70, 73]]}
# gained: {"lines": [63, 65, 66, 67, 68, 70, 71, 73, 75, 76], "branches": [[66, 67], [66, 75], [67, 68], [67, 70], [70, 71], [70, 73]]}

import pytest
from unittest import mock
from ansible.module_utils.facts.utils import get_file_lines

def test_get_file_lines_with_default_separator(monkeypatch):
    mock_content = "line1\nline2\nline3"
    mock_get_file_content = mock.Mock(return_value=mock_content)
    monkeypatch.setattr('ansible.module_utils.facts.utils.get_file_content', mock_get_file_content)
    
    result = get_file_lines('dummy_path')
    assert result == ['line1', 'line2', 'line3']

def test_get_file_lines_with_custom_separator(monkeypatch):
    mock_content = "line1,line2,line3"
    mock_get_file_content = mock.Mock(return_value=mock_content)
    monkeypatch.setattr('ansible.module_utils.facts.utils.get_file_content', mock_get_file_content)
    
    result = get_file_lines('dummy_path', line_sep=',')
    assert result == ['line1', 'line2', 'line3']

def test_get_file_lines_with_multichar_separator(monkeypatch):
    mock_content = "line1||line2||line3"
    mock_get_file_content = mock.Mock(return_value=mock_content)
    monkeypatch.setattr('ansible.module_utils.facts.utils.get_file_content', mock_get_file_content)
    
    result = get_file_lines('dummy_path', line_sep='||')
    assert result == ['line1', 'line2', 'line3']

def test_get_file_lines_with_empty_content(monkeypatch):
    mock_get_file_content = mock.Mock(return_value='')
    monkeypatch.setattr('ansible.module_utils.facts.utils.get_file_content', mock_get_file_content)
    
    result = get_file_lines('dummy_path')
    assert result == []
