# file: lib/ansible/playbook/attribute.py:105-106
# asked: {"lines": [105, 106], "branches": []}
# gained: {"lines": [105, 106], "branches": []}

import pytest
from ansible.playbook.attribute import Attribute

@pytest.fixture
def attribute():
    return Attribute(priority=10)

@pytest.fixture
def other_attribute():
    return Attribute(priority=20)

def test_attribute_lt(attribute, other_attribute):
    assert not attribute < other_attribute
    assert other_attribute < attribute

def test_attribute_eq(attribute, other_attribute):
    other_attribute.priority = 10
    assert attribute == other_attribute

def test_attribute_ne(attribute, other_attribute):
    assert attribute != other_attribute

def test_attribute_gt(attribute, other_attribute):
    assert attribute > other_attribute
    assert not other_attribute > attribute

def test_attribute_le(attribute, other_attribute):
    assert not attribute <= other_attribute
    other_attribute.priority = 10
    assert attribute <= other_attribute

def test_attribute_ge(attribute, other_attribute):
    assert attribute >= other_attribute
    assert not other_attribute >= attribute
    other_attribute.priority = 10
    assert attribute >= other_attribute
