# file: lib/ansible/playbook/base.py:774-790
# asked: {"lines": [774, 783, 786, 787, 788, 790], "branches": []}
# gained: {"lines": [774, 783, 786, 787, 788, 790], "branches": []}

import pytest
from unittest.mock import MagicMock

# Assuming the class FieldAttributeBase and its dependencies are imported from ansible.playbook.base
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase:
    @pytest.fixture
    def field_attribute_base(self, mocker):
        class MockFieldAttributeBase(FieldAttributeBase):
            def __init__(self):
                self._uuid = 'test-uuid'
                self._finalized = True
                self._squashed = False

            def dump_attrs(self):
                return {'attr1': 'value1', 'attr2': 'value2'}

        return MockFieldAttributeBase()

    def test_serialize(self, field_attribute_base):
        result = field_attribute_base.serialize()
        
        assert result['uuid'] == 'test-uuid'
        assert result['finalized'] is True
        assert result['squashed'] is False
        assert result['attr1'] == 'value1'
        assert result['attr2'] == 'value2'
