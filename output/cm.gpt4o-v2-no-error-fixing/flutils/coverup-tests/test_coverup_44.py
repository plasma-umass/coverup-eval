# file: flutils/objutils.py:61-85
# asked: {"lines": [81, 82, 83, 84, 85], "branches": [[81, 82], [81, 85], [82, 83], [82, 85], [83, 82], [83, 84]]}
# gained: {"lines": [81, 82, 83, 84, 85], "branches": [[81, 82], [81, 85], [82, 83], [83, 84]]}

import pytest
from flutils.objutils import has_any_callables

def test_has_any_callables_with_callable_attrs():
    class TestClass:
        def method(self):
            pass

    obj = TestClass()
    assert has_any_callables(obj, 'method', 'nonexistent') is True

def test_has_any_callables_with_non_callable_attrs():
    class TestClass:
        def method(self):
            pass

    obj = TestClass()
    assert has_any_callables(obj, 'nonexistent') is False

def test_has_any_callables_with_mixed_attrs():
    class TestClass:
        def method(self):
            pass
        attribute = "I am not callable"

    obj = TestClass()
    assert has_any_callables(obj, 'method', 'attribute') is True

def test_has_any_callables_with_no_attrs():
    class TestClass:
        def method(self):
            pass

    obj = TestClass()
    assert has_any_callables(obj, 'nonexistent1', 'nonexistent2') is False
