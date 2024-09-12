# file: lib/ansible/module_utils/facts/utils.py:63-76
# asked: {"lines": [73], "branches": [[70, 73]]}
# gained: {"lines": [73], "branches": [[70, 73]]}

import pytest
from ansible.module_utils.facts.utils import get_file_lines
from unittest.mock import mock_open, patch

def test_get_file_lines_no_data():
    with patch('ansible.module_utils.facts.utils.get_file_content', return_value=None):
        assert get_file_lines('dummy_path') == []

def test_get_file_lines_default_sep():
    with patch('ansible.module_utils.facts.utils.get_file_content', return_value='line1\nline2\nline3'):
        assert get_file_lines('dummy_path') == ['line1', 'line2', 'line3']

def test_get_file_lines_custom_sep_single_char():
    with patch('ansible.module_utils.facts.utils.get_file_content', return_value='line1,line2,line3'):
        assert get_file_lines('dummy_path', line_sep=',') == ['line1', 'line2', 'line3']

def test_get_file_lines_custom_sep_multi_char():
    with patch('ansible.module_utils.facts.utils.get_file_content', return_value='line1<sep>line2<sep>line3'):
        assert get_file_lines('dummy_path', line_sep='<sep>') == ['line1', 'line2', 'line3']
