# file: lib/ansible/playbook/base.py:301-302
# asked: {"lines": [302], "branches": []}
# gained: {"lines": [302], "branches": []}

import pytest
from ansible.playbook.base import FieldAttributeBase

class MockVariableManager:
    pass

@pytest.fixture
def field_attribute_base_instance(monkeypatch):
    instance = FieldAttributeBase()
    mock_variable_manager = MockVariableManager()
    monkeypatch.setattr(instance, '_variable_manager', mock_variable_manager)
    return instance

def test_get_variable_manager(field_attribute_base_instance):
    result = field_attribute_base_instance.get_variable_manager()
    assert isinstance(result, MockVariableManager)
