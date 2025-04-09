# file: thonny/roughparse.py:236-239
# asked: {"lines": [236, 237, 238, 239], "branches": [[238, 0], [238, 239]]}
# gained: {"lines": [236, 237, 238, 239], "branches": [[238, 0], [238, 239]]}

import pytest
from thonny.roughparse import RoughParser

class TestRoughParser:
    @pytest.fixture
    def parser(self):
        parser = RoughParser(indent_width=4, tabwidth=4)
        parser.str = "line1\nline2\nline3\n"
        return parser

    def test_set_lo_zero(self, parser):
        parser.set_lo(0)
        assert parser.str == "line1\nline2\nline3\n"

    def test_set_lo_non_zero(self, parser):
        parser.set_lo(6)
        assert parser.str == "line2\nline3\n"

    def test_set_lo_assertion_error(self, parser):
        with pytest.raises(AssertionError):
            parser.set_lo(5)
