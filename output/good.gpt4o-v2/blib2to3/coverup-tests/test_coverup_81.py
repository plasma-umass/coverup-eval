# file: src/blib2to3/pytree.py:724-766
# asked: {"lines": [759], "branches": [[754, 763]]}
# gained: {"lines": [759], "branches": []}

import pytest
from blib2to3.pytree import WildcardPattern

HUGE = 2**31 - 1  # Assuming HUGE is a large constant, typically used in such contexts

def test_wildcardpattern_with_content():
    content = [['a', 'b'], ['c', 'd']]
    pattern = WildcardPattern(content=content)
    assert pattern.content == (('a', 'b'), ('c', 'd'))
    assert pattern.min == 0
    assert pattern.max == HUGE
    assert pattern.name is None

def test_wildcardpattern_empty_content():
    content = []
    with pytest.raises(AssertionError):
        WildcardPattern(content=content)

def test_wildcardpattern_with_min_max():
    content = [['a', 'b']]
    pattern = WildcardPattern(content=content, min=1, max=2)
    assert pattern.content == (('a', 'b'),)
    assert pattern.min == 1
    assert pattern.max == 2
    assert pattern.name is None
