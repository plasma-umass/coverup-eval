# file: src/blib2to3/pytree.py:523-526
# asked: {"lines": [523, 525, 526], "branches": []}
# gained: {"lines": [523, 525], "branches": []}

import pytest
from blib2to3.pytree import BasePattern

def test_basepattern_instantiation():
    with pytest.raises(AssertionError, match="Cannot instantiate BasePattern"):
        BasePattern()
