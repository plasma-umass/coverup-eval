# file lib/ansible/module_utils/facts/utils.py:63-76
# lines [63, 65, 66, 67, 68, 70, 71, 73, 75, 76]
# branches ['66->67', '66->75', '67->68', '67->70', '70->71', '70->73']

import pytest
from ansible.module_utils.facts.utils import get_file_lines
from unittest.mock import mock_open, patch

# Test function for get_file_lines with default line_sep
def test_get_file_lines_default_sep(mocker):
    mocker.patch('ansible.module_utils.facts.utils.get_file_content', return_value='line1\nline2\nline3')
    lines = get_file_lines('/fake/path')
    assert lines == ['line1', 'line2', 'line3']

# Test function for get_file_lines with custom line_sep of length 1
def test_get_file_lines_custom_sep_single_char(mocker):
    mocker.patch('ansible.module_utils.facts.utils.get_file_content', return_value='line1;line2;line3')
    lines = get_file_lines('/fake/path', line_sep=';')
    assert lines == ['line1', 'line2', 'line3']

# Test function for get_file_lines with custom line_sep of length greater than 1
def test_get_file_lines_custom_sep_multi_char(mocker):
    mocker.patch('ansible.module_utils.facts.utils.get_file_content', return_value='line1XYZline2XYZline3')
    lines = get_file_lines('/fake/path', line_sep='XYZ')
    assert lines == ['line1', 'line2', 'line3']

# Test function for get_file_lines with empty file
def test_get_file_lines_empty_file(mocker):
    mocker.patch('ansible.module_utils.facts.utils.get_file_content', return_value='')
    lines = get_file_lines('/fake/path')
    assert lines == []

# Test function for get_file_lines with None data
def test_get_file_lines_none_data(mocker):
    mocker.patch('ansible.module_utils.facts.utils.get_file_content', return_value=None)
    lines = get_file_lines('/fake/path')
    assert lines == []
