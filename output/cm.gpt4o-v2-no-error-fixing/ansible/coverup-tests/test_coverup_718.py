# file: lib/ansible/playbook/base.py:247-290
# asked: {"lines": [250, 251, 254, 258, 261, 262, 264, 269, 270, 274, 276, 277, 278, 279, 280, 281, 282, 284, 287, 290], "branches": [[250, 251], [250, 254], [261, 262], [261, 264], [274, 276], [274, 287], [277, 278], [277, 279], [279, 274], [279, 280], [281, 282], [281, 284]]}
# gained: {"lines": [250, 251, 254, 258, 261, 262, 264, 269, 270, 274, 276, 277, 278, 279, 280, 281, 284, 287, 290], "branches": [[250, 251], [250, 254], [261, 262], [261, 264], [274, 276], [274, 287], [277, 278], [277, 279], [279, 280], [281, 284]]}

import pytest
from ansible.errors import AnsibleAssertionError
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils.six import iteritems
from unittest.mock import MagicMock, patch
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase:

    @pytest.fixture
    def field_attribute_base(self):
        return FieldAttributeBase()

    def test_load_data_none_ds(self, field_attribute_base):
        with pytest.raises(AnsibleAssertionError, match=r'ds \(None\) should not be None but it is.'):
            field_attribute_base.load_data(None)

    def test_load_data_with_loader(self, field_attribute_base):
        ds = {'key': 'value'}
        loader = DataLoader()
        field_attribute_base.preprocess_data = MagicMock(return_value=ds)
        field_attribute_base._validate_attributes = MagicMock()
        field_attribute_base._valid_attrs = {}
        field_attribute_base._alias_attrs = {}
        field_attribute_base.validate = MagicMock()

        result = field_attribute_base.load_data(ds, loader=loader)

        assert result == field_attribute_base
        assert field_attribute_base._ds == ds
        assert field_attribute_base._loader == loader
        field_attribute_base.preprocess_data.assert_called_once_with(ds)
        field_attribute_base._validate_attributes.assert_called_once_with(ds)
        field_attribute_base.validate.assert_called_once()

    def test_load_data_without_loader(self, field_attribute_base):
        ds = {'key': 'value'}
        field_attribute_base.preprocess_data = MagicMock(return_value=ds)
        field_attribute_base._validate_attributes = MagicMock()
        field_attribute_base._valid_attrs = {}
        field_attribute_base._alias_attrs = {}
        field_attribute_base.validate = MagicMock()

        result = field_attribute_base.load_data(ds)

        assert result == field_attribute_base
        assert field_attribute_base._ds == ds
        assert isinstance(field_attribute_base._loader, DataLoader)
        field_attribute_base.preprocess_data.assert_called_once_with(ds)
        field_attribute_base._validate_attributes.assert_called_once_with(ds)
        field_attribute_base.validate.assert_called_once()

    def test_load_data_with_valid_attrs(self, field_attribute_base):
        ds = {'key': 'value'}
        field_attribute_base.preprocess_data = MagicMock(return_value=ds)
        field_attribute_base._validate_attributes = MagicMock()
        field_attribute_base._valid_attrs = {'key': 1}
        field_attribute_base._alias_attrs = {}
        field_attribute_base.validate = MagicMock()

        result = field_attribute_base.load_data(ds)

        assert result == field_attribute_base
        assert field_attribute_base._ds == ds
        assert field_attribute_base._attributes['key'] == 'value'
        field_attribute_base.preprocess_data.assert_called_once_with(ds)
        field_attribute_base._validate_attributes.assert_called_once_with(ds)
        field_attribute_base.validate.assert_called_once()

    def test_load_data_with_alias_attrs(self, field_attribute_base):
        ds = {'key': 'value'}
        field_attribute_base.preprocess_data = MagicMock(return_value=ds)
        field_attribute_base._validate_attributes = MagicMock()
        field_attribute_base._valid_attrs = {'key': 1}
        field_attribute_base._alias_attrs = {'key': 'alias_key'}
        field_attribute_base.validate = MagicMock()

        result = field_attribute_base.load_data(ds)

        assert result == field_attribute_base
        assert field_attribute_base._ds == ds
        assert field_attribute_base._attributes['alias_key'] == 'value'
        field_attribute_base.preprocess_data.assert_called_once_with(ds)
        field_attribute_base._validate_attributes.assert_called_once_with(ds)
        field_attribute_base.validate.assert_called_once()
