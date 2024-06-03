# file lib/ansible/parsing/mod_args.py:260-346
# lines [304, 306, 317, 334, 335, 340]
# branches ['303->304', '305->306', '316->317', '319->322', '328->334', '339->340']

import pytest
from unittest.mock import MagicMock, patch
from ansible.parsing.mod_args import ModuleArgsParser, AnsibleParserError

@pytest.fixture
def mock_task_ds():
    return {
        'action': 'some_action',
        'args': {'_raw_params': 'some_params'},
        'delegate_to': 'some_delegate'
    }

@pytest.fixture
def parser(mock_task_ds):
    parser = ModuleArgsParser()
    parser._task_ds = mock_task_ds
    parser._task_attrs = set()
    parser._collection_list = []
    return parser

def test_parse_action_and_local_action_conflict(parser, mock_task_ds):
    mock_task_ds['local_action'] = 'some_local_action'
    with pytest.raises(AnsibleParserError, match="action and local_action are mutually exclusive"):
        parser.parse()

def test_parse_conflicting_action_statements(parser, mock_task_ds):
    mock_task_ds['some_module'] = 'some_value'
    with patch('ansible.parsing.mod_args.action_loader.find_plugin_with_context') as mock_find_plugin:
        mock_find_plugin.return_value.resolved = True
        mock_find_plugin.return_value.redirect_list = ['redirect']
        with pytest.raises(AnsibleParserError, match="conflicting action statements"):
            parser.parse()

def test_parse_no_module_action_detected(parser, mock_task_ds):
    mock_task_ds.clear()
    with pytest.raises(AnsibleParserError, match="no module/action detected in task"):
        parser.parse()

def test_parse_template_raw_params(parser, mock_task_ds):
    mock_task_ds['action'] = 'some_action'
    mock_task_ds['args'] = {'_raw_params': '{{ some_template }}'}
    with patch('ansible.parsing.mod_args.Templar.is_template', return_value=True):
        action, args, delegate_to = parser.parse()
        assert args['_variable_params'] == '{{ some_template }}'

def test_parse_non_template_raw_params(parser, mock_task_ds):
    mock_task_ds['action'] = 'some_action'
    mock_task_ds['args'] = {'_raw_params': 'some_params'}
    with patch('ansible.parsing.mod_args.Templar.is_template', return_value=False):
        with pytest.raises(AnsibleParserError, match="this task 'some_action' has extra params"):
            parser.parse()
