# file: thonny/roughparse.py:632-634
# asked: {"lines": [632, 633, 634], "branches": []}
# gained: {"lines": [632, 633, 634], "branches": []}

import pytest
from thonny.roughparse import RoughParser

class TestRoughParser:
    @pytest.fixture
    def parser(self):
        return RoughParser(indent_width=4, tabwidth=4)

    def test_is_block_opener_true(self, parser, mocker):
        mocker.patch.object(parser, '_study2', return_value=None)
        parser.lastch = ":"
        assert parser.is_block_opener() == True

    def test_is_block_opener_false(self, parser, mocker):
        mocker.patch.object(parser, '_study2', return_value=None)
        parser.lastch = ";"
        assert parser.is_block_opener() == False
