# file: lib/ansible/playbook/base.py:298-299
# asked: {"lines": [299], "branches": []}
# gained: {"lines": [299], "branches": []}

import pytest
from ansible.playbook.base import FieldAttributeBase

class MockLoader:
    pass

@pytest.fixture
def field_attribute_base(monkeypatch):
    instance = FieldAttributeBase()
    mock_loader = MockLoader()
    monkeypatch.setattr(instance, '_loader', mock_loader)
    return instance

def test_get_loader(field_attribute_base):
    loader = field_attribute_base.get_loader()
    assert loader is not None
    assert isinstance(loader, MockLoader)
