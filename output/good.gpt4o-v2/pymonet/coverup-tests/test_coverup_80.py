# file: pymonet/box.py:59-68
# asked: {"lines": [59, 66, 68], "branches": []}
# gained: {"lines": [59, 66, 68], "branches": []}

import pytest
from pymonet.box import Box
from pymonet.maybe import Maybe

class TestBox:
    
    def test_to_maybe(self):
        # Create an instance of Box with a value
        box = Box(42)
        
        # Convert Box to Maybe
        maybe = box.to_maybe()
        
        # Assert that the Maybe instance is not nothing and has the correct value
        assert isinstance(maybe, Maybe)
        assert not maybe.is_nothing
        assert maybe.value == 42
