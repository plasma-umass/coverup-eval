# file: lib/ansible/playbook/attribute.py:100-101
# asked: {"lines": [100, 101], "branches": []}
# gained: {"lines": [100, 101], "branches": []}

import pytest
from ansible.playbook.attribute import Attribute

def test_attribute_ne():
    attr1 = Attribute(priority=1)
    attr2 = Attribute(priority=2)
    attr3 = Attribute(priority=1)

    assert attr1 != attr2  # Different priorities
    assert not (attr1 != attr3)  # Same priorities
