# file: src/blib2to3/pytree.py:724-766
# asked: {"lines": [759], "branches": [[754, 763]]}
# gained: {"lines": [759], "branches": []}

import pytest
from blib2to3.pytree import WildcardPattern, HUGE

def test_wildcardpattern_with_content():
    content = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h']]
    pattern = WildcardPattern(content=content, min=1, max=2, name="test")
    
    assert pattern.content == (('a', 'b', 'c'), ('d', 'e'), ('f', 'g', 'h'))
    assert pattern.min == 1
    assert pattern.max == 2
    assert pattern.name == "test"

def test_wildcardpattern_empty_content():
    with pytest.raises(AssertionError):
        WildcardPattern(content=[], min=1, max=2, name="test")

def test_wildcardpattern_with_empty_alternative():
    content = [['a', 'b', 'c'], [], ['f', 'g', 'h']]
    with pytest.raises(AssertionError):
        WildcardPattern(content=content, min=1, max=2, name="test")
