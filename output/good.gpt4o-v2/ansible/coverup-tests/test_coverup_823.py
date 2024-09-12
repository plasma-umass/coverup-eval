# file: lib/ansible/playbook/attribute.py:97-98
# asked: {"lines": [97, 98], "branches": []}
# gained: {"lines": [97, 98], "branches": []}

import pytest
from ansible.playbook.attribute import Attribute

def test_attribute_eq():
    attr1 = Attribute(priority=10)
    attr2 = Attribute(priority=10)
    attr3 = Attribute(priority=5)

    assert attr1 == attr2  # Should be True, same priority
    assert attr1 != attr3  # Should be True, different priority
