# file lib/ansible/playbook/base.py:518-527
# lines [518, 524, 525, 526, 527]
# branches ['524->exit', '524->525', '525->526', '525->527']

import pytest
from unittest import mock

# Assuming the class FieldAttributeBase is imported from ansible.playbook.base
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase:
    @pytest.fixture
    def field_attribute_base(self):
        class TestFieldAttributeBase(FieldAttributeBase):
            _valid_attrs = {'attr1': 'value1', 'attr2': 'value2'}
            _attributes = {}
            _squashed = False

            def __init__(self):
                self.attr1 = 'evaluated_value1'
                self.attr2 = 'evaluated_value2'
                super().__init__()

        return TestFieldAttributeBase()

    def test_squash(self, field_attribute_base):
        # Ensure initial state
        assert not field_attribute_base._squashed
        assert field_attribute_base._attributes == {}

        # Mock the _valid_attrs to ensure it contains the correct keys
        field_attribute_base._valid_attrs = {'attr1': None, 'attr2': None}

        # Call the method
        field_attribute_base.squash()

        # Verify the attributes are set correctly
        assert field_attribute_base._attributes['attr1'] == 'evaluated_value1'
        assert field_attribute_base._attributes['attr2'] == 'evaluated_value2'
        assert field_attribute_base._squashed

        # Clean up
        field_attribute_base._attributes.clear()
        field_attribute_base._squashed = False
