# file lib/ansible/playbook/play.py:101-102
# lines [102]
# branches []

import pytest
from ansible.playbook.play import Play

# Assuming the Play class has a method get_name() that we need to cover
# and that it is initialized properly with the required arguments.

@pytest.fixture
def mock_play(mocker):
    # Mock the Play class with a mock get_name method
    mocker.patch.object(Play, 'get_name', return_value='test_play_name')
    return Play()

def test_play_repr(mock_play):
    # Test the __repr__ method to ensure it calls get_name
    assert repr(mock_play) == 'test_play_name', "The __repr__ method should return the result of get_name"
    mock_play.get_name.assert_called_once_with()

# Clean up is handled by pytest fixtures automatically
