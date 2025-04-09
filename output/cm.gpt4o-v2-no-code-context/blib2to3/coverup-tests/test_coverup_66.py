# file: src/blib2to3/pytree.py:538-544
# asked: {"lines": [538, 544], "branches": []}
# gained: {"lines": [538, 544], "branches": []}

import pytest
from blib2to3.pytree import BasePattern

class TestBasePattern:
    def test_optimize(self, monkeypatch):
        # Create a subclass of BasePattern to test the optimize method
        class SubPattern(BasePattern):
            pass

        sub_pattern = SubPattern()
        optimized_pattern = sub_pattern.optimize()
        
        # Assert that the optimize method returns self
        assert optimized_pattern is sub_pattern
