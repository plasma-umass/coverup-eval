# file: thonny/roughparse.py:638-640
# asked: {"lines": [638, 639, 640], "branches": []}
# gained: {"lines": [638, 639, 640], "branches": []}

import pytest
from thonny.roughparse import RoughParser

class MockRoughParser(RoughParser):
    def __init__(self, str, stmt_start):
        self.str = str
        self.stmt_start = stmt_start

    def _study2(self):
        pass

def test_is_block_closer(monkeypatch):
    def mock_closere(s, start):
        return True

    monkeypatch.setattr('thonny.roughparse._closere', mock_closere)

    parser = MockRoughParser("some string", 0)
    result = parser.is_block_closer()
    assert result is True
