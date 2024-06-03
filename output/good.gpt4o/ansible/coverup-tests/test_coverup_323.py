# file lib/ansible/cli/adhoc.py:66-81
# lines [66, 67, 69, 70, 73, 74, 75, 77, 78, 79, 80, 81]
# branches ['73->74', '73->77']

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.adhoc import AdHocCLI
import ansible.constants as C
import ansible.context as context

@pytest.fixture
def mock_context_cliargs():
    original_cliargs = context.CLIARGS
    context.CLIARGS = {
        'module_name': 'test_module',
        'module_args': 'arg1=val1 arg2=val2',
        'task_timeout': 30
    }
    yield
    context.CLIARGS = original_cliargs

@pytest.fixture
def mock_cli_args():
    with patch('ansible.cli.adhoc.CLI.__init__', return_value=None):
        yield

def test_play_ds_with_async_and_poll(mock_context_cliargs, mock_cli_args):
    cli = AdHocCLI(args=[])
    
    pattern = 'localhost'
    async_val = 10
    poll = 5
    
    with patch('ansible.cli.adhoc.parse_kv', return_value={'arg1': 'val1', 'arg2': 'val2'}) as mock_parse_kv:
        result = cli._play_ds(pattern, async_val, poll)
        
        assert result['name'] == "Ansible Ad-Hoc"
        assert result['hosts'] == pattern
        assert result['gather_facts'] == 'no'
        assert len(result['tasks']) == 1
        task = result['tasks'][0]
        assert task['action']['module'] == 'test_module'
        assert task['action']['args'] == {'arg1': 'val1', 'arg2': 'val2'}
        assert task['timeout'] == 30
        assert task['async_val'] == async_val
        assert task['poll'] == poll

def test_play_ds_without_async_and_poll(mock_context_cliargs, mock_cli_args):
    cli = AdHocCLI(args=[])
    
    pattern = 'localhost'
    async_val = 0
    poll = 0
    
    with patch('ansible.cli.adhoc.parse_kv', return_value={'arg1': 'val1', 'arg2': 'val2'}) as mock_parse_kv:
        result = cli._play_ds(pattern, async_val, poll)
        
        assert result['name'] == "Ansible Ad-Hoc"
        assert result['hosts'] == pattern
        assert result['gather_facts'] == 'no'
        assert len(result['tasks']) == 1
        task = result['tasks'][0]
        assert task['action']['module'] == 'test_module'
        assert task['action']['args'] == {'arg1': 'val1', 'arg2': 'val2'}
        assert task['timeout'] == 30
        assert 'async_val' not in task
        assert 'poll' not in task
