# file: flutils/objutils.py:116-143
# asked: {"lines": [116, 138, 139, 140, 141, 142, 143], "branches": [[138, 139], [138, 143], [139, 140], [139, 142], [140, 139], [140, 141]]}
# gained: {"lines": [116, 138, 139, 140, 141, 142, 143], "branches": [[138, 139], [138, 143], [139, 140], [139, 142], [140, 139], [140, 141]]}

import pytest
from flutils.objutils import has_callables

class DummyClass:
    def method1(self):
        pass

    def method2(self):
        pass

    not_callable = "I am not callable"

def test_has_callables_all_callable():
    obj = DummyClass()
    assert has_callables(obj, 'method1', 'method2') is True

def test_has_callables_not_all_callable():
    obj = DummyClass()
    assert has_callables(obj, 'method1', 'not_callable') is False

def test_has_callables_missing_attr():
    obj = DummyClass()
    assert has_callables(obj, 'method1', 'missing_method') is False

def test_has_callables_no_attrs():
    obj = DummyClass()
    assert has_callables(obj) is True

def test_has_callables_empty_obj():
    obj = object()
    assert has_callables(obj, 'method1') is False
