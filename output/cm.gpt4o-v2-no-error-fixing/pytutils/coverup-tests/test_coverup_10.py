# file: pytutils/props.py:40-52
# asked: {"lines": [40, 44, 46, 47, 48, 49, 50, 52], "branches": [[48, 49], [48, 50]]}
# gained: {"lines": [40, 44, 46, 47, 48, 49, 50, 52], "branches": [[48, 49], [48, 50]]}

import pytest
from pytutils.props import lazyclassproperty

class TestClass:
    @lazyclassproperty
    def lazy_value(cls):
        return 42

def test_lazyclassproperty():
    # Access the lazy property and assert its value
    assert TestClass.lazy_value == 42

    # Ensure the value is cached by checking the attribute directly
    assert getattr(TestClass, '_lazy_lazy_value') == 42

    # Clean up the cached attribute to avoid state pollution
    delattr(TestClass, '_lazy_lazy_value')
