# file: pytutils/props.py:40-52
# asked: {"lines": [44, 46, 47, 48, 49, 50, 52], "branches": [[48, 49], [48, 50]]}
# gained: {"lines": [44, 46, 47, 48, 49, 50, 52], "branches": [[48, 49], [48, 50]]}

import pytest

from pytutils.props import lazyclassproperty

def test_lazyclassproperty():
    class TestClass:
        @lazyclassproperty
        def lazy_value(cls):
            return 42

    # Access the lazyclassproperty to trigger the code execution
    assert TestClass.lazy_value == 42

    # Ensure the cached value is used
    assert TestClass.lazy_value == 42

    # Clean up the attribute to avoid state pollution
    delattr(TestClass, '_lazy_lazy_value')
