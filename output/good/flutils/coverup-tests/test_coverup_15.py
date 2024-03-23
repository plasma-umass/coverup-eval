# file flutils/objutils.py:88-112
# lines [88, 109, 110, 111, 112]
# branches ['109->110', '109->112', '110->109', '110->111']

import pytest
from flutils.objutils import has_attrs

def test_has_attrs():
    class TestClass:
        def __init__(self):
            self.a = 1
            self.b = 2

    obj = TestClass()

    # Test with attributes that exist
    assert has_attrs(obj, 'a', 'b') is True

    # Test with one attribute that does not exist
    assert has_attrs(obj, 'a', 'c') is False

    # Test with no attributes passed
    assert has_attrs(obj) is True

    # Test with None as object
    assert has_attrs(None, 'a') is False

    # Test with built-in type and its attributes
    assert has_attrs(list, 'append', 'extend', 'pop') is True

    # Test with built-in type and non-existing attribute
    assert has_attrs(list, 'non_existing_method') is False

# Clean up is not necessary as no state is modified outside the function scope
