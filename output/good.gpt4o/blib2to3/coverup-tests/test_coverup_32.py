# file src/blib2to3/pgen2/tokenize.py:196-212
# lines [196, 209, 210, 211, 212]
# branches []

import pytest
from blib2to3.pgen2.tokenize import tokenize, StopTokenizing

def mock_readline():
    lines = [
        "def foo():\n",
        "    return 42\n",
        ""
    ]
    for line in lines:
        yield line

def mock_tokeneater(type, token, start, end, line):
    if token == "return":
        raise StopTokenizing

def test_tokenize_stop_tokenizing():
    readline_gen = mock_readline()
    readline = lambda: next(readline_gen)
    
    # Ensure that StopTokenizing is raised and caught within tokenize
    try:
        tokenize(readline, mock_tokeneater)
    except StopTokenizing:
        pytest.fail("StopTokenizing should be caught within tokenize")

    # No assertions needed as we are testing the control flow and exception handling

