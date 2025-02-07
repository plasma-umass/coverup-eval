# file: flutils/objutils.py:116-143
# asked: {"lines": [116, 138, 139, 140, 141, 142, 143], "branches": [[138, 139], [138, 143], [139, 140], [139, 142], [140, 139], [140, 141]]}
# gained: {"lines": [116, 138, 139, 140, 141, 142, 143], "branches": [[138, 139], [138, 143], [139, 140], [139, 142], [140, 139], [140, 141]]}

import pytest
from flutils.objutils import has_callables

class DummyClass:
    def method_one(self):
        pass

    def method_two(self):
        pass

    not_callable = "I am not callable"

def test_has_callables_all_callable():
    obj = DummyClass()
    assert has_callables(obj, 'method_one', 'method_two') is True

def test_has_callables_not_all_callable():
    obj = DummyClass()
    assert has_callables(obj, 'method_one', 'not_callable') is False

def test_has_callables_missing_attr():
    obj = DummyClass()
    assert has_callables(obj, 'method_one', 'missing_method') is False
