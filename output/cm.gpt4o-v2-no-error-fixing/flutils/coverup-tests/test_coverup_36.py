# file: flutils/txtutils.py:261-271
# asked: {"lines": [261, 263, 271], "branches": []}
# gained: {"lines": [261, 263, 271], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper
import re

_ANSI_RE = re.compile('(\x1b\\[[0-9;:]+[ABCDEFGHJKSTfhilmns])')

def test_ansi_text_wrapper_split():
    text = "\x1b[31mHello\x1b[0m World"
    wrapper = AnsiTextWrapper()
    
    result = wrapper._split(text)
    
    expected = ['\x1b[31m', 'Hello', '\x1b[0m', ' ', 'World']
    assert result == expected, f"Expected {expected}, but got {result}"
