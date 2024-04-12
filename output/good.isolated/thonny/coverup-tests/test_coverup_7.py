# file thonny/roughparse.py:556-559
# lines [556, 557, 558, 559]
# branches []

import pytest
from thonny.roughparse import RoughParser

class TestRoughParser:
    @pytest.fixture
    def mock_rough_parser(self, mocker):
        mocker.patch.object(RoughParser, '_study1')
        parser = RoughParser(indent_width=4, tabwidth=4)
        parser.goodlines = [0, 2]
        return parser

    def test_get_num_lines_in_stmt(self, mock_rough_parser):
        num_lines = mock_rough_parser.get_num_lines_in_stmt()
        assert num_lines == 2
