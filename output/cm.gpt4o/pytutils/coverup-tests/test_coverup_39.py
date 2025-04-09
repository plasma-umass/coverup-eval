# file pytutils/props.py:16-22
# lines [18, 19, 22]
# branches []

import pytest
from pytutils.props import setterproperty

class TestSetterProperty:
    def test_setterproperty(self):
        class TestClass:
            def __init__(self):
                self._value = None

            @setterproperty
            def value(self, val):
                self._value = val

        obj = TestClass()
        obj.value = 10
        assert obj._value == 10

    def test_setterproperty_with_doc(self):
        class TestClass:
            def __init__(self):
                self._value = None

            def set_value(self, val):
                self._value = val

            value = setterproperty(set_value, doc="Custom docstring")

        obj = TestClass()
        assert obj.value.__doc__ == "Custom docstring"
        obj.value = 20
        assert obj._value == 20
