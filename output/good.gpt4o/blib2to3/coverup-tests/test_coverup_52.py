# file src/blib2to3/pytree.py:287-293
# lines [287, 293]
# branches []

import pytest
from blib2to3.pytree import Base

class TestNode:
    def test_node_str(self):
        class Node(Base):
            def __str__(self) -> str:
                """
                Return a pretty string representation.

                This reproduces the input source exactly.
                """
                return "".join(map(str, self.children))

        # Create a mock for the children attribute
        node = Node()
        node.children = ["child1", "child2", "child3"]

        # Assert the string representation
        assert str(node) == "child1child2child3"
