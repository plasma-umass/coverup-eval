# file pytutils/lazy/simple_import.py:14-21
# lines [14, 15, 18, 20, 21]
# branches []

import pytest
from pytutils.lazy.simple_import import NonLocal

def test_nonlocal_init_and_value():
    # Test the initialization and value attribute of NonLocal class
    initial_value = 'initial'
    nonlocal_instance = NonLocal(initial_value)
    assert nonlocal_instance.value == initial_value, "NonLocal instance value should be the initial value"

    # Test updating the value attribute
    new_value = 'updated'
    nonlocal_instance.value = new_value
    assert nonlocal_instance.value == new_value, "NonLocal instance value should be updated to the new value"

    # Test the __slots__ mechanism by trying to add a new attribute
    with pytest.raises(AttributeError):
        nonlocal_instance.new_attr = 'should fail'
