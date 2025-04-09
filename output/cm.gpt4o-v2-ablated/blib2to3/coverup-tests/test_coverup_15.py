# file: src/blib2to3/pgen2/tokenize.py:196-212
# asked: {"lines": [196, 209, 210, 211, 212], "branches": []}
# gained: {"lines": [196, 209, 210, 211, 212], "branches": []}

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
    pass

def test_tokenize_normal_case(monkeypatch):
    readline_gen = mock_readline()
    def mock_readline_callable():
        return next(readline_gen, '')

    monkeypatch.setattr('blib2to3.pgen2.tokenize.printtoken', mock_tokeneater)
    tokenize(mock_readline_callable, mock_tokeneater)

def test_tokenize_stop_tokenizing(monkeypatch):
    def mock_readline_callable():
        raise StopTokenizing

    monkeypatch.setattr('blib2to3.pgen2.tokenize.printtoken', mock_tokeneater)
    tokenize(mock_readline_callable, mock_tokeneater)

@pytest.fixture(autouse=True)
def cleanup(monkeypatch):
    yield
    monkeypatch.undo()
