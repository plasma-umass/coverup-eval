# file: src/blib2to3/pytree.py:535-536
# asked: {"lines": [535, 536], "branches": []}
# gained: {"lines": [535, 536], "branches": []}

import pytest
from blib2to3.pytree import BasePattern

class ConcretePattern(BasePattern):
    def _submatch(self, node, results=None) -> bool:
        return super()._submatch(node, results)

def test_basepattern_submatch():
    pattern = ConcretePattern()
    with pytest.raises(NotImplementedError):
        pattern._submatch(None)
