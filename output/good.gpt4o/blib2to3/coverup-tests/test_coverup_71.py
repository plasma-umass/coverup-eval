# file src/blib2to3/pytree.py:535-536
# lines [535, 536]
# branches []

import pytest
from blib2to3.pytree import BasePattern

class TestPattern(BasePattern):
    def _submatch(self, node, results=None) -> bool:
        return super()._submatch(node, results)

def test_basepattern_submatch():
    test_pattern = TestPattern()
    with pytest.raises(NotImplementedError):
        test_pattern._submatch(None)
