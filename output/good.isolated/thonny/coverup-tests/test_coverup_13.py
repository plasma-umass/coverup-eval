# file thonny/roughparse.py:392-394
# lines [392, 393, 394]
# branches []

import pytest
from thonny.roughparse import RoughParser

# Assuming the existence of a RoughParser class with the method get_continuation_type
# and a private method _study1 which sets the attribute 'continuation'
# and that RoughParser requires 'indent_width' and 'tabwidth' arguments for initialization

class TestRoughParser:
    def test_get_continuation_type(self, mocker):
        # Mock the _study1 method to set the continuation attribute
        mocker.patch.object(RoughParser, '_study1', autospec=True)
        
        # Create an instance of RoughParser with required arguments
        parser = RoughParser(indent_width=4, tabwidth=8)
        
        # Set a known value for continuation
        parser.continuation = "expected_continuation"
        
        # Call the method under test
        continuation = parser.get_continuation_type()
        
        # Assert that the mocked _study1 method was called
        parser._study1.assert_called_once_with(parser)
        
        # Assert that the continuation type returned is as expected
        assert continuation == "expected_continuation"
