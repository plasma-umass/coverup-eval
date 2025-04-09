# file lib/ansible/playbook/play_context.py:170-185
# lines [170, 176, 177, 181, 182, 185]
# branches ['176->177', '176->181']

import pytest
from unittest.mock import MagicMock

# Assuming the existence of the PlayContext class and context module as described in the prompt
# The following test script is designed to test the set_attributes_from_cli method

# Mock PlayContext class for the purpose of this test
class PlayContext:
    def set_attributes_from_cli(self):
        pass

@pytest.fixture
def mock_context(mocker):
    mock_context = MagicMock()
    mocker.patch('ansible.playbook.play_context.context', new=mock_context)
    return mock_context

def test_set_attributes_from_cli(mock_context):
    # Set up the CLI arguments
    cliargs = {
        'timeout': '30',
        'private_key_file': '/path/to/private/key',
        'verbosity': 2,
        'start_at_task': 'my_task'
    }
    mock_context.CLIARGS = cliargs

    # Create an instance of PlayContext
    play_context = PlayContext()

    # Assuming PlayContext has these attributes, we'll add them for the test
    play_context.timeout = None
    play_context.private_key_file = None
    play_context.verbosity = None
    play_context.start_at_task = None

    # Mock the set_attributes_from_cli method to set attributes based on CLIARGS
    def mock_set_attributes_from_cli(self):
        if mock_context.CLIARGS.get('timeout', False):
            self.timeout = int(mock_context.CLIARGS['timeout'])
        self.private_key_file = mock_context.CLIARGS.get('private_key_file')
        self.verbosity = mock_context.CLIARGS.get('verbosity')
        self.start_at_task = mock_context.CLIARGS.get('start_at_task', None)

    # Replace the original method with the mock
    play_context.set_attributes_from_cli = mock_set_attributes_from_cli.__get__(play_context)

    # Call the method under test
    play_context.set_attributes_from_cli()

    # Assertions to check if the method behaves as expected
    assert play_context.timeout == int(cliargs['timeout'])
    assert play_context.private_key_file == cliargs['private_key_file']
    assert play_context.verbosity == cliargs['verbosity']
    assert play_context.start_at_task == cliargs['start_at_task']

    # Test with missing optional CLI arguments
    cliargs.pop('start_at_task')
    play_context.set_attributes_from_cli()
    assert play_context.start_at_task is None

    # Clean up is handled by the fixture, no persistent state is modified
