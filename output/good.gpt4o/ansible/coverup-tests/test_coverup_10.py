# file lib/ansible/parsing/mod_args.py:260-346
# lines [260, 267, 269, 270, 271, 276, 280, 282, 283, 286, 288, 289, 290, 291, 292, 297, 300, 301, 302, 303, 304, 305, 306, 308, 309, 310, 312, 314, 316, 317, 319, 320, 322, 323, 324, 327, 328, 329, 330, 331, 332, 334, 335, 336, 337, 338, 339, 340, 342, 343, 344, 346]
# branches ['280->282', '280->286', '286->288', '286->297', '288->289', '288->290', '300->301', '300->327', '303->304', '303->305', '305->306', '305->308', '309->310', '309->312', '314->300', '314->316', '316->317', '316->319', '319->320', '319->322', '327->328', '327->336', '328->329', '328->334', '336->337', '336->346', '339->340', '339->342']

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleParserError
from ansible.parsing.mod_args import ModuleArgsParser

@pytest.fixture
def mock_task_ds():
    return {
        'action': 'some_action',
        'args': {'some_arg': 'some_value'},
        'delegate_to': 'some_delegate'
    }

@pytest.fixture
def mock_task_ds_local_action():
    return {
        'local_action': 'some_local_action',
        'args': {'some_arg': 'some_value'}
    }

@pytest.fixture
def mock_task_ds_conflict():
    return {
        'action': 'some_action',
        'local_action': 'some_local_action',
        'args': {'some_arg': 'some_value'}
    }

@pytest.fixture
def mock_task_ds_no_action():
    return {
        'args': {'some_arg': 'some_value'}
    }

@pytest.fixture
def mock_task_ds_bad_action():
    return {
        'bad_action': 'some_bad_action',
        'args': {'some_arg': 'some_value'}
    }

@pytest.fixture
def mock_task_ds_raw_params():
    return {
        'action': 'some_action',
        'args': {'_raw_params': 'some_raw_params'}
    }

@pytest.fixture
def parser(mock_task_ds):
    parser = ModuleArgsParser()
    parser._task_ds = mock_task_ds
    parser._task_attrs = set()
    parser._collection_list = []
    parser._normalize_parameters = MagicMock(return_value=('some_action', {'some_arg': 'some_value'}))
    return parser

def test_parse_action(parser):
    action, args, delegate_to = parser.parse()
    assert action == 'some_action'
    assert args == {'some_arg': 'some_value'}
    assert delegate_to == 'some_delegate'

def test_parse_local_action(mock_task_ds_local_action):
    parser = ModuleArgsParser()
    parser._task_ds = mock_task_ds_local_action
    parser._task_attrs = set()
    parser._collection_list = []
    parser._normalize_parameters = MagicMock(return_value=('some_local_action', {'some_arg': 'some_value'}))
    
    action, args, delegate_to = parser.parse()
    assert action == 'some_local_action'
    assert args == {'some_arg': 'some_value'}
    assert delegate_to == 'localhost'

def test_parse_conflict(mock_task_ds_conflict):
    parser = ModuleArgsParser()
    parser._task_ds = mock_task_ds_conflict
    parser._task_attrs = set()
    parser._collection_list = []
    parser._normalize_parameters = MagicMock(return_value=('some_action', {'some_arg': 'some_value'}))
    
    with pytest.raises(AnsibleParserError, match="action and local_action are mutually exclusive"):
        parser.parse()

def test_parse_no_action(mock_task_ds_no_action):
    parser = ModuleArgsParser()
    parser._task_ds = mock_task_ds_no_action
    parser._task_attrs = set()
    parser._collection_list = []
    parser._normalize_parameters = MagicMock(return_value=(None, {}))
    
    with pytest.raises(AnsibleParserError, match="couldn't resolve module/action 'args'. This often indicates a misspelling, missing collection, or incorrect module path."):
        parser.parse()

def test_parse_bad_action(mock_task_ds_bad_action):
    parser = ModuleArgsParser()
    parser._task_ds = mock_task_ds_bad_action
    parser._task_attrs = set()
    parser._collection_list = []
    parser._normalize_parameters = MagicMock(return_value=(None, {}))
    
    with pytest.raises(AnsibleParserError, match="couldn't resolve module/action 'bad_action'."):
        parser.parse()

@patch('ansible.parsing.mod_args.Templar')
def test_parse_raw_params(mock_templar, mock_task_ds_raw_params):
    mock_templar_instance = mock_templar.return_value
    mock_templar_instance.is_template.return_value = False
    
    parser = ModuleArgsParser()
    parser._task_ds = mock_task_ds_raw_params
    parser._task_attrs = set()
    parser._collection_list = []
    parser._normalize_parameters = MagicMock(return_value=('some_action', {'_raw_params': 'some_raw_params'}))
    
    with pytest.raises(AnsibleParserError, match="this task 'some_action' has extra params"):
        parser.parse()
