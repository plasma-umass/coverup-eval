# file: pytutils/props.py:1-10
# asked: {"lines": [1, 2, 6, 7, 9, 10], "branches": []}
# gained: {"lines": [1, 2, 6, 7, 9, 10], "branches": []}

import pytest
from pytutils.props import roclassproperty

class TestRoClassProperty:
    def test_roclassproperty_get(self):
        class MyClass:
            @roclassproperty
            def my_prop(cls):
                return "class property value"
        
        assert MyClass.my_prop == "class property value"
    
    def test_roclassproperty_with_instance(self):
        class MyClass:
            @roclassproperty
            def my_prop(cls):
                return "class property value"
        
        instance = MyClass()
        assert instance.my_prop == "class property value"
