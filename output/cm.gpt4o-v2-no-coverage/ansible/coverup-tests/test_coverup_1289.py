# file: lib/ansible/playbook/base.py:47-54
# asked: {"lines": [50, 53, 54], "branches": [[49, 50]]}
# gained: {"lines": [50, 53, 54], "branches": [[49, 50]]}

import pytest
from ansible.playbook.base import _generic_g_method

class MockClass:
    def __init__(self, squashed, attributes=None):
        self._squashed = squashed
        self._attributes = attributes or {}

    def _get_attr_test(self):
        return "test_value"

def test_generic_g_method_squashed():
    obj = MockClass(squashed=True, attributes={"test": "value"})
    assert _generic_g_method("test", obj) == "value"

def test_generic_g_method_not_squashed():
    obj = MockClass(squashed=False)
    assert _generic_g_method("test", obj) == "test_value"

def test_generic_g_method_key_error():
    obj = MockClass(squashed=True)
    with pytest.raises(AttributeError) as excinfo:
        _generic_g_method("nonexistent", obj)
    assert str(excinfo.value) == "'MockClass' object has no attribute 'nonexistent'"

def test_generic_g_method_attribute_error():
    obj = MockClass(squashed=False)
    with pytest.raises(AttributeError) as excinfo:
        _generic_g_method("nonexistent", obj)
    assert str(excinfo.value) == "'MockClass' object has no attribute '_get_attr_nonexistent'"
