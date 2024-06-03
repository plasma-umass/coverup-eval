# file thonny/roughparse.py:392-394
# lines [392, 393, 394]
# branches []

import pytest
from thonny.roughparse import RoughParser

class TestRoughParser:
    def test_get_continuation_type(self, mocker):
        # Mock the _study1 method to set the continuation attribute
        parser = RoughParser(indent_width=4, tabwidth=4)
        mocker.patch.object(parser, '_study1', return_value=None)
        parser.continuation = "some_continuation_type"
        
        result = parser.get_continuation_type()
        
        assert result == "some_continuation_type"
