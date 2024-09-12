# file: flutils/namedtupleutils.py:181-186
# asked: {"lines": [181, 182, 184, 186], "branches": []}
# gained: {"lines": [181, 182, 184, 186], "branches": []}

import pytest
from types import SimpleNamespace
from collections import namedtuple
from flutils.namedtupleutils import _to_namedtuple

def test_to_namedtuple_with_simplenamespace():
    # Create a SimpleNamespace object
    ns = SimpleNamespace(a=1, b=2)
    
    # Convert to namedtuple
    result = _to_namedtuple(ns)
    
    # Verify the result is a namedtuple
    assert isinstance(result, tuple)
    assert hasattr(result, '_fields')
    
    # Verify the fields and values
    assert result.a == 1
    assert result.b == 2

def test_to_namedtuple_with_empty_simplenamespace():
    # Create an empty SimpleNamespace object
    ns = SimpleNamespace()
    
    # Convert to namedtuple
    result = _to_namedtuple(ns)
    
    # Verify the result is a namedtuple
    assert isinstance(result, tuple)
    assert hasattr(result, '_fields')
    
    # Verify there are no fields
    assert result._fields == ()
