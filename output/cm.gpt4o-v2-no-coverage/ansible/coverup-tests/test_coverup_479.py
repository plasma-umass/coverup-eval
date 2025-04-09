# file: lib/ansible/playbook/base.py:35-44
# asked: {"lines": [35, 36, 37, 38, 39, 41, 42, 44], "branches": [[41, 42], [41, 44]]}
# gained: {"lines": [35, 36, 37, 38, 39, 41, 42, 44], "branches": [[41, 42], [41, 44]]}

import pytest
from ansible.utils.sentinel import Sentinel
from ansible.playbook.base import _generic_g

class MockClass:
    def __init__(self, attributes, attr_defaults):
        self._attributes = attributes
        self._attr_defaults = attr_defaults

def test_generic_g_existing_attribute():
    obj = MockClass(attributes={'test_attr': 'value'}, attr_defaults={})
    assert _generic_g('test_attr', obj) == 'value'

def test_generic_g_missing_attribute():
    obj = MockClass(attributes={}, attr_defaults={})
    with pytest.raises(AttributeError, match="'MockClass' object has no attribute 'missing_attr'"):
        _generic_g('missing_attr', obj)

def test_generic_g_sentinel_value():
    obj = MockClass(attributes={'test_attr': Sentinel}, attr_defaults={'test_attr': 'default_value'})
    assert _generic_g('test_attr', obj) == 'default_value'
