# file: pymonet/maybe.py:140-151
# asked: {"lines": [140, 147, 149, 150, 151], "branches": [[149, 150], [149, 151]]}
# gained: {"lines": [140, 147, 149, 150, 151], "branches": [[149, 150], [149, 151]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.lazy import Lazy

def test_to_lazy_with_nothing():
    maybe_nothing = Maybe.nothing()
    lazy_result = maybe_nothing.to_lazy()
    
    assert isinstance(lazy_result, Lazy)
    assert lazy_result.get() is None

def test_to_lazy_with_value():
    maybe_just = Maybe.just(42)
    lazy_result = maybe_just.to_lazy()
    
    assert isinstance(lazy_result, Lazy)
    assert lazy_result.get() == 42
