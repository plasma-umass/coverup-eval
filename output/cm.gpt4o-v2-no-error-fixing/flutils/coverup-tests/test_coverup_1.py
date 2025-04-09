# file: flutils/txtutils.py:223-227
# asked: {"lines": [223, 224, 225, 226, 227], "branches": [[225, 226], [225, 227]]}
# gained: {"lines": [223, 224, 225, 226, 227], "branches": [[225, 226], [225, 227]]}

import pytest
from flutils.txtutils import AnsiTextWrapper

def test_initial_indent_len_with_indent():
    wrapper = AnsiTextWrapper(initial_indent='    ')
    assert wrapper.initial_indent_len == 4

def test_initial_indent_len_without_indent():
    wrapper = AnsiTextWrapper(initial_indent='')
    assert wrapper.initial_indent_len == 0
