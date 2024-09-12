# file: pytutils/lazy/lazy_import.py:115-118
# asked: {"lines": [115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}
# gained: {"lines": [115, 116, 117, 118], "branches": [[116, 117], [116, 118]]}

import pytest
from pytutils.lazy.lazy_import import IllegalUseOfScopeReplacer

def test_illegal_use_of_scope_replacer_eq_same_class():
    obj1 = IllegalUseOfScopeReplacer("name1", "msg1")
    obj2 = IllegalUseOfScopeReplacer("name1", "msg1")
    assert obj1 == obj2

def test_illegal_use_of_scope_replacer_eq_different_class():
    class DifferentClass:
        def __init__(self, name, msg):
            self.name = name
            self.msg = msg

    obj1 = IllegalUseOfScopeReplacer("name1", "msg1")
    obj2 = DifferentClass("name1", "msg1")
    assert obj1 != obj2
