# file flutils/objutils.py:116-143
# lines [116, 138, 139, 140, 141, 142, 143]
# branches ['138->139', '138->143', '139->140', '139->142', '140->139', '140->141']

import pytest
from flutils.objutils import has_callables

class TestObject:
    def method(self):
        pass

    def __call__(self):
        pass

def test_has_callables():
    obj = TestObject()
    assert has_callables(obj, 'method', '__call__') is True
    assert has_callables(obj, 'method', 'nonexistent') is False
    assert has_callables(obj, 'method', 'non_callable_attribute') is False

def test_has_callables_with_non_callable_attribute(mocker):
    obj = TestObject()
    mocker.patch.object(obj, 'method', 42)
    assert has_callables(obj, 'method') is False
