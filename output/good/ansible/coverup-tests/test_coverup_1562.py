# file lib/ansible/playbook/play_context.py:128-154
# lines [133, 135, 136, 138, 139, 141, 143, 144, 147, 150, 151, 153, 154]
# branches ['135->136', '135->138', '150->151', '150->153', '153->exit', '153->154']

import pytest
from ansible.playbook.play_context import PlayContext
from ansible import context
from unittest.mock import MagicMock

# Define a mock Play object with attributes to be used in the test
class MockPlay(object):
    def __init__(self, attributes):
        for key, value in attributes.items():
            setattr(self, key, value)

@pytest.fixture
def mock_cliargs():
    # Backup original CLIARGS
    original_cliargs = context.CLIARGS
    # Set a mock CLIARGS
    context.CLIARGS = MagicMock()
    context.CLIARGS.get.return_value = None
    yield
    # Restore original CLIARGS after test
    context.CLIARGS = original_cliargs

def test_play_context_initialization_with_play_and_passwords(mocker, mock_cliargs):
    # Mock the set_attributes_from_cli and set_attributes_from_play methods
    mocker.patch.object(PlayContext, 'set_attributes_from_cli')
    mocker.patch.object(PlayContext, 'set_attributes_from_play')

    # Create a mock play object with some attributes
    mock_play = MockPlay({'name': 'test_play', 'hosts': 'localhost'})

    # Create a passwords dictionary
    passwords = {'conn_pass': 'password123', 'become_pass': 'become123'}

    # Initialize PlayContext with mock play and passwords
    play_context = PlayContext(play=mock_play, passwords=passwords)

    # Assertions to ensure that the methods were called and attributes are set correctly
    assert play_context.password == 'password123'
    assert play_context.become_pass == 'become123'
    assert play_context._become_plugin is None
    assert play_context.prompt == ''
    assert play_context.success_key == ''
    assert play_context.connection_lockfd is None

    # Assert that the set_attributes_from_cli and set_attributes_from_play methods were called
    PlayContext.set_attributes_from_cli.assert_called_once()
    PlayContext.set_attributes_from_play.assert_called_once_with(mock_play)

    # Clean up by stopping the patcher
    mocker.stopall()
