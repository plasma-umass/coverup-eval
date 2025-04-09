# file: flutils/objutils.py:61-85
# asked: {"lines": [], "branches": [[82, 85], [83, 82]]}
# gained: {"lines": [], "branches": [[82, 85], [83, 82]]}

import pytest
from flutils.objutils import has_any_callables

class DummyClass:
    def method(self):
        pass

def test_has_any_callables_with_callable_attr():
    obj = DummyClass()
    assert has_any_callables(obj, 'method') is True

def test_has_any_callables_with_non_callable_attr():
    obj = DummyClass()
    obj.non_callable = "I am not callable"
    assert has_any_callables(obj, 'non_callable') is False

def test_has_any_callables_with_no_attrs():
    obj = DummyClass()
    assert has_any_callables(obj, 'non_existent_attr') is False

def test_has_any_callables_with_mixed_attrs():
    obj = DummyClass()
    obj.non_callable = "I am not callable"
    assert has_any_callables(obj, 'non_callable', 'method') is True

def test_has_any_callables_with_no_matching_attrs():
    obj = DummyClass()
    assert has_any_callables(obj, 'non_existent_attr1', 'non_existent_attr2') is False
