# file src/blib2to3/pytree.py:432-438
# lines [432, 438]
# branches []

import pytest
from blib2to3.pytree import Base

class TestLeaf:
    def test_leaf_str(self):
        class Leaf(Base):
            def __init__(self, prefix, value):
                self._prefix = prefix
                self._value = value

            @property
            def prefix(self):
                return self._prefix

            @property
            def value(self):
                return self._value

            def __str__(self) -> str:
                """
                Return a pretty string representation.

                This reproduces the input source exactly.
                """
                return self.prefix + str(self.value)

        leaf = Leaf(prefix="prefix_", value="value")
        result = str(leaf)
        assert result == "prefix_value"
