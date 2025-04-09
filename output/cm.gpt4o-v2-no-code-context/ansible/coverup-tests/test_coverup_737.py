# file: lib/ansible/playbook/base.py:79-80
# asked: {"lines": [79, 80], "branches": []}
# gained: {"lines": [79, 80], "branches": []}

import pytest

from ansible.playbook.base import _generic_d

class MockClass:
    def __init__(self):
        self._attributes = {'test_prop': 'value'}

def test_generic_d_removes_property():
    obj = MockClass()
    assert 'test_prop' in obj._attributes
    _generic_d('test_prop', obj)
    assert 'test_prop' not in obj._attributes

def test_generic_d_with_nonexistent_property():
    obj = MockClass()
    with pytest.raises(KeyError):
        _generic_d('nonexistent_prop', obj)
