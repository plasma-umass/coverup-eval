# file lib/ansible/plugins/action/fetch.py:36-207
# lines [36, 38, 39, 41, 42, 44, 45, 46, 48, 49, 50, 51, 52, 54, 56, 57, 59, 60, 62, 63, 65, 66, 68, 69, 71, 72, 73, 76, 77, 78, 79, 80, 81, 82, 83, 85, 87, 89, 90, 91, 92, 93, 94, 101, 102, 103, 104, 106, 109, 110, 111, 112, 113, 114, 115, 117, 119, 120, 121, 122, 124, 126, 127, 128, 129, 132, 133, 134, 136, 139, 141, 143, 144, 145, 146, 149, 150, 151, 153, 156, 157, 159, 160, 162, 165, 167, 169, 172, 173, 175, 176, 177, 178, 179, 180, 181, 183, 184, 185, 186, 188, 189, 190, 191, 193, 194, 195, 198, 199, 200, 201, 202, 205, 207]
# branches ['38->39', '38->41', '45->46', '45->48', '56->57', '56->59', '59->60', '59->62', '62->63', '62->65', '65->66', '65->68', '73->76', '73->109', '81->82', '81->85', '90->91', '90->109', '91->92', '91->109', '101->102', '101->106', '110->111', '110->132', '112->113', '112->126', '113->114', '113->117', '119->120', '119->121', '121->122', '121->124', '126->127', '126->128', '128->129', '128->132', '132->133', '132->136', '139->141', '139->143', '143->144', '143->156', '144->145', '144->146', '146->149', '146->151', '151->153', '151->162', '156->157', '156->159', '167->169', '167->198', '172->173', '172->175', '188->189', '188->193']

import pytest
from unittest.mock import MagicMock, patch
from ansible.plugins.action.fetch import ActionModule
from ansible.errors import AnsibleActionFail, AnsibleActionSkip
from ansible.module_utils._text import to_bytes
import os

@pytest.fixture
def mock_connection(mocker):
    connection = mocker.Mock()
    connection._shell = mocker.Mock()
    connection._shell.join_path = lambda *args: os.path.join(*args)
    connection._shell._unquote = lambda x: x
    connection._shell.tmpdir = '/tmp'
    connection.fetch_file = mocker.Mock()
    connection.become = False
    return connection

@pytest.fixture
def mock_loader(mocker):
    loader = mocker.Mock()
    loader.path_dwim = lambda x: x
    return loader

@pytest.fixture
def mock_task(mocker):
    task = mocker.Mock()
    task.args = {
        'src': '/path/to/source',
        'dest': '/path/to/dest',
        'flat': False,
        'fail_on_missing': True,
        'validate_checksum': True
    }
    return task

@pytest.fixture
def mock_play_context(mocker):
    play_context = mocker.Mock()
    play_context.check_mode = False
    play_context.remote_addr = 'localhost'
    return play_context

@pytest.fixture
def mock_action_base(mocker):
    mocker.patch('ansible.plugins.action.fetch.ActionBase.run', return_value={})

@pytest.fixture
def mock_execute_remote_stat(mocker):
    return mocker.patch('ansible.plugins.action.fetch.ActionModule._execute_remote_stat', return_value={'exists': True, 'isdir': False, 'checksum': '12345'})

@pytest.fixture
def mock_execute_module(mocker):
    return mocker.patch('ansible.plugins.action.fetch.ActionModule._execute_module', return_value={'encoding': 'base64', 'content': 'dGVzdA==', 'failed': False})

@pytest.fixture
def mock_checksum(mocker):
    return mocker.patch('ansible.plugins.action.fetch.checksum', return_value='12345')

@pytest.fixture
def mock_secure_hash(mocker):
    return mocker.patch('ansible.plugins.action.fetch.secure_hash', return_value='12345')

@pytest.fixture
def mock_md5(mocker):
    return mocker.patch('ansible.plugins.action.fetch.md5', return_value='12345')

@pytest.fixture
def mock_makedirs_safe(mocker):
    return mocker.patch('ansible.plugins.action.fetch.makedirs_safe')

@pytest.fixture
def mock_remove_tmp_path(mocker):
    return mocker.patch('ansible.plugins.action.fetch.ActionModule._remove_tmp_path')

def test_fetch_run(mock_connection, mock_loader, mock_task, mock_play_context, mock_action_base, mock_execute_remote_stat, mock_execute_module, mock_checksum, mock_secure_hash, mock_md5, mock_makedirs_safe, mock_remove_tmp_path):
    action_module = ActionModule(task=mock_task, connection=mock_connection, play_context=mock_play_context, loader=mock_loader, templar=None, shared_loader_obj=None)
    
    result = action_module.run(task_vars={'inventory_hostname': 'localhost'})
    
    assert result['changed'] == False
    assert result['md5sum'] == '12345'
    assert result['file'] == '/path/to/source'
    assert result['dest'] == '/path/to/dest/localhost/path/to/source'
    assert result['checksum'] == '12345'
    
    mock_remove_tmp_path.assert_called_once_with('/tmp')
