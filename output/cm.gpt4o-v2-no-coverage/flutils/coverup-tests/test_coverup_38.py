# file: flutils/txtutils.py:261-271
# asked: {"lines": [261, 263, 271], "branches": []}
# gained: {"lines": [261, 263, 271], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper
import re

# Mock _ANSI_RE for testing purposes
_ANSI_RE = re.compile(r'\x1b\[[0-9;]*m')

def test_ansi_text_wrapper_split():
    wrapper = AnsiTextWrapper()
    
    # Test with text containing ANSI codes
    text = "\x1b[31mHello\x1b[0m \x1b[32mWorld\x1b[0m"
    expected_chunks = ["\x1b[31m", "Hello", "\x1b[0m", " ", "\x1b[32m", "World", "\x1b[0m"]
    result = wrapper._split(text)
    assert result == expected_chunks, f"Expected {expected_chunks}, but got {result}"
    
    # Test with text without ANSI codes
    text = "Hello World"
    expected_chunks = ["Hello", " ", "World"]
    result = wrapper._split(text)
    assert result == expected_chunks, f"Expected {expected_chunks}, but got {result}"
    
    # Test with empty text
    text = ""
    expected_chunks = []
    result = wrapper._split(text)
    assert result == expected_chunks, f"Expected {expected_chunks}, but got {result}"
