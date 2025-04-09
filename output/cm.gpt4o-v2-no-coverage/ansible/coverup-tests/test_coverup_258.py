# file: lib/ansible/playbook/base.py:57-72
# asked: {"lines": [57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 69, 70, 72], "branches": [[59, 60], [59, 62], [69, 70], [69, 72]]}
# gained: {"lines": [57, 58, 59, 60, 62, 63, 64, 65, 66, 67, 69, 70, 72], "branches": [[59, 60], [59, 62], [69, 70], [69, 72]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.utils.sentinel import Sentinel
from ansible.playbook.base import _generic_g_parent

class MockSelf:
    def __init__(self, squashed=False, finalized=False, attributes=None, attr_defaults=None):
        self._squashed = squashed
        self._finalized = finalized
        self._attributes = attributes or {}
        self._attr_defaults = attr_defaults or {}

    def _get_parent_attribute(self, prop_name):
        raise AttributeError

def test_generic_g_parent_squashed():
    mock_self = MockSelf(squashed=True, attributes={'test_prop': 'test_value'})
    assert _generic_g_parent('test_prop', mock_self) == 'test_value'

def test_generic_g_parent_finalized():
    mock_self = MockSelf(finalized=True, attributes={'test_prop': 'test_value'})
    assert _generic_g_parent('test_prop', mock_self) == 'test_value'

def test_generic_g_parent_not_squashed_or_finalized_with_parent_attribute():
    mock_self = MockSelf(attributes={'test_prop': 'test_value'})
    mock_self._get_parent_attribute = MagicMock(return_value='parent_value')
    assert _generic_g_parent('test_prop', mock_self) == 'parent_value'

def test_generic_g_parent_not_squashed_or_finalized_without_parent_attribute():
    mock_self = MockSelf(attributes={'test_prop': 'test_value'})
    assert _generic_g_parent('test_prop', mock_self) == 'test_value'

def test_generic_g_parent_key_error():
    mock_self = MockSelf()
    with pytest.raises(AttributeError, match="'MockSelf' object has no attribute 'test_prop'"):
        _generic_g_parent('test_prop', mock_self)

def test_generic_g_parent_sentinel_value():
    mock_self = MockSelf(attributes={'test_prop': Sentinel}, attr_defaults={'test_prop': 'default_value'})
    assert _generic_g_parent('test_prop', mock_self) == 'default_value'
