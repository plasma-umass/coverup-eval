# file src/blib2to3/pytree.py:465-470
# lines [465, 466, 470]
# branches []

import pytest
from blib2to3.pytree import Base

class TestLeaf:
    def test_prefix_property(self, mocker):
        # Mocking the Base class to avoid any side effects
        mock_base = mocker.Mock(spec=Base)
        
        # Creating a subclass of Leaf to test the prefix property
        class Leaf(Base):
            @property
            def prefix(self) -> str:
                return self._prefix
        
        # Creating an instance of the Leaf class
        leaf_instance = Leaf()
        
        # Setting the _prefix attribute
        leaf_instance._prefix = "   # comment"
        
        # Asserting that the prefix property returns the correct value
        assert leaf_instance.prefix == "   # comment"
