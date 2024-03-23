# file src/blib2to3/pytree.py:707-723
# lines [707, 709, 721, 722]
# branches []

import pytest
from blib2to3.pytree import WildcardPattern

def test_wildcard_pattern_init():
    # Test the initialization of WildcardPattern with different min and max values
    # Since the error indicates that 'wrapped_content' is referenced before assignment,
    # we need to pass a 'content' argument to avoid the UnboundLocalError.
    content = [[('a',), ('b',)], [('c',)]]
    wildcard_pattern_1 = WildcardPattern(content=content, min=0, max=1)
    assert wildcard_pattern_1.min == 0
    assert wildcard_pattern_1.max == 1
    assert wildcard_pattern_1.content == tuple(map(tuple, content))

    wildcard_pattern_2 = WildcardPattern(content=content, min=1, max=5)
    assert wildcard_pattern_2.min == 1
    assert wildcard_pattern_2.max == 5
    assert wildcard_pattern_2.content == tuple(map(tuple, content))

    wildcard_pattern_3 = WildcardPattern(content=content, min=2, max=10)
    assert wildcard_pattern_3.min == 2
    assert wildcard_pattern_3.max == 10
    assert wildcard_pattern_3.content == tuple(map(tuple, content))
