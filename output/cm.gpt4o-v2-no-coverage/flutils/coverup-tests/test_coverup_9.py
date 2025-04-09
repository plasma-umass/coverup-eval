# file: flutils/txtutils.py:223-227
# asked: {"lines": [223, 224, 225, 226, 227], "branches": [[225, 226], [225, 227]]}
# gained: {"lines": [223, 224, 225, 226, 227], "branches": [[225, 226], [225, 227]]}

import pytest
from flutils.txtutils import AnsiTextWrapper, len_without_ansi

def test_initial_indent_len_no_indent():
    wrapper = AnsiTextWrapper(initial_indent='')
    assert wrapper.initial_indent_len == 0

def test_initial_indent_len_with_indent():
    wrapper = AnsiTextWrapper(initial_indent='\x1b[31m\x1b[1m\x1b[4mIndent\x1b[0m')
    assert wrapper.initial_indent_len == len_without_ansi('\x1b[31m\x1b[1m\x1b[4mIndent\x1b[0m')

def test_len_without_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
