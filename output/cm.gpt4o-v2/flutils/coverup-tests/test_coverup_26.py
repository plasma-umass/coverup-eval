# file: flutils/txtutils.py:213-215
# asked: {"lines": [213, 214, 215], "branches": []}
# gained: {"lines": [213, 214, 215], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_ansi_text_wrapper_initial_indent():
    wrapper = AnsiTextWrapper(initial_indent='>>')
    assert wrapper.initial_indent == '>>'
    assert wrapper.initial_indent == wrapper._AnsiTextWrapper__initial_indent
