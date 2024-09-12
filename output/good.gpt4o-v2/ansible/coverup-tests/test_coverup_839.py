# file: lib/ansible/playbook/base.py:79-80
# asked: {"lines": [79, 80], "branches": []}
# gained: {"lines": [79, 80], "branches": []}

import pytest
from ansible.playbook.base import Base, _generic_d

class TestBase(Base):
    def __init__(self):
        self._attributes = {
            'test_prop': 'test_value'
        }

def test_generic_d():
    obj = TestBase()
    assert 'test_prop' in obj._attributes
    _generic_d('test_prop', obj)
    assert 'test_prop' not in obj._attributes
