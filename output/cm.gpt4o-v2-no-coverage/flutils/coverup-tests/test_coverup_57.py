# file: flutils/objutils.py:61-85
# asked: {"lines": [81, 82, 83, 84, 85], "branches": [[81, 82], [81, 85], [82, 83], [82, 85], [83, 82], [83, 84]]}
# gained: {"lines": [81, 82, 83, 84, 85], "branches": [[81, 82], [81, 85], [82, 83], [82, 85], [83, 82], [83, 84]]}

import pytest
from flutils.objutils import has_any_callables

class DummyClass:
    def method(self):
        pass

    non_callable = "I am not callable"

def test_has_any_callables_with_callable_attrs():
    obj = DummyClass()
    assert has_any_callables(obj, 'method', 'non_existent_attr') is True

def test_has_any_callables_with_non_callable_attrs():
    obj = DummyClass()
    assert has_any_callables(obj, 'non_callable') is False

def test_has_any_callables_with_no_attrs():
    obj = DummyClass()
    assert has_any_callables(obj) is False

def test_has_any_callables_with_mixed_attrs():
    obj = DummyClass()
    assert has_any_callables(obj, 'method', 'non_callable') is True

def test_has_any_callables_with_non_existent_attrs():
    obj = DummyClass()
    assert has_any_callables(obj, 'non_existent_attr1', 'non_existent_attr2') is False
