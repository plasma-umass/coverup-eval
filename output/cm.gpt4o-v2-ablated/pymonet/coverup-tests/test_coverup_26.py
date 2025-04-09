# file: pymonet/immutable_list.py:18-22
# asked: {"lines": [18, 19, 20, 21, 22], "branches": []}
# gained: {"lines": [18, 19, 20, 21, 22], "branches": []}

import pytest
from pymonet.immutable_list import ImmutableList

class TestImmutableList:
    def test_eq_same_object(self):
        lst = ImmutableList()
        assert lst == lst

    def test_eq_different_type(self):
        lst = ImmutableList()
        assert lst != []

    def test_eq_different_head(self, monkeypatch):
        lst1 = ImmutableList()
        lst2 = ImmutableList()
        monkeypatch.setattr(lst1, 'head', 1)
        monkeypatch.setattr(lst2, 'head', 2)
        assert lst1 != lst2

    def test_eq_different_tail(self, monkeypatch):
        lst1 = ImmutableList()
        lst2 = ImmutableList()
        monkeypatch.setattr(lst1, 'tail', [1])
        monkeypatch.setattr(lst2, 'tail', [2])
        assert lst1 != lst2

    def test_eq_different_is_empty(self, monkeypatch):
        lst1 = ImmutableList()
        lst2 = ImmutableList()
        monkeypatch.setattr(lst1, 'is_empty', True)
        monkeypatch.setattr(lst2, 'is_empty', False)
        assert lst1 != lst2

    def test_eq_all_equal(self, monkeypatch):
        lst1 = ImmutableList()
        lst2 = ImmutableList()
        monkeypatch.setattr(lst1, 'head', 1)
        monkeypatch.setattr(lst2, 'head', 1)
        monkeypatch.setattr(lst1, 'tail', [2])
        monkeypatch.setattr(lst2, 'tail', [2])
        monkeypatch.setattr(lst1, 'is_empty', False)
        monkeypatch.setattr(lst2, 'is_empty', False)
        assert lst1 == lst2
