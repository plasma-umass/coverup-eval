# file: src/blib2to3/pytree.py:86-94
# asked: {"lines": [86, 92, 93, 94], "branches": [[92, 93], [92, 94]]}
# gained: {"lines": [86, 92, 93, 94], "branches": [[92, 93], [92, 94]]}

import pytest
from typing import Any
from blib2to3.pytree import Base

class ConcreteBase(Base):
    def _eq(self, other: Any) -> bool:
        return True

def test_base_eq_same_class():
    obj1 = ConcreteBase()
    obj2 = ConcreteBase()
    assert obj1 == obj2

def test_base_eq_different_class():
    obj1 = ConcreteBase()
    obj2 = "not a Base instance"
    assert obj1 != obj2
