# file: lib/ansible/playbook/base.py:292-296
# asked: {"lines": [292, 293, 294, 295, 296], "branches": []}
# gained: {"lines": [292, 293, 294, 295, 296], "branches": []}

import pytest
from ansible.playbook.base import FieldAttributeBase

def test_get_ds_with_ds_attribute():
    obj = FieldAttributeBase()
    obj._ds = 'test_ds'
    assert obj.get_ds() == 'test_ds'

def test_get_ds_without_ds_attribute():
    obj = FieldAttributeBase()
    assert obj.get_ds() is None
