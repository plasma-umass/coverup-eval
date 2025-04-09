# file lib/ansible/playbook/play.py:322-323
# lines [322, 323]
# branches []

import pytest
from ansible.playbook.play import Play

# Assuming the Play class is part of a larger Ansible codebase and has dependencies
# that need to be mocked for isolation.

@pytest.fixture
def play_class(mocker):
    mocker.patch('ansible.playbook.play.Base')
    mocker.patch('ansible.playbook.play.Taggable')
    mocker.patch('ansible.playbook.play.CollectionSearch')
    return Play

def test_get_handlers_returns_copy_of_handlers(play_class, mocker):
    # Setup the Play instance with some mock handlers
    play = play_class()
    mock_handler1 = mocker.Mock()
    mock_handler2 = mocker.Mock()
    play.handlers = [mock_handler1, mock_handler2]

    # Call the method under test
    handlers_copy = play.get_handlers()

    # Assert that we got a copy of the handlers list
    assert handlers_copy == [mock_handler1, mock_handler2]
    assert handlers_copy is not play.handlers  # Ensure it's a copy, not the same list

    # Cleanup is handled by the fixture and pytest's garbage collection
