# file lib/ansible/playbook/play.py:101-102
# lines [102]
# branches []

import pytest
from ansible.playbook.play import Play

# Assuming the Play class has a method get_name() that we need to cover

# Mock class to replace the actual Base and CollectionSearch classes
class MockBaseCollectionSearch:
    def __init__(self, *args, **kwargs):
        pass

# Test function to cover the __repr__ method in Play class
def test_play_repr(mocker):
    # Mock the get_name method to return a fixed value
    mocker.patch.object(Play, 'get_name', return_value='test_play_name')
    
    # Create an instance of the Play class
    play_instance = Play()

    # Call the __repr__ method and assert the return value
    assert repr(play_instance) == 'test_play_name', "The __repr__ method did not return the expected play name"

    # Verify that get_name was called once
    Play.get_name.assert_called_once()
