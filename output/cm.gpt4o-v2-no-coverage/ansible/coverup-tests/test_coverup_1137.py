# file: lib/ansible/playbook/base.py:404-417
# asked: {"lines": [406, 407, 408, 409, 411, 413, 415, 417], "branches": [[406, 407], [406, 408], [408, 409], [408, 411], [413, 415], [413, 417]]}
# gained: {"lines": [406, 407, 408, 409, 411, 413, 415, 417], "branches": [[406, 407], [406, 408], [408, 409], [408, 411], [413, 415], [413, 417]]}

import pytest
from unittest.mock import Mock

from ansible.playbook.base import FieldAttributeBase

class MockPlay:
    __class__ = Mock()
    __class__.__name__ = 'Play'

class MockNotPlay:
    __class__ = Mock()
    __class__.__name__ = 'NotPlay'

def test_play_property_with_play_attribute():
    obj = FieldAttributeBase()
    obj._play = MockPlay()
    assert obj.play == obj._play

def test_play_property_with_parent_play_attribute():
    parent = Mock()
    parent._play = MockPlay()
    obj = FieldAttributeBase()
    obj._parent = parent
    assert obj.play == parent._play

def test_play_property_without_play_attribute():
    obj = FieldAttributeBase()
    obj.__class__.__name__ = 'Play'
    assert obj.play == obj

def test_play_property_with_invalid_play_class():
    obj = FieldAttributeBase()
    obj._play = MockNotPlay()
    assert obj.play is None

def test_play_property_with_parent_invalid_play_class():
    parent = Mock()
    parent._play = MockNotPlay()
    obj = FieldAttributeBase()
    obj._parent = parent
    assert obj.play is None
