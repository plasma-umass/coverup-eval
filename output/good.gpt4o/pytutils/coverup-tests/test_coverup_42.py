# file pytutils/props.py:40-52
# lines [44, 46, 47, 48, 49, 50, 52]
# branches ['48->49', '48->50']

import pytest
from pytutils.props import lazyclassproperty

class TestClass:
    @lazyclassproperty
    def expensive_computation(cls):
        return sum(range(100))

def test_lazyclassproperty():
    # Ensure the property is computed correctly
    assert TestClass.expensive_computation == 4950
    
    # Ensure the property is cached by checking the attribute directly
    assert hasattr(TestClass, '_lazy_expensive_computation')
    assert TestClass._lazy_expensive_computation == 4950

    # Clean up to not affect other tests
    delattr(TestClass, '_lazy_expensive_computation')
