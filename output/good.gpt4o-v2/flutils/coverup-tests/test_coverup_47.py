# file: flutils/objutils.py:61-85
# asked: {"lines": [61, 81, 82, 83, 84, 85], "branches": [[81, 82], [81, 85], [82, 83], [82, 85], [83, 82], [83, 84]]}
# gained: {"lines": [61, 81, 82, 83, 84, 85], "branches": [[81, 82], [81, 85], [82, 83], [82, 85], [83, 82], [83, 84]]}

import pytest
from flutils.objutils import has_any_callables

class DummyClass:
    def method(self):
        pass

    non_callable = "I am not callable"

def test_has_any_callables_with_callable_attributes():
    obj = DummyClass()
    assert has_any_callables(obj, 'method', 'non_existent') is True

def test_has_any_callables_with_non_callable_attributes():
    obj = DummyClass()
    assert has_any_callables(obj, 'non_callable') is False

def test_has_any_callables_with_no_attributes():
    obj = DummyClass()
    assert has_any_callables(obj, 'non_existent1', 'non_existent2') is False

def test_has_any_callables_with_mixed_attributes():
    obj = DummyClass()
    assert has_any_callables(obj, 'method', 'non_callable') is True
