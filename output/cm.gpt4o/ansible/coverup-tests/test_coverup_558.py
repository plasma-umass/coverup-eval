# file lib/ansible/playbook/base.py:774-790
# lines [774, 783, 786, 787, 788, 790]
# branches []

import pytest
from unittest.mock import MagicMock

# Assuming the FieldAttributeBase class is imported from ansible.playbook.base
from ansible.playbook.base import FieldAttributeBase

class TestFieldAttributeBase(FieldAttributeBase):
    def __init__(self, uuid, finalized, squashed):
        self._uuid = uuid
        self._finalized = finalized
        self._squashed = squashed

    def dump_attrs(self):
        return {'attr1': 'value1', 'attr2': 'value2'}

@pytest.fixture
def field_attribute_base():
    return TestFieldAttributeBase(uuid='1234-5678', finalized=True, squashed=False)

def test_serialize(field_attribute_base):
    serialized = field_attribute_base.serialize()
    assert serialized['uuid'] == '1234-5678'
    assert serialized['finalized'] is True
    assert serialized['squashed'] is False
    assert serialized['attr1'] == 'value1'
    assert serialized['attr2'] == 'value2'
