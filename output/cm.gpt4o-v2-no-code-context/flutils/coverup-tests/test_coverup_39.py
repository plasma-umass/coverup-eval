# file: flutils/txtutils.py:261-271
# asked: {"lines": [261, 263, 271], "branches": []}
# gained: {"lines": [261, 263, 271], "branches": []}

import pytest
from flutils.txtutils import AnsiTextWrapper
from textwrap import TextWrapper
import re

_ANSI_RE = re.compile(r'\x1b\[[0-9;]*m')

@pytest.fixture
def ansi_text_wrapper():
    return AnsiTextWrapper()

def test_ansi_text_wrapper_split(ansi_text_wrapper):
    text = "This is a \x1b[31mred\x1b[0m text"
    expected_output = ['This', ' ', 'is', ' ', 'a', ' ', '\x1b[31m', 'red', '\x1b[0m', ' ', 'text']
    
    result = ansi_text_wrapper._split(text)
    
    assert result == expected_output

def test_ansi_text_wrapper_split_no_ansi(ansi_text_wrapper):
    text = "This is a plain text"
    expected_output = ['This', ' ', 'is', ' ', 'a', ' ', 'plain', ' ', 'text']
    
    result = ansi_text_wrapper._split(text)
    
    assert result == expected_output

def test_ansi_text_wrapper_split_only_ansi(ansi_text_wrapper):
    text = "\x1b[31m\x1b[0m"
    expected_output = ['\x1b[31m', '\x1b[0m']
    
    result = ansi_text_wrapper._split(text)
    
    assert result == expected_output
