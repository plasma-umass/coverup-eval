# file: pytutils/lazy/simple_import.py:14-21
# asked: {"lines": [14, 15, 18, 20, 21], "branches": []}
# gained: {"lines": [14, 15, 18, 20, 21], "branches": []}

import pytest

from pytutils.lazy.simple_import import NonLocal

def test_nonlocal_initialization():
    value = 10
    nonlocal_instance = NonLocal(value)
    assert nonlocal_instance.value == value

def test_nonlocal_slots():
    nonlocal_instance = NonLocal(10)
    with pytest.raises(AttributeError):
        nonlocal_instance.new_attr = "test"

