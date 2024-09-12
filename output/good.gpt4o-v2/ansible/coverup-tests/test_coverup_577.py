# file: lib/ansible/playbook/base.py:774-790
# asked: {"lines": [774, 783, 786, 787, 788, 790], "branches": []}
# gained: {"lines": [774, 783, 786, 787, 788, 790], "branches": []}

import pytest
from ansible.playbook.base import FieldAttributeBase

@pytest.fixture
def field_attribute_base():
    return FieldAttributeBase()

def test_serialize(field_attribute_base, mocker):
    # Mock the dump_attrs method to return a specific dictionary
    mocker.patch.object(field_attribute_base, 'dump_attrs', return_value={})
    
    # Call the serialize method
    result = field_attribute_base.serialize()
    
    # Check that the result contains the expected keys and values
    assert 'uuid' in result
    assert result['uuid'] == field_attribute_base._uuid
    assert 'finalized' in result
    assert result['finalized'] == field_attribute_base._finalized
    assert 'squashed' in result
    assert result['squashed'] == field_attribute_base._squashed

    # Ensure that dump_attrs was called
    field_attribute_base.dump_attrs.assert_called_once()
