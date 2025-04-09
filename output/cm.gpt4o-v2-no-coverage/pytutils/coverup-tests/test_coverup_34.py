# file: pytutils/props.py:40-52
# asked: {"lines": [], "branches": [[48, 50]]}
# gained: {"lines": [], "branches": [[48, 50]]}

import pytest

from pytutils.props import lazyclassproperty

def test_lazyclassproperty():
    class TestClass:
        @lazyclassproperty
        def lazy_value(cls):
            return 42

    # Ensure the lazy property is not set initially
    assert not hasattr(TestClass, '_lazy_lazy_value')

    # Access the lazy property and check its value
    assert TestClass.lazy_value == 42

    # Ensure the lazy property is now set
    assert hasattr(TestClass, '_lazy_lazy_value')
    assert TestClass._lazy_lazy_value == 42

    # Access the lazy property again to ensure it is cached
    assert TestClass.lazy_value == 42

    # Clean up
    delattr(TestClass, '_lazy_lazy_value')
