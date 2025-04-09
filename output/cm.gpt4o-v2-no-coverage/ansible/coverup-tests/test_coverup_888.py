# file: lib/ansible/playbook/base.py:75-76
# asked: {"lines": [75, 76], "branches": []}
# gained: {"lines": [75, 76], "branches": []}

import pytest
from ansible.playbook.base import _generic_s

class DummyClass:
    def __init__(self):
        self._attributes = {}

def test_generic_s():
    instance = DummyClass()
    _generic_s('test_prop', instance, 'test_value')
    
    assert instance._attributes['test_prop'] == 'test_value'
