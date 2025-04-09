# file: lib/ansible/playbook/base.py:292-296
# asked: {"lines": [292, 293, 294, 295, 296], "branches": []}
# gained: {"lines": [292, 293, 294, 295, 296], "branches": []}

import pytest
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase:
    def test_get_ds_with_ds_attribute(self):
        instance = FieldAttributeBase()
        instance._ds = 'test_value'
        assert instance.get_ds() == 'test_value'

    def test_get_ds_without_ds_attribute(self):
        instance = FieldAttributeBase()
        assert instance.get_ds() is None
