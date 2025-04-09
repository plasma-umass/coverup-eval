# file: src/blib2to3/pytree.py:538-544
# asked: {"lines": [538, 544], "branches": []}
# gained: {"lines": [538, 544], "branches": []}

import pytest
from blib2to3.pytree import BasePattern

def test_basepattern_optimize():
    class TestPattern(BasePattern):
        pass

    pattern = TestPattern()
    optimized_pattern = pattern.optimize()
    
    assert optimized_pattern is pattern
