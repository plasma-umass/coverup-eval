# file src/blib2to3/pytree.py:320-327
# lines [320, 321, 325, 326, 327]
# branches ['325->326', '325->327']

import pytest
from blib2to3.pytree import Base

class TestNode:
    class Node(Base):
        @property
        def prefix(self) -> str:
            """
            The whitespace and comments preceding this node in the input.
            """
            if not self.children:
                return ""
            return self.children[0].prefix

    def test_prefix_no_children(self):
        node = self.Node()
        node.children = []
        assert node.prefix == ""

    def test_prefix_with_children(self, mocker):
        node = self.Node()
        child = mocker.Mock()
        child.prefix = " "
        node.children = [child]
        assert node.prefix == " "
