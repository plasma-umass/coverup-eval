# file: src/blib2to3/pgen2/tokenize.py:196-212
# asked: {"lines": [209, 210, 211, 212], "branches": []}
# gained: {"lines": [209, 210, 211, 212], "branches": []}

import pytest
from blib2to3.pgen2.tokenize import tokenize, StopTokenizing

def test_tokenize_stop_tokenizing(monkeypatch):
    def mock_readline():
        return "print('Hello, world!')\n"

    def mock_tokeneater(*args):
        raise StopTokenizing

    with monkeypatch.context() as m:
        m.setattr('blib2to3.pgen2.tokenize.tokenize_loop', mock_tokeneater)
        try:
            tokenize(mock_readline, mock_tokeneater)
        except StopTokenizing:
            pytest.fail("StopTokenizing was not handled inside tokenize")

    # Ensure no exceptions were raised and the StopTokenizing was handled
    assert True
