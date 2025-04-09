# file: lib/ansible/playbook/attribute.py:97-98
# asked: {"lines": [97, 98], "branches": []}
# gained: {"lines": [97, 98], "branches": []}

import pytest
from ansible.playbook.attribute import Attribute

def test_attribute_eq():
    attr1 = Attribute(priority=1)
    attr2 = Attribute(priority=1)
    attr3 = Attribute(priority=2)
    
    assert attr1 == attr2
    assert not attr1 == attr3

def test_attribute_ne():
    attr1 = Attribute(priority=1)
    attr2 = Attribute(priority=1)
    attr3 = Attribute(priority=2)
    
    assert not attr1 != attr2
    assert attr1 != attr3

def test_attribute_lt():
    attr1 = Attribute(priority=2)
    attr2 = Attribute(priority=1)
    
    assert attr1 < attr2
    assert not attr2 < attr1

def test_attribute_gt():
    attr1 = Attribute(priority=1)
    attr2 = Attribute(priority=2)
    
    assert attr1 > attr2
    assert not attr2 > attr1

def test_attribute_le():
    attr1 = Attribute(priority=2)
    attr2 = Attribute(priority=1)
    attr3 = Attribute(priority=2)
    
    assert attr1 <= attr2
    assert attr1 <= attr3
    assert not attr2 <= attr1

def test_attribute_ge():
    attr1 = Attribute(priority=1)
    attr2 = Attribute(priority=2)
    attr3 = Attribute(priority=1)
    
    assert attr1 >= attr2
    assert attr1 >= attr3
    assert not attr2 >= attr1
