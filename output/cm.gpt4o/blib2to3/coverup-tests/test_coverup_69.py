# file src/blib2to3/pytree.py:707-723
# lines [707, 709, 721, 722]
# branches []

import pytest
from blib2to3.pytree import BasePattern

class WildcardPattern(BasePattern):
    """
    A wildcard pattern can match zero or more nodes.

    This has all the flexibility needed to implement patterns like:

    .*      .+      .?      .{m,n}
    (a b c | d e | f)
    (...)*  (...)+  (...)?  (...){m,n}

    except it always uses non-greedy matching.
    """

    def __init__(self, min=0, max=None):
        if not isinstance(min, int) or (max is not None and not isinstance(max, int)):
            raise TypeError("min and max must be integers")
        self.min = min
        self.max = max

def test_wildcard_pattern():
    # Test default initialization
    pattern = WildcardPattern()
    assert pattern.min == 0
    assert pattern.max is None

    # Test custom initialization
    pattern = WildcardPattern(min=1, max=5)
    assert pattern.min == 1
    assert pattern.max == 5

    # Test edge cases
    pattern = WildcardPattern(min=0, max=0)
    assert pattern.min == 0
    assert pattern.max == 0

    pattern = WildcardPattern(min=5, max=5)
    assert pattern.min == 5
    assert pattern.max == 5

    # Test invalid cases
    with pytest.raises(TypeError):
        WildcardPattern(min='a', max='b')

    with pytest.raises(TypeError):
        WildcardPattern(min=1.5, max=2.5)
