# file pytutils/props.py:1-10
# lines [1, 2, 6, 7, 9, 10]
# branches []

import pytest
from pytutils.props import roclassproperty

class MyClass:
    _value = "class_value"

    @roclassproperty
    def value(cls):
        return cls._value

def test_roclassproperty():
    assert MyClass.value == "class_value", "The roclassproperty did not return the expected value"

    # Modify the class attribute to ensure the property reflects the change
    MyClass._value = "new_value"
    assert MyClass.value == "new_value", "The roclassproperty did not reflect the updated class attribute"

    # Clean up by resetting the class attribute to its original value
    MyClass._value = "class_value"
