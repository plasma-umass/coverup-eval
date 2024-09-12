# file: thonny/roughparse.py:638-640
# asked: {"lines": [638, 639, 640], "branches": []}
# gained: {"lines": [638, 639, 640], "branches": []}

import pytest
from thonny.roughparse import RoughParser

class MockRoughParser(RoughParser):
    def __init__(self, str_value, stmt_start):
        self.str = str_value
        self.stmt_start = stmt_start

    def _study2(self):
        pass

def _closere(string, start):
    # Mock implementation of _closere
    if string[start:] == "end":
        return True
    return None

@pytest.fixture
def mock_rough_parser(monkeypatch):
    monkeypatch.setattr("thonny.roughparse._closere", _closere)
    return MockRoughParser

def test_is_block_closer_true(mock_rough_parser):
    parser = mock_rough_parser("end", 0)
    assert parser.is_block_closer() is True

def test_is_block_closer_false(mock_rough_parser):
    parser = mock_rough_parser("not_end", 0)
    assert parser.is_block_closer() is False
