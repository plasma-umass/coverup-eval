# file: src/blib2to3/pgen2/tokenize.py:216-218
# asked: {"lines": [216, 217, 218], "branches": [[217, 0], [217, 218]]}
# gained: {"lines": [216, 217, 218], "branches": [[217, 0], [217, 218]]}

import pytest
from blib2to3.pgen2.tokenize import tokenize_loop, generate_tokens
from io import StringIO

def test_tokenize_loop():
    def mock_readline():
        lines = [
            "def foo():\n",
            "    return 42\n"
        ]
        for line in lines:
            yield line

    def mock_tokeneater(type, token, start, end, line):
        assert isinstance(type, int)
        assert isinstance(token, str)
        assert isinstance(start, tuple)
        assert isinstance(end, tuple)
        assert isinstance(line, str)

    readline = mock_readline().__next__
    tokenize_loop(readline, mock_tokeneater)

