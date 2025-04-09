# file: pytutils/lazy/simple_import.py:14-21
# asked: {"lines": [14, 15, 18, 20, 21], "branches": []}
# gained: {"lines": [14, 15, 18, 20, 21], "branches": []}

import pytest
from pytutils.lazy.simple_import import NonLocal

def test_nonlocal_initialization():
    # Test the initialization of NonLocal class
    non_local_instance = NonLocal(value=10)
    assert non_local_instance.value == 10

def test_nonlocal_value_assignment():
    # Test the value assignment of NonLocal class
    non_local_instance = NonLocal(value=20)
    non_local_instance.value = 30
    assert non_local_instance.value == 30
