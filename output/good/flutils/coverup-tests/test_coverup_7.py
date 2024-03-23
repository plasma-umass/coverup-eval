# file flutils/txtutils.py:239-243
# lines [239, 240, 241, 242, 243]
# branches ['241->242', '241->243']

import pytest
from flutils.txtutils import AnsiTextWrapper, len_without_ansi

def test_subsequent_indent_len_no_indent():
    wrapper = AnsiTextWrapper()
    assert wrapper.subsequent_indent_len == 0

def test_subsequent_indent_len_with_ansi_indent(mocker):
    # Mock the len_without_ansi function to control its output
    mocker.patch('flutils.txtutils.len_without_ansi', return_value=10)
    wrapper = AnsiTextWrapper()
    wrapper.subsequent_indent = '\x1b[1;32m    \x1b[0m'  # ANSI colored spaces
    assert wrapper.subsequent_indent_len == 10
