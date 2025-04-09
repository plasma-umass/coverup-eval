# file: src/blib2to3/pgen2/tokenize.py:196-212
# asked: {"lines": [196, 209, 210, 211, 212], "branches": []}
# gained: {"lines": [196, 209, 210, 211, 212], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import tokenize, StopTokenizing

def mock_readline():
    lines = ["print('Hello, world!')\n", "print('Goodbye, world!')\n", ""]
    def readline():
        return lines.pop(0)
    return readline

def mock_tokeneater(type, token, start, end, line):
    pass

def test_tokenize_normal_execution(monkeypatch):
    readline = mock_readline()
    tokeneater = mock_tokeneater

    # Ensure no exception is raised and function completes
    tokenize(readline, tokeneater)

def test_tokenize_stop_tokenizing(monkeypatch):
    def mock_tokenize_loop(readline, tokeneater):
        raise StopTokenizing

    monkeypatch.setattr('blib2to3.pgen2.tokenize.tokenize_loop', mock_tokenize_loop)

    readline = mock_readline()
    tokeneater = mock_tokeneater

    # Ensure StopTokenizing is caught and function completes
    tokenize(readline, tokeneater)
