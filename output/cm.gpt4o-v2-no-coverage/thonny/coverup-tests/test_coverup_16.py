# file: thonny/roughparse.py:645-647
# asked: {"lines": [645, 646, 647], "branches": []}
# gained: {"lines": [645, 646, 647], "branches": []}

import pytest
from thonny.roughparse import RoughParser

class TestRoughParser:
    
    def test_get_last_open_bracket_pos(self, mocker):
        parser = RoughParser(indent_width=4, tabwidth=4)
        
        # Mocking the _study2 method to control its behavior
        mocker.patch.object(parser, '_study2', autospec=True)
        
        # Setting up the necessary attributes for the test
        parser.lastopenbracketpos = 5
        
        # Call the method
        result = parser.get_last_open_bracket_pos()
        
        # Assertions
        parser._study2.assert_called_once()
        assert result == 5
