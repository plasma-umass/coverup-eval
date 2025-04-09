# file src/blib2to3/pytree.py:523-526
# lines [523, 525, 526]
# branches []

import pytest
from blib2to3.pytree import BasePattern

def test_base_pattern_instantiation_error():
    with pytest.raises(AssertionError) as excinfo:
        BasePattern()
    assert str(excinfo.value) == "Cannot instantiate BasePattern"
