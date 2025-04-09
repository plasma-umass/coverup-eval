# file: src/blib2to3/pytree.py:192-204
# asked: {"lines": [192, 193, 198, 199, 201, 202, 203, 204], "branches": [[198, 199], [198, 201], [201, 202], [201, 203]]}
# gained: {"lines": [192, 193, 198, 199, 201, 202, 203, 204], "branches": [[198, 199], [198, 201], [201, 202], [201, 203]]}

import pytest
from blib2to3.pytree import Base, Node

class MockParent:
    def __init__(self):
        self.next_sibling_map = None

    def update_sibling_maps(self):
        self.next_sibling_map = {id(self.child): self.sibling}

class MockNode(Base):
    def __init__(self, parent=None):
        self.parent = parent

def test_next_sibling_no_parent():
    node = MockNode()
    assert node.next_sibling is None

def test_next_sibling_no_sibling_map(monkeypatch):
    parent = MockParent()
    node = MockNode(parent)
    sibling = MockNode(parent)
    parent.child = node
    parent.sibling = sibling

    assert node.next_sibling is sibling

def test_next_sibling_with_sibling_map(monkeypatch):
    parent = MockParent()
    node = MockNode(parent)
    sibling = MockNode(parent)
    parent.child = node
    parent.sibling = sibling
    parent.update_sibling_maps()

    assert node.next_sibling is sibling
