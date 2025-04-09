# file thonny/roughparse.py:638-640
# lines [638, 639, 640]
# branches []

import pytest
from thonny.roughparse import RoughParser

class MockRoughParser(RoughParser):
    def __init__(self, string, stmt_start):
        self.str = string
        self.stmt_start = stmt_start

    def _study2(self):
        pass

def test_is_block_closer(mocker):
    mocker.patch('thonny.roughparse._closere', return_value=True)
    parser = MockRoughParser("some string", 0)
    assert parser.is_block_closer() is True

    mocker.patch('thonny.roughparse._closere', return_value=None)
    parser = MockRoughParser("some string", 0)
    assert parser.is_block_closer() is False
