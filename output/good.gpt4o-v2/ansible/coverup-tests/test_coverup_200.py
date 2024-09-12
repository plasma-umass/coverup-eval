# file: lib/ansible/playbook/base.py:57-72
# asked: {"lines": [57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 69, 70, 72], "branches": [[59, 60], [59, 62], [69, 70], [69, 72]]}
# gained: {"lines": [57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 69, 70, 72], "branches": [[59, 60], [59, 62], [69, 70], [69, 72]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.playbook.base import _generic_g_parent
from ansible.utils.sentinel import Sentinel

class MockParent:
    def __init__(self, squashed=False, finalized=False, attributes=None, attr_defaults=None):
        self._squashed = squashed
        self._finalized = finalized
        self._attributes = attributes or {}
        self._attr_defaults = attr_defaults or {}

    def _get_parent_attribute(self, prop_name):
        raise AttributeError

def test_generic_g_parent_squashed():
    parent = MockParent(squashed=True, attributes={'test_prop': 'test_value'})
    assert _generic_g_parent('test_prop', parent) == 'test_value'

def test_generic_g_parent_finalized():
    parent = MockParent(finalized=True, attributes={'test_prop': 'test_value'})
    assert _generic_g_parent('test_prop', parent) == 'test_value'

def test_generic_g_parent_get_parent_attribute():
    parent = MockParent(attributes={'test_prop': 'test_value'})
    parent._get_parent_attribute = MagicMock(return_value='parent_value')
    assert _generic_g_parent('test_prop', parent) == 'parent_value'
    parent._get_parent_attribute.assert_called_once_with('test_prop')

def test_generic_g_parent_key_error():
    parent = MockParent()
    with pytest.raises(AttributeError, match="'MockParent' object has no attribute 'test_prop'"):
        _generic_g_parent('test_prop', parent)

def test_generic_g_parent_sentinel():
    parent = MockParent(attributes={'test_prop': Sentinel}, attr_defaults={'test_prop': 'default_value'})
    assert _generic_g_parent('test_prop', parent) == 'default_value'
