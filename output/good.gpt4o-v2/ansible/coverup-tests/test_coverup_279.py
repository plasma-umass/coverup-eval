# file: lib/ansible/cli/adhoc.py:66-81
# asked: {"lines": [66, 67, 69, 70, 73, 74, 75, 77, 78, 79, 80, 81], "branches": [[73, 74], [73, 77]]}
# gained: {"lines": [66, 67, 69, 70, 73, 74, 75, 77, 78, 79, 80, 81], "branches": [[73, 74], [73, 77]]}

import pytest
from ansible.cli.adhoc import AdHocCLI
from ansible import context
from ansible import constants as C

@pytest.fixture
def setup_context(monkeypatch):
    cliargs = {
        'module_name': 'command',
        'module_args': 'arg1=val1 arg2=val2',
        'task_timeout': 30
    }
    monkeypatch.setattr(context, 'CLIARGS', cliargs)
    return cliargs

def test_play_ds_with_async_and_poll(setup_context):
    adhoc_cli = AdHocCLI(args=['ansible-playbook'])
    pattern = 'localhost'
    async_val = 10
    poll = 5

    result = adhoc_cli._play_ds(pattern, async_val, poll)

    assert result['name'] == 'Ansible Ad-Hoc'
    assert result['hosts'] == pattern
    assert result['gather_facts'] == 'no'
    assert 'async_val' in result['tasks'][0]
    assert result['tasks'][0]['async_val'] == async_val
    assert 'poll' in result['tasks'][0]
    assert result['tasks'][0]['poll'] == poll

def test_play_ds_without_async_and_poll(setup_context):
    adhoc_cli = AdHocCLI(args=['ansible-playbook'])
    pattern = 'localhost'
    async_val = 0
    poll = 0

    result = adhoc_cli._play_ds(pattern, async_val, poll)

    assert result['name'] == 'Ansible Ad-Hoc'
    assert result['hosts'] == pattern
    assert result['gather_facts'] == 'no'
    assert 'async_val' not in result['tasks'][0]
    assert 'poll' not in result['tasks'][0]
