# file pytutils/props.py:25-37
# lines [30, 31, 32, 33, 34, 35, 37]
# branches ['33->34', '33->35']

import pytest
from pytutils.props import lazyperclassproperty

class BaseTest:
    @lazyperclassproperty
    def value(cls):
        return 'base value'

class DerivedTest(BaseTest):
    pass

def test_lazyperclassproperty_different_classes():
    # Access the property on the base class to trigger the lazy initialization
    assert BaseTest.value == 'base value'
    # Access the property again to ensure it's coming from the cache
    assert BaseTest.value == 'base value'

    # Access the property on the derived class to trigger the lazy initialization
    assert DerivedTest.value == 'base value'
    # Access the property again to ensure it's coming from the cache
    assert DerivedTest.value == 'base value'
