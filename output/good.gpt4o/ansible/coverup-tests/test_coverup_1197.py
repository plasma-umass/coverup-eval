# file lib/ansible/playbook/play_context.py:170-185
# lines [176, 177, 181, 182, 185]
# branches ['176->177', '176->181']

import pytest
from unittest import mock
from ansible.playbook.play_context import PlayContext

@pytest.fixture
def mock_context_cliargs():
    with mock.patch('ansible.playbook.play_context.context.CLIARGS', {
        'timeout': '30',
        'private_key_file': '/path/to/private/key',
        'verbosity': '2',
        'start_at_task': 'my_task'
    }):
        yield

def test_set_attributes_from_cli(mock_context_cliargs):
    with mock.patch('ansible.playbook.play_context.Base.__init__', lambda x: None):
        play_context = PlayContext()
        play_context.set_attributes_from_cli()

        assert play_context.timeout == 30
        assert play_context.private_key_file == '/path/to/private/key'
        assert play_context.verbosity == '2'
        assert play_context.start_at_task == 'my_task'
