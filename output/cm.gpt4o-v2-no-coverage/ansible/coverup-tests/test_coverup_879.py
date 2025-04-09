# file: lib/ansible/playbook/attribute.py:111-112
# asked: {"lines": [111, 112], "branches": []}
# gained: {"lines": [111, 112], "branches": []}

import pytest
from ansible.playbook.attribute import Attribute

class TestAttribute:
    
    def test_le(self):
        attr1 = Attribute(priority=1)
        attr2 = Attribute(priority=2)
        
        assert (attr1.__le__(attr2)) == False
        assert (attr2.__le__(attr1)) == True
