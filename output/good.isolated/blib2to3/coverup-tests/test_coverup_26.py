# file src/blib2to3/pytree.py:501-522
# lines [501, 503, 518, 519, 520, 521]
# branches []

import pytest
from blib2to3.pytree import BasePattern

class ConcreteBasePattern(BasePattern):
    def __init__(self, type=None, content=None, name=None):
        self.type = type
        self.content = content
        self.name = name

    def match(self, node):
        return True

def test_base_pattern_initialization():
    pattern = ConcreteBasePattern(type=256, content="test_content", name="test_name")
    assert pattern.type == 256
    assert pattern.content == "test_content"
    assert pattern.name == "test_name"

def test_base_pattern_default_initialization():
    pattern = ConcreteBasePattern()
    assert pattern.type is None
    assert pattern.content is None
    assert pattern.name is None
