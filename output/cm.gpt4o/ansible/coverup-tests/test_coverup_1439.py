# file lib/ansible/playbook/base.py:247-290
# lines [251, 262]
# branches ['250->251', '261->262']

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleAssertionError
from ansible.parsing.dataloader import DataLoader

class MockVariableManager:
    pass

class MockLoader:
    pass

@pytest.fixture
def field_attribute_base():
    return FieldAttributeBase()

def test_load_data_with_none_ds(field_attribute_base):
    with pytest.raises(AnsibleAssertionError, match=r'ds \(None\) should not be None but it is.'):
        field_attribute_base.load_data(None)

def test_load_data_with_loader(field_attribute_base, mocker):
    mock_ds = {}
    mock_loader = MockLoader()
    mocker.patch.object(field_attribute_base, 'preprocess_data', return_value=mock_ds)
    mocker.patch.object(field_attribute_base, '_validate_attributes')
    mocker.patch.object(field_attribute_base, 'validate')

    field_attribute_base.load_data(mock_ds, loader=mock_loader)
    
    assert field_attribute_base._loader is mock_loader

def test_load_data_without_loader(field_attribute_base, mocker):
    mock_ds = {}
    mocker.patch.object(field_attribute_base, 'preprocess_data', return_value=mock_ds)
    mocker.patch.object(field_attribute_base, '_validate_attributes')
    mocker.patch.object(field_attribute_base, 'validate')

    field_attribute_base.load_data(mock_ds)
    
    assert isinstance(field_attribute_base._loader, DataLoader)
