# file: lib/ansible/playbook/base.py:247-290
# asked: {"lines": [251, 262], "branches": [[250, 251], [261, 262]]}
# gained: {"lines": [251, 262], "branches": [[250, 251], [261, 262]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from ansible.errors import AnsibleAssertionError, AnsibleParserError
from ansible.parsing.dataloader import DataLoader

class TestFieldAttributeBase:
    def test_load_data_with_none_ds(self):
        instance = FieldAttributeBase()
        with pytest.raises(AnsibleAssertionError) as excinfo:
            instance.load_data(None)
        assert 'ds (None) should not be None but it is.' in str(excinfo.value)

    def test_load_data_with_loader(self, mocker):
        instance = FieldAttributeBase()
        mock_loader = mocker.Mock()
        ds = {}
        
        instance.load_data(ds, loader=mock_loader)
        
        assert instance._ds == ds
        assert instance._loader == mock_loader

    def test_load_data_without_loader(self, mocker):
        instance = FieldAttributeBase()
        mock_preprocess_data = mocker.patch.object(instance, 'preprocess_data', return_value={})
        mock_validate_attributes = mocker.patch.object(instance, '_validate_attributes')
        ds = {}
        
        instance.load_data(ds)
        
        assert instance._ds == ds
        assert isinstance(instance._loader, DataLoader)
        mock_preprocess_data.assert_called_once_with(ds)
        mock_validate_attributes.assert_called_once_with(mock_preprocess_data.return_value)
