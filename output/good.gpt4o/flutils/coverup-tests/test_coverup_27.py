# file flutils/namedtupleutils.py:181-186
# lines [181, 182, 184, 186]
# branches []

import pytest
from types import SimpleNamespace
from collections import namedtuple
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_with_simplenamespace():
    # Create a SimpleNamespace object
    ns = SimpleNamespace(a=1, b=2)
    
    # Convert SimpleNamespace to NamedTuple
    result = _to_namedtuple(ns)
    
    # Verify the result is a NamedTuple
    assert isinstance(result, tuple)
    assert hasattr(result, '_fields')
    
    # Verify the fields and values
    assert result.a == 1
    assert result.b == 2

    # Clean up (not strictly necessary here, but good practice)
    del ns
    del result
