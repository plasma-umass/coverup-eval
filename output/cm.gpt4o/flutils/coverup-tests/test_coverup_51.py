# file flutils/txtutils.py:261-271
# lines [261, 263, 271]
# branches []

import pytest
from flutils.txtutils import AnsiTextWrapper
import re
from textwrap import TextWrapper

_ANSI_RE = re.compile(r'\x1b\[[0-9;]*m')

def test_ansi_text_wrapper_split():
    wrapper = AnsiTextWrapper()
    text = "This is a \x1b[31mred\x1b[0m text"
    expected_output = ['This', ' ', 'is', ' ', 'a', ' ', 'red', ' ', 'text']
    
    result = [chunk for chunk in wrapper._split(text) if not _ANSI_RE.match(chunk)]
    
    assert result == expected_output, f"Expected {expected_output}, but got {result}"
