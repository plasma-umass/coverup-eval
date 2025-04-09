# file: pytutils/lazy/lazy_import.py:115-118
# asked: {"lines": [115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}
# gained: {"lines": [115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}

import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_illegal_use_of_scope_replacer_eq_same_class():
    exc1 = IllegalUseOfScopeReplacer("name1", "msg1")
    exc2 = IllegalUseOfScopeReplacer("name1", "msg1")
    assert exc1 == exc2

def test_illegal_use_of_scope_replacer_eq_different_class():
    exc1 = IllegalUseOfScopeReplacer("name1", "msg1")
    class DifferentException(Exception):
        pass
    exc2 = DifferentException()
    assert exc1 != exc2
