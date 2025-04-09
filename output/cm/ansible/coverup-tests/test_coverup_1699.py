# file lib/ansible/playbook/base.py:404-417
# lines [409]
# branches ['408->409']

import pytest
from ansible.playbook.base import FieldAttributeBase

class MockPlay(object):
    __class__ = type('Play', (object,), {})

class MockParent(object):
    def __init__(self, play):
        self._play = play

@pytest.fixture
def mock_play():
    return MockPlay()

@pytest.fixture
def mock_parent(mock_play):
    return MockParent(mock_play)

@pytest.fixture
def field_attribute_base():
    return FieldAttributeBase()

def test_field_attribute_base_play_property_with_parent_play(mock_play, mock_parent, field_attribute_base):
    # Set up the parent with a play object
    field_attribute_base._parent = mock_parent

    # Assert that the play property returns the play from the parent
    assert field_attribute_base.play == mock_play

    # Clean up by removing the parent attribute
    del field_attribute_base._parent

def test_field_attribute_base_play_property_without_parent_or_play(field_attribute_base):
    # Assert that the play property returns None when there is no _play or _parent._play
    assert field_attribute_base.play is None

    # No clean up necessary as no attributes were set
