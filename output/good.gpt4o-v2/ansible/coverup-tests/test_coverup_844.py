# file: lib/ansible/playbook/base.py:75-76
# asked: {"lines": [75, 76], "branches": []}
# gained: {"lines": [75, 76], "branches": []}

import pytest
from ansible.playbook.base import Base, _generic_s

class MockBase:
    def __init__(self):
        self._attributes = {}

def test_generic_s():
    mock_base = MockBase()
    _generic_s('test_prop', mock_base, 'test_value')
    assert mock_base._attributes['test_prop'] == 'test_value'
