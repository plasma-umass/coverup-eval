# file pytutils/props.py:40-52
# lines [44, 46, 47, 48, 49, 50, 52]
# branches ['48->49', '48->50']

import pytest
from pytutils.props import lazyclassproperty

class TestClass:
    _lazy_called = False

    @lazyclassproperty
    def lazy_prop(cls):
        if cls._lazy_called:
            raise ValueError("lazy_prop should only be called once.")
        cls._lazy_called = True
        return 42

def test_lazyclassproperty():
    assert TestClass.lazy_prop == 42
    assert TestClass.lazy_prop == 42  # Access the property again to ensure it's cached

    # Cleanup
    if hasattr(TestClass, '_lazy_lazy_prop'):
        delattr(TestClass, '_lazy_lazy_prop')
    TestClass._lazy_called = False
