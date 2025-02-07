# file: lib/ansible/playbook/play_context.py:170-185
# asked: {"lines": [170, 176, 177, 181, 182, 185], "branches": [[176, 177], [176, 181]]}
# gained: {"lines": [170, 176, 177, 181, 182, 185], "branches": [[176, 177]]}

import pytest
from ansible.playbook.play_context import PlayContext
from ansible import context
from ansible.utils.context_objects import CLIArgs

@pytest.fixture
def mock_context_cliargs(monkeypatch):
    cliargs = CLIArgs({
        'timeout': '30',
        'private_key_file': '/path/to/private/key',
        'verbosity': 2,
        'start_at_task': 'my_task'
    })
    monkeypatch.setattr(context, 'CLIARGS', cliargs)
    yield
    monkeypatch.undo()

def test_set_attributes_from_cli(mock_context_cliargs):
    pc = PlayContext()
    pc.set_attributes_from_cli()
    
    assert pc.timeout == 30
    assert pc.private_key_file == '/path/to/private/key'
    assert pc.verbosity == 2
    assert pc.start_at_task == 'my_task'
