# file: pytutils/props.py:16-22
# asked: {"lines": [16, 17, 18, 19, 21, 22], "branches": []}
# gained: {"lines": [16, 17, 18, 19, 21, 22], "branches": []}

import pytest
from pytutils.props import setterproperty

class TestSetterProperty:
    def test_setterproperty_initialization(self):
        def dummy_func(obj, value):
            pass

        prop = setterproperty(dummy_func, "Test docstring")
        assert prop.func == dummy_func
        assert prop.__doc__ == "Test docstring"

    def test_setterproperty_initialization_no_doc(self):
        def dummy_func(obj, value):
            pass

        prop = setterproperty(dummy_func)
        assert prop.func == dummy_func
        assert prop.__doc__ == dummy_func.__doc__

    def test_setterproperty_set(self):
        class DummyClass:
            def __init__(self):
                self._value = None

            @setterproperty
            def value(self, val):
                self._value = val

        obj = DummyClass()
        obj.value = 10
        assert obj._value == 10
