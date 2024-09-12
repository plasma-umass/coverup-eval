# file: lib/ansible/playbook/base.py:740-751
# asked: {"lines": [740, 744, 745, 746, 747, 748, 750, 751], "branches": [[745, 746], [745, 751], [747, 748], [747, 750]]}
# gained: {"lines": [740, 744, 745, 746, 747, 748, 750, 751], "branches": [[745, 746], [745, 751], [747, 748], [747, 750]]}

import pytest
from unittest.mock import MagicMock

def test_dump_attrs():
    from ansible.playbook.base import FieldAttributeBase

    class MockAttribute:
        def __init__(self, isa):
            self.isa = isa

    class MockSerialized:
        def serialize(self):
            return "serialized"

    # Create a mock instance of FieldAttributeBase
    instance = FieldAttributeBase()
    instance._valid_attrs = {
        'attr1': MockAttribute('class'),
        'attr2': MockAttribute('other')
    }
    instance.attr1 = MockSerialized()
    instance.attr2 = "value2"

    # Call dump_attrs and verify the output
    result = instance.dump_attrs()
    assert result == {
        'attr1': "serialized",
        'attr2': "value2"
    }

    # Clean up
    del instance

