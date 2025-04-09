# file thonny/roughparse.py:632-634
# lines [632, 633, 634]
# branches []

import pytest
from thonny.roughparse import RoughParser

class TestRoughParser:
    def test_is_block_opener_with_colon(self, mocker):
        # Set up the RoughParser instance with required arguments
        parser = RoughParser(indent_width=4, tabwidth=4)
        
        # Mock the _study2 method to not do anything
        mocker.patch.object(parser, '_study2')
        
        # Set lastch to ':' to simulate a block opener
        parser.lastch = ':'
        
        # Assert that is_block_opener returns True when lastch is ':'
        assert parser.is_block_opener() == True

    def test_is_block_opener_without_colon(self, mocker):
        # Set up the RoughParser instance with required arguments
        parser = RoughParser(indent_width=4, tabwidth=4)
        
        # Mock the _study2 method to not do anything
        mocker.patch.object(parser, '_study2')
        
        # Set lastch to a different character to simulate not a block opener
        parser.lastch = 'a'
        
        # Assert that is_block_opener returns False when lastch is not ':'
        assert parser.is_block_opener() == False
