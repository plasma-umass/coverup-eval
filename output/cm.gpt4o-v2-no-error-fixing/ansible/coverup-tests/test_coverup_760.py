# file: lib/ansible/module_utils/facts/utils.py:63-76
# asked: {"lines": [65, 66, 67, 68, 70, 71, 73, 75, 76], "branches": [[66, 67], [66, 75], [67, 68], [67, 70], [70, 71], [70, 73]]}
# gained: {"lines": [65, 66, 67, 68, 70, 71, 73, 75, 76], "branches": [[66, 67], [66, 75], [67, 68], [67, 70], [70, 71], [70, 73]]}

import pytest
from unittest import mock
from ansible.module_utils.facts.utils import get_file_lines

def test_get_file_lines_no_data(monkeypatch):
    def mock_get_file_content(path, strip=True):
        return None

    monkeypatch.setattr('ansible.module_utils.facts.utils.get_file_content', mock_get_file_content)
    result = get_file_lines('dummy_path')
    assert result == []

def test_get_file_lines_default_sep(monkeypatch):
    def mock_get_file_content(path, strip=True):
        return "line1\nline2\nline3"

    monkeypatch.setattr('ansible.module_utils.facts.utils.get_file_content', mock_get_file_content)
    result = get_file_lines('dummy_path')
    assert result == ["line1", "line2", "line3"]

def test_get_file_lines_custom_sep_single_char(monkeypatch):
    def mock_get_file_content(path, strip=True):
        return "line1,line2,line3,"

    monkeypatch.setattr('ansible.module_utils.facts.utils.get_file_content', mock_get_file_content)
    result = get_file_lines('dummy_path', line_sep=',')
    assert result == ["line1", "line2", "line3"]

def test_get_file_lines_custom_sep_multi_char(monkeypatch):
    def mock_get_file_content(path, strip=True):
        return "line1SEPline2SEPline3"

    monkeypatch.setattr('ansible.module_utils.facts.utils.get_file_content', mock_get_file_content)
    result = get_file_lines('dummy_path', line_sep='SEP')
    assert result == ["line1", "line2", "line3"]
