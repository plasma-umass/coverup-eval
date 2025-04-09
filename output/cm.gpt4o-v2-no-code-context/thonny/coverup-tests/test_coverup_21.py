# file: thonny/roughparse.py:621-628
# asked: {"lines": [621, 622, 623, 624, 625, 626, 627, 628], "branches": [[626, 627], [626, 628]]}
# gained: {"lines": [621, 622, 623, 624, 625, 626, 627, 628], "branches": [[626, 627], [626, 628]]}

import pytest
from thonny.roughparse import RoughParser

class TestRoughParser:
    @pytest.fixture
    def parser(self, monkeypatch):
        parser = RoughParser(indent_width=4, tabwidth=4)
        parser.stmt_start = 0
        parser.stmt_end = 10
        parser.str = '    indented line'
        return parser

    def test_get_base_indent_string(self, parser):
        def mock_study2():
            pass

        parser._study2 = mock_study2
        result = parser.get_base_indent_string()
        assert result == '    '
