# file: flutils/txtutils.py:223-227
# asked: {"lines": [225, 226, 227], "branches": [[225, 226], [225, 227]]}
# gained: {"lines": [225, 226, 227], "branches": [[225, 226], [225, 227]]}

import pytest
from flutils.txtutils import AnsiTextWrapper
from unittest.mock import patch

@pytest.fixture
def mock_len_without_ansi(mocker):
    return mocker.patch('flutils.txtutils.len_without_ansi', return_value=5)

def test_initial_indent_len_no_indent():
    wrapper = AnsiTextWrapper()
    wrapper.initial_indent = ''
    assert wrapper.initial_indent_len == 0

def test_initial_indent_len_with_indent(mock_len_without_ansi):
    wrapper = AnsiTextWrapper()
    wrapper.initial_indent = '    '
    assert wrapper.initial_indent_len == 5
    mock_len_without_ansi.assert_called_once_with('    ')
