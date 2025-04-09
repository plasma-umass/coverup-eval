# file: lib/ansible/playbook/base.py:740-751
# asked: {"lines": [748], "branches": [[747, 748]]}
# gained: {"lines": [748], "branches": [[747, 748]]}

import pytest
from ansible.playbook.base import FieldAttributeBase

class MockAttribute:
    def __init__(self, isa):
        self.isa = isa

class MockClassWithSerialize:
    def serialize(self):
        return "serialized_value"

class TestFieldAttributeBase:
    def test_dump_attrs_with_serialize(self, mocker):
        # Create a mock for _valid_attrs
        mock_valid_attrs = {
            'attr1': MockAttribute('class'),
            'attr2': MockAttribute('other')
        }

        # Create an instance of the class
        instance = FieldAttributeBase()
        instance._valid_attrs = mock_valid_attrs
        instance.attr1 = MockClassWithSerialize()
        instance.attr2 = "regular_value"

        # Patch the instance's _valid_attrs
        mocker.patch.object(instance, '_valid_attrs', mock_valid_attrs)

        # Call the method
        result = instance.dump_attrs()

        # Assertions
        assert result['attr1'] == "serialized_value"
        assert result['attr2'] == "regular_value"
