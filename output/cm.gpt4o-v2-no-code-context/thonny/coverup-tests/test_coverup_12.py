# file: thonny/roughparse.py:392-394
# asked: {"lines": [392, 393, 394], "branches": []}
# gained: {"lines": [392, 393, 394], "branches": []}

import pytest
from thonny.roughparse import RoughParser

class TestRoughParser:
    @pytest.fixture
    def parser(self, mocker):
        parser = RoughParser(indent_width=4, tabwidth=4)
        mocker.patch.object(parser, '_study1')
        parser.continuation = 'test_continuation'
        return parser

    def test_get_continuation_type(self, parser):
        result = parser.get_continuation_type()
        parser._study1.assert_called_once()
        assert result == 'test_continuation'
