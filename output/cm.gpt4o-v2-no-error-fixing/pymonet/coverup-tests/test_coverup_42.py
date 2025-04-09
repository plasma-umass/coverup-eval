# file: pymonet/maybe.py:19-22
# asked: {"lines": [19, 20, 21, 22], "branches": []}
# gained: {"lines": [19, 20, 21, 22], "branches": []}

import pytest
from pymonet.maybe import Maybe

def test_maybe_eq_with_nothing():
    maybe1 = Maybe.nothing()
    maybe2 = Maybe.nothing()
    assert maybe1 == maybe2

def test_maybe_eq_with_just():
    maybe1 = Maybe.just(10)
    maybe2 = Maybe.just(10)
    assert maybe1 == maybe2

def test_maybe_eq_with_different_values():
    maybe1 = Maybe.just(10)
    maybe2 = Maybe.just(20)
    assert maybe1 != maybe2

def test_maybe_eq_with_nothing_and_just():
    maybe1 = Maybe.nothing()
    maybe2 = Maybe.just(10)
    assert maybe1 != maybe2

def test_maybe_eq_with_different_types():
    maybe1 = Maybe.just(10)
    assert maybe1 != 10
