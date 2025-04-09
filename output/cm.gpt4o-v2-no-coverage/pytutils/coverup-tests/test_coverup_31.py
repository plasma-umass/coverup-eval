# file: pytutils/props.py:40-52
# asked: {"lines": [44, 46, 47, 48, 49, 50, 52], "branches": [[48, 49], [48, 50]]}
# gained: {"lines": [44, 46, 47, 48, 49, 50, 52], "branches": [[48, 49]]}

import pytest
from pytutils.props import lazyclassproperty

class TestLazyClassProperty:
    def test_lazyclassproperty(self):
        class MyClass:
            @lazyclassproperty
            def my_prop(cls):
                return 42

        # Ensure the property is computed correctly
        assert MyClass.my_prop == 42

        # Ensure the property is cached
        assert '_lazy_my_prop' in MyClass.__dict__
        assert MyClass.__dict__['_lazy_my_prop'] == 42

        # Clean up
        delattr(MyClass, '_lazy_my_prop')

    def test_lazyclassproperty_not_cached_initially(self):
        class MyClass:
            @lazyclassproperty
            def my_prop(cls):
                return 42

        # Ensure the property is not cached initially
        assert '_lazy_my_prop' not in MyClass.__dict__

    def test_lazyclassproperty_cached_after_access(self):
        class MyClass:
            @lazyclassproperty
            def my_prop(cls):
                return 42

        # Access the property to cache it
        _ = MyClass.my_prop

        # Ensure the property is cached after access
        assert '_lazy_my_prop' in MyClass.__dict__
        assert MyClass.__dict__['_lazy_my_prop'] == 42

        # Clean up
        delattr(MyClass, '_lazy_my_prop')
