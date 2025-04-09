# file: flutils/txtutils.py:213-215
# asked: {"lines": [213, 214, 215], "branches": []}
# gained: {"lines": [213, 214, 215], "branches": []}

import pytest
from textwrap import TextWrapper
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_initial_indent():
    wrapper = AnsiTextWrapper()
    wrapper._AnsiTextWrapper__initial_indent = '>> '
    assert wrapper.initial_indent == '>> '

def test_ansi_text_wrapper_initial_indent_default():
    wrapper = AnsiTextWrapper()
    wrapper._AnsiTextWrapper__initial_indent = ''
    assert wrapper.initial_indent == ''
