# file: pytutils/props.py:25-37
# asked: {"lines": [25, 30, 31, 32, 33, 34, 35, 37], "branches": [[33, 34], [33, 35]]}
# gained: {"lines": [25, 30, 31, 32, 33, 34, 35, 37], "branches": [[33, 34], [33, 35]]}

import pytest
from pytutils.props import lazyperclassproperty

class TestClass:
    @lazyperclassproperty
    def lazy_value(cls):
        return 42

def test_lazyperclassproperty():
    # Access the lazy property to trigger its evaluation and caching
    assert TestClass.lazy_value == 42
    # Ensure the cached value is used on subsequent access
    assert TestClass.lazy_value == 42

    # Check that the attribute is set on the class
    attr_name = '_TestClass_lazy_lazy_value'
    assert hasattr(TestClass, attr_name)
    assert getattr(TestClass, attr_name) == 42
