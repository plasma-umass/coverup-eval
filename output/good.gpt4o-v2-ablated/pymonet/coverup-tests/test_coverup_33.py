# file: pymonet/maybe.py:19-22
# asked: {"lines": [19, 20, 21, 22], "branches": []}
# gained: {"lines": [19, 20, 21, 22], "branches": []}

import pytest
from pymonet.maybe import Maybe

class TestMaybe:
    def test_maybe_eq_same_instance(self):
        maybe1 = Maybe.just(10)
        assert maybe1 == maybe1

    def test_maybe_eq_different_instances_same_value(self):
        maybe1 = Maybe.just(10)
        maybe2 = Maybe.just(10)
        assert maybe1 == maybe2

    def test_maybe_eq_different_instances_different_value(self):
        maybe1 = Maybe.just(10)
        maybe2 = Maybe.just(20)
        assert maybe1 != maybe2

    def test_maybe_eq_nothing_instances(self, monkeypatch):
        maybe1 = Maybe.nothing()
        maybe2 = Maybe.nothing()
        assert maybe1 == maybe2

    def test_maybe_eq_just_and_nothing(self):
        maybe1 = Maybe.just(10)
        maybe2 = Maybe.nothing()
        assert maybe1 != maybe2

    def test_maybe_eq_with_non_maybe_object(self):
        maybe1 = Maybe.just(10)
        assert maybe1 != 10
