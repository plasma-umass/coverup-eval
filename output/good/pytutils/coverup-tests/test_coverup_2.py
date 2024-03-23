# file pytutils/props.py:16-22
# lines [16, 17, 18, 19, 21, 22]
# branches []

import pytest
from pytutils.props import setterproperty

class TestClass:
    def __init__(self):
        self._value = None

    @setterproperty
    def value(self, value):
        """Setter for value."""
        self._value = value

@pytest.fixture
def test_class_instance():
    return TestClass()

def test_setterproperty(test_class_instance):
    # Test the setterproperty by setting a value
    test_class_instance.value = 10
    assert test_class_instance._value == 10, "The setterproperty did not set the value correctly"

    # Test the docstring
    assert TestClass.value.__doc__ == "Setter for value.", "The setterproperty did not set the docstring correctly"
