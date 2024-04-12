# file src/blib2to3/pytree.py:535-536
# lines [535, 536]
# branches []

import pytest
from blib2to3.pytree import BasePattern

class ConcreteBasePattern(BasePattern):
    def _submatch(self, node, results=None) -> bool:
        return super()._submatch(node, results)

class TestBasePattern:
    def test_submatch_not_implemented(self):
        pattern = ConcreteBasePattern()
        with pytest.raises(NotImplementedError):
            pattern._submatch(None)
