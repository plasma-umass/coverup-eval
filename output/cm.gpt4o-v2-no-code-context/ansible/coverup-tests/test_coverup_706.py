# file: lib/ansible/playbook/attribute.py:100-101
# asked: {"lines": [100, 101], "branches": []}
# gained: {"lines": [100, 101], "branches": []}

import pytest
from ansible.playbook.attribute import Attribute

class TestAttribute:
    def test_ne_method(self):
        attr1 = Attribute()
        attr2 = Attribute()
        
        # Mocking the priority attribute
        attr1.priority = 1
        attr2.priority = 2
        
        assert attr1 != attr2  # This should trigger the __ne__ method and return True

    def test_ne_method_equal_priority(self):
        attr1 = Attribute()
        attr2 = Attribute()
        
        # Mocking the priority attribute
        attr1.priority = 1
        attr2.priority = 1
        
        assert not (attr1 != attr2)  # This should trigger the __ne__ method and return False
