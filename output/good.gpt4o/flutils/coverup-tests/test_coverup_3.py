# file flutils/txtutils.py:223-227
# lines [223, 224, 225, 226, 227]
# branches ['225->226', '225->227']

import pytest
from flutils.txtutils import AnsiTextWrapper
from unittest.mock import patch

def test_ansi_text_wrapper_initial_indent_len_no_indent():
    wrapper = AnsiTextWrapper(initial_indent='')
    assert wrapper.initial_indent_len == 0

def test_ansi_text_wrapper_initial_indent_len_with_indent(mocker):
    mock_len_without_ansi = mocker.patch('flutils.txtutils.len_without_ansi', return_value=5)
    wrapper = AnsiTextWrapper(initial_indent='    ')
    assert wrapper.initial_indent_len == 5
    mock_len_without_ansi.assert_called_once_with('    ')
