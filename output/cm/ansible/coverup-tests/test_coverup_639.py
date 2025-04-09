# file lib/ansible/playbook/base.py:292-296
# lines [292, 293, 294, 295, 296]
# branches []

import pytest
from ansible.playbook.base import FieldAttributeBase

class MockFieldAttributeBase(FieldAttributeBase):
    pass

def test_get_ds_with_ds_set():
    mock_base = MockFieldAttributeBase()
    mock_base._ds = 'test_data_structure'
    assert mock_base.get_ds() == 'test_data_structure'

def test_get_ds_without_ds_set():
    mock_base = MockFieldAttributeBase()
    assert mock_base.get_ds() is None
