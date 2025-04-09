# file: flutils/txtutils.py:239-243
# asked: {"lines": [239, 240, 241, 242, 243], "branches": [[241, 242], [241, 243]]}
# gained: {"lines": [239, 240, 241, 242, 243], "branches": [[241, 242], [241, 243]]}

import pytest
from flutils.txtutils import AnsiTextWrapper, len_without_ansi

def test_subsequent_indent_len_no_indent():
    wrapper = AnsiTextWrapper()
    assert wrapper.subsequent_indent_len == 0

def test_subsequent_indent_len_with_indent():
    wrapper = AnsiTextWrapper(subsequent_indent='    ')
    assert wrapper.subsequent_indent_len == 4

def test_len_without_ansi_no_ansi():
    text = "foobar"
    assert len_without_ansi(text) == 6

def test_len_without_ansi_with_ansi():
    text = '\x1b[38;5;209mfoobar\x1b[0m'
    assert len_without_ansi(text) == 6
