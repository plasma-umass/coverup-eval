# file thonny/roughparse.py:621-628
# lines [621, 622, 623, 624, 625, 626, 627, 628]
# branches ['626->627', '626->628']

import pytest
from thonny.roughparse import RoughParser

class MockRoughParser(RoughParser):
    def __init__(self, stmt_start, stmt_end, str_):
        self.stmt_start = stmt_start
        self.stmt_end = stmt_end
        self.str = str_

    def _study2(self):
        pass

@pytest.fixture
def mock_rough_parser():
    return MockRoughParser(stmt_start=0, stmt_end=10, str_="    def test():\n")

def test_get_base_indent_string(mock_rough_parser):
    result = mock_rough_parser.get_base_indent_string()
    assert result == "    "
