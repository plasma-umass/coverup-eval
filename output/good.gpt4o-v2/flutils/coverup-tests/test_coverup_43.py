# file: flutils/txtutils.py:261-271
# asked: {"lines": [261, 263, 271], "branches": []}
# gained: {"lines": [261, 263, 271], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper
import re

def test_ansi_text_wrapper_split():
    wrapper = AnsiTextWrapper()
    text = "Hello \x1b[31mWorld\x1b[0m!"
    
    result = wrapper._split(text)
    
    expected = ["Hello", " ", "\x1b[31m", "World", "\x1b[0m", "!"]
    assert result == expected, f"Expected {expected}, but got {result}"
