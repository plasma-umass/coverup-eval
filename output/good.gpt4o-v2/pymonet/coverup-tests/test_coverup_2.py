# file: pymonet/maybe.py:140-151
# asked: {"lines": [140, 147, 149, 150, 151], "branches": [[149, 150], [149, 151]]}
# gained: {"lines": [140, 147, 149, 150, 151], "branches": [[149, 150], [149, 151]]}

import pytest
from pymonet.maybe import Maybe
from pymonet.lazy import Lazy

def test_maybe_to_lazy_with_value():
    maybe = Maybe.just(10)
    lazy_result = maybe.to_lazy()
    assert isinstance(lazy_result, Lazy)
    assert lazy_result.get() == 10

def test_maybe_to_lazy_with_nothing():
    maybe = Maybe.nothing()
    lazy_result = maybe.to_lazy()
    assert isinstance(lazy_result, Lazy)
    assert lazy_result.get() is None
