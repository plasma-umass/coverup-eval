# file: pytutils/props.py:25-37
# asked: {"lines": [25, 30, 31, 32, 33, 34, 35, 37], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [25, 30, 31, 32, 33, 34, 35, 37], "branches": [[33, 34]]}

import pytest
from pytutils.props import lazyperclassproperty

class TestLazyPerClassProperty:
    def test_lazyperclassproperty(self):
        class MyClass:
            @lazyperclassproperty
            def my_prop(cls):
                return "value"

        # Access the property to trigger the lazy loading
        assert MyClass.my_prop == "value"
        # Ensure the property is cached by checking the attribute directly
        assert hasattr(MyClass, '_MyClass_lazy_my_prop')
        assert getattr(MyClass, '_MyClass_lazy_my_prop') == "value"

    def test_lazyperclassproperty_inheritance(self):
        class BaseClass:
            @lazyperclassproperty
            def my_prop(cls):
                return "base_value"

        class SubClass(BaseClass):
            @lazyperclassproperty
            def my_prop(cls):
                return "sub_value"

        # Access the property to trigger the lazy loading
        assert BaseClass.my_prop == "base_value"
        assert SubClass.my_prop == "sub_value"
        # Ensure the property is cached by checking the attribute directly
        assert hasattr(BaseClass, '_BaseClass_lazy_my_prop')
        assert hasattr(SubClass, '_SubClass_lazy_my_prop')
        assert getattr(BaseClass, '_BaseClass_lazy_my_prop') == "base_value"
        assert getattr(SubClass, '_SubClass_lazy_my_prop') == "sub_value"

    def test_lazyperclassproperty_no_overlap(self):
        class ClassA:
            @lazyperclassproperty
            def my_prop(cls):
                return "value_a"

        class ClassB:
            @lazyperclassproperty
            def my_prop(cls):
                return "value_b"

        # Access the property to trigger the lazy loading
        assert ClassA.my_prop == "value_a"
        assert ClassB.my_prop == "value_b"
        # Ensure the property is cached by checking the attribute directly
        assert hasattr(ClassA, '_ClassA_lazy_my_prop')
        assert hasattr(ClassB, '_ClassB_lazy_my_prop')
        assert getattr(ClassA, '_ClassA_lazy_my_prop') == "value_a"
        assert getattr(ClassB, '_ClassB_lazy_my_prop') == "value_b"
