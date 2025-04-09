# file: pytutils/props.py:25-37
# asked: {"lines": [30, 31, 32, 33, 34, 35, 37], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [30, 31, 32, 33, 34, 35, 37], "branches": [[33, 34]]}

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
