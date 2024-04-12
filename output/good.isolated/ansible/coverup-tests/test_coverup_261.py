# file lib/ansible/playbook/base.py:404-417
# lines [404, 405, 406, 407, 408, 409, 411, 413, 415, 417]
# branches ['406->407', '406->408', '408->409', '408->411', '413->415', '413->417']

import pytest
from ansible.playbook.base import FieldAttributeBase

# Mock class to simulate the 'Play' class
class MockPlay(FieldAttributeBase):
    def __init__(self):
        self.__class__.__name__ = 'Play'

# Test function to cover the missing lines/branches
def test_field_attribute_base_play_property():
    # Create an instance of FieldAttributeBase
    field_attribute_base = FieldAttributeBase()

    # Case 1: _play attribute is set directly on the instance
    mock_play_instance = MockPlay()
    field_attribute_base._play = mock_play_instance
    assert field_attribute_base.play == mock_play_instance

    # Case 2: _play attribute is set on the _parent attribute of the instance
    field_attribute_base._parent = FieldAttributeBase()
    field_attribute_base._parent._play = mock_play_instance
    assert field_attribute_base.play == mock_play_instance

    # Case 3: Neither _play nor _parent._play is set, should return None
    del field_attribute_base._play  # Remove _play from the instance itself
    del field_attribute_base._parent._play  # Remove _play from the parent
    assert field_attribute_base.play is None

    # Case 4: _play is set but is not an instance of 'Play', should return None
    field_attribute_base._play = FieldAttributeBase()  # Not an instance of 'Play'
    assert field_attribute_base.play is None

    # Clean up by deleting the mock attributes
    if hasattr(field_attribute_base, '_play'):
        del field_attribute_base._play
    if hasattr(field_attribute_base, '_parent'):
        del field_attribute_base._parent
