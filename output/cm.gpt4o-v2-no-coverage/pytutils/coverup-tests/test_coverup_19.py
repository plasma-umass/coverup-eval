# file: pytutils/trees.py:59-61
# asked: {"lines": [59, 61], "branches": []}
# gained: {"lines": [59, 61], "branches": []}

import pytest
import collections
from pytutils.trees import tree

def test_tree_creation():
    t = tree()
    assert isinstance(t, collections.defaultdict)
    assert t.default_factory == tree

def test_tree_nested_structure():
    t = tree()
    t['a']['b']['c'] = 'value'
    assert t['a']['b']['c'] == 'value'
    assert isinstance(t['a'], collections.defaultdict)
    assert isinstance(t['a']['b'], collections.defaultdict)
    assert isinstance(t['a']['b']['c'], str)

def test_tree_default_factory():
    t = tree()
    assert t.default_factory == tree
    t['a']
    assert isinstance(t['a'], collections.defaultdict)
    assert t['a'].default_factory == tree
