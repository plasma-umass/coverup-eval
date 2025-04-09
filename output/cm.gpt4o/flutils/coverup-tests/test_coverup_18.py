# file flutils/objutils.py:36-58
# lines [36, 55, 56, 57, 58]
# branches ['55->56', '55->58', '56->55', '56->57']

import pytest
from flutils.objutils import has_any_attrs

def test_has_any_attrs():
    class TestClass:
        def __init__(self):
            self.attr1 = "value1"
            self.attr2 = "value2"

    obj = TestClass()

    # Test case where the object has at least one of the attributes
    assert has_any_attrs(obj, 'attr1', 'attr3') == True
    assert has_any_attrs(obj, 'attr2', 'attr4') == True

    # Test case where the object does not have any of the attributes
    assert has_any_attrs(obj, 'attr3', 'attr4') == False

    # Test case with no attributes provided
    assert has_any_attrs(obj) == False

    # Test case with built-in object and attributes
    assert has_any_attrs(dict(), 'get', 'keys', 'items', 'values', 'something') == True
    assert has_any_attrs(dict(), 'something') == False
