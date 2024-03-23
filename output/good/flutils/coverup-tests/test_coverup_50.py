# file flutils/decorators.py:8-56
# lines [8, 9]
# branches []

import pytest

from flutils.decorators import cached_property


class MyClass:
    def __init__(self):
        self._y_called = 0

    @cached_property
    def y(self):
        self._y_called += 1
        return 42


@pytest.fixture
def my_class_instance():
    return MyClass()


def test_cached_property(my_class_instance):
    # Ensure the property is not yet set
    assert not hasattr(my_class_instance, '_y')

    # Call the property and check if it returns the correct value
    assert my_class_instance.y == 42
    # Ensure the property was called
    assert my_class_instance._y_called == 1

    # Call the property again and make sure it's not computed again
    assert my_class_instance.y == 42
    assert my_class_instance._y_called == 1

    # Delete the property and ensure it can be recomputed
    del my_class_instance.y
    assert not hasattr(my_class_instance, '_y')
    assert my_class_instance.y == 42
    assert my_class_instance._y_called == 2

    # Clean up by deleting the instance attribute
    del my_class_instance.y
