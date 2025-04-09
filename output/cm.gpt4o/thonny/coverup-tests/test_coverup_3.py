# file thonny/roughparse.py:556-559
# lines [556, 557, 558, 559]
# branches []

import pytest
from thonny.roughparse import RoughParser

class MockRoughParser(RoughParser):
    def __init__(self, goodlines):
        self.goodlines = goodlines

    def _study1(self):
        pass

def test_get_num_lines_in_stmt():
    parser = MockRoughParser(goodlines=[1, 2, 3, 5])
    result = parser.get_num_lines_in_stmt()
    assert result == 2  # 5 - 3 = 2
