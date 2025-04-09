# file: src/blib2to3/pgen2/tokenize.py:216-218
# asked: {"lines": [216, 217, 218], "branches": [[217, 0], [217, 218]]}
# gained: {"lines": [216, 217, 218], "branches": [[217, 0], [217, 218]]}

import pytest
from blib2to3.pgen2.tokenize import tokenize_loop, generate_tokens
from io import StringIO
import token

def test_tokenize_loop(monkeypatch):
    # Mock readline function
    def mock_readline():
        yield "print('Hello, world!')\n"
        yield ''

    # Mock tokeneater function
    tokens = []
    def mock_tokeneater(type, string, start, end, line):
        tokens.append((type, string, start, end, line))

    # Use the mock readline and tokeneater
    tokenize_loop(mock_readline().__next__, mock_tokeneater)

    # Assertions to verify the postconditions
    assert len(tokens) > 0
    assert tokens[0][0] == token.NAME
    assert tokens[0][1] == 'print'
    assert tokens[-1][0] == token.ENDMARKER

    # Clean up
    tokens.clear()

