# file src/blib2to3/pytree.py:538-544
# lines [538, 544]
# branches []

import pytest
from blib2to3.pytree import BasePattern

class DerivedPattern(BasePattern):
    pass

def test_base_pattern_optimize():
    pattern = DerivedPattern()
    optimized_pattern = pattern.optimize()
    assert optimized_pattern is pattern, "Optimize should return self for DerivedPattern"
