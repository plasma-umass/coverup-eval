# file: lib/ansible/playbook/base.py:740-751
# asked: {"lines": [740, 744, 745, 746, 747, 748, 750, 751], "branches": [[745, 746], [745, 751], [747, 748], [747, 750]]}
# gained: {"lines": [740, 744, 745, 746, 747, 748, 750, 751], "branches": [[745, 746], [745, 751], [747, 748], [747, 750]]}

import pytest
from unittest.mock import Mock

from ansible.playbook.base import FieldAttributeBase

class MockAttribute:
    def __init__(self, isa):
        self.isa = isa

    def serialize(self):
        return "serialized"

@pytest.fixture
def mock_valid_attrs():
    return {
        'attr1': MockAttribute(isa='class'),
        'attr2': MockAttribute(isa='other')
    }

@pytest.fixture
def mock_instance(mock_valid_attrs, monkeypatch):
    class MockFieldAttributeBase(FieldAttributeBase):
        attr1 = Mock(serialize=Mock(return_value="serialized_value"))
        attr2 = "value2"
    
    instance = MockFieldAttributeBase()
    monkeypatch.setattr(instance, '_valid_attrs', mock_valid_attrs)
    return instance

def test_dump_attrs(mock_instance):
    result = mock_instance.dump_attrs()
    assert result == {
        'attr1': "serialized_value",
        'attr2': "value2"
    }
