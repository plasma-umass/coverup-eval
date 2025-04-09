# file: lib/ansible/cli/adhoc.py:66-81
# asked: {"lines": [66, 67, 69, 70, 73, 74, 75, 77, 78, 79, 80, 81], "branches": [[73, 74], [73, 77]]}
# gained: {"lines": [66, 67, 69, 70, 73, 74, 75, 77, 78, 79, 80, 81], "branches": [[73, 74], [73, 77]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.adhoc import AdHocCLI
from ansible import context

@pytest.fixture
def setup_context():
    context.CLIARGS = {
        'module_name': 'test_module',
        'module_args': 'arg1=val1 arg2=val2',
        'task_timeout': 30
    }
    yield
    context.CLIARGS = {}

@pytest.fixture
def adhoc_cli():
    with patch('ansible.cli.adhoc.CLI.__init__', return_value=None):
        cli = AdHocCLI(None)
        yield cli

def test_play_ds_with_async_and_poll(setup_context, adhoc_cli):
    pattern = 'localhost'
    async_val = 10
    poll = 5

    with patch('ansible.cli.adhoc.parse_kv', return_value={'arg1': 'val1', 'arg2': 'val2'}) as mock_parse_kv:
        result = adhoc_cli._play_ds(pattern, async_val, poll)

    assert result['name'] == "Ansible Ad-Hoc"
    assert result['hosts'] == pattern
    assert result['gather_facts'] == 'no'
    assert result['tasks'][0]['action']['module'] == 'test_module'
    assert result['tasks'][0]['action']['args'] == {'arg1': 'val1', 'arg2': 'val2'}
    assert result['tasks'][0]['timeout'] == 30
    assert result['tasks'][0]['async_val'] == async_val
    assert result['tasks'][0]['poll'] == poll

def test_play_ds_without_async_and_poll(setup_context, adhoc_cli):
    pattern = 'localhost'
    async_val = 0
    poll = 0

    with patch('ansible.cli.adhoc.parse_kv', return_value={'arg1': 'val1', 'arg2': 'val2'}) as mock_parse_kv:
        result = adhoc_cli._play_ds(pattern, async_val, poll)

    assert result['name'] == "Ansible Ad-Hoc"
    assert result['hosts'] == pattern
    assert result['gather_facts'] == 'no'
    assert result['tasks'][0]['action']['module'] == 'test_module'
    assert result['tasks'][0]['action']['args'] == {'arg1': 'val1', 'arg2': 'val2'}
    assert result['tasks'][0]['timeout'] == 30
    assert 'async_val' not in result['tasks'][0]
    assert 'poll' not in result['tasks'][0]

def test_play_ds_with_non_included_module(setup_context, adhoc_cli):
    pattern = 'localhost'
    async_val = 10
    poll = 5

    context.CLIARGS['module_name'] = 'non_included_module'
    with patch('ansible.cli.adhoc.parse_kv', return_value={'arg1': 'val1', 'arg2': 'val2'}) as mock_parse_kv:
        result = adhoc_cli._play_ds(pattern, async_val, poll)

    assert result['name'] == "Ansible Ad-Hoc"
    assert result['hosts'] == pattern
    assert result['gather_facts'] == 'no'
    assert result['tasks'][0]['action']['module'] == 'non_included_module'
    assert result['tasks'][0]['action']['args'] == {'arg1': 'val1', 'arg2': 'val2'}
    assert result['tasks'][0]['timeout'] == 30
    assert result['tasks'][0]['async_val'] == async_val
    assert result['tasks'][0]['poll'] == poll
