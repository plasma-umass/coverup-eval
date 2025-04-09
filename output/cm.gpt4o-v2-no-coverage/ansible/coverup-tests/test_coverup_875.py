# file: lib/ansible/playbook/base.py:298-299
# asked: {"lines": [298, 299], "branches": []}
# gained: {"lines": [298, 299], "branches": []}

import pytest
from unittest.mock import MagicMock

from ansible.playbook.base import FieldAttributeBase

@pytest.fixture
def field_attribute_base():
    instance = FieldAttributeBase()
    instance._loader = MagicMock()
    return instance

def test_get_loader(field_attribute_base):
    loader = field_attribute_base.get_loader()
    assert loader is field_attribute_base._loader
