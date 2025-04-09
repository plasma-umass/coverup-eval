# file: lib/ansible/playbook/attribute.py:97-98
# asked: {"lines": [97, 98], "branches": []}
# gained: {"lines": [97, 98], "branches": []}

import pytest
from ansible.playbook.attribute import Attribute

class TestAttribute:
    def test_eq_true(self):
        attr1 = Attribute()
        attr2 = Attribute()
        attr1.priority = 1
        attr2.priority = 1
        assert attr1 == attr2

    def test_eq_false(self):
        attr1 = Attribute()
        attr2 = Attribute()
        attr1.priority = 1
        attr2.priority = 2
        assert attr1 != attr2
