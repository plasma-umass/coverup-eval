# file lib/ansible/playbook/base.py:292-296
# lines [292, 293, 294, 295, 296]
# branches []

import pytest
from unittest.mock import patch

# Assuming the FieldAttributeBase class is imported from ansible.playbook.base
from ansible.playbook.base import FieldAttributeBase

def test_get_ds_with_ds_attribute():
    instance = FieldAttributeBase()
    instance._ds = 'test_value'
    assert instance.get_ds() == 'test_value'

def test_get_ds_without_ds_attribute():
    instance = FieldAttributeBase()
    assert instance.get_ds() is None
