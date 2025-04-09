# file: lib/ansible/playbook/base.py:740-751
# asked: {"lines": [740, 744, 745, 746, 747, 748, 750, 751], "branches": [[745, 746], [745, 751], [747, 748], [747, 750]]}
# gained: {"lines": [740, 744, 745, 746, 747, 748, 750, 751], "branches": [[745, 746], [745, 751], [747, 748], [747, 750]]}

import pytest
from ansible.playbook.base import FieldAttributeBase
from unittest.mock import Mock

class MockAttribute:
    def __init__(self, isa):
        self.isa = isa

    def serialize(self):
        return "serialized"

@pytest.fixture
def field_attribute_base():
    fab = FieldAttributeBase()
    fab._valid_attrs = {
        'attr1': MockAttribute('class'),
        'attr2': MockAttribute('other')
    }
    fab.attr1 = Mock()
    fab.attr1.serialize = Mock(return_value="serialized_attr1")
    fab.attr2 = "value_attr2"
    return fab

def test_dump_attrs(field_attribute_base):
    attrs = field_attribute_base.dump_attrs()
    assert attrs == {
        'attr1': "serialized_attr1",
        'attr2': "value_attr2"
    }
