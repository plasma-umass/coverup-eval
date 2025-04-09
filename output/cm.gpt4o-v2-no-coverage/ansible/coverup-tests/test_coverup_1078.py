# file: lib/ansible/playbook/play_context.py:187-316
# asked: {"lines": [197, 201, 202, 203, 210, 214, 215, 217, 218, 219, 220, 221, 227, 228, 229, 231, 232, 236, 237, 238, 240, 241, 243, 246, 247, 248, 250, 252, 255, 256, 257, 259, 260, 261, 262, 263, 265, 266, 267, 268, 269, 270, 271, 276, 277, 278, 281, 282, 285, 289, 290, 291, 293, 294, 295, 296, 297, 298, 302, 303, 304, 307, 308, 310, 311, 313, 314, 316], "branches": [[201, 202], [201, 210], [202, 201], [202, 203], [210, 214], [210, 252], [218, 219], [218, 227], [219, 218], [219, 220], [227, 228], [227, 231], [228, 227], [228, 229], [236, 237], [236, 240], [237, 236], [237, 238], [240, 241], [240, 243], [246, 247], [246, 250], [247, 246], [247, 248], [255, 256], [255, 259], [256, 255], [256, 257], [260, 261], [260, 276], [261, 260], [261, 262], [262, 263], [262, 265], [265, 266], [265, 269], [266, 261], [266, 267], [269, 261], [269, 270], [276, 277], [276, 281], [277, 276], [277, 278], [281, 282], [281, 285], [285, 289], [285, 302], [289, 290], [289, 293], [290, 289], [290, 291], [295, 296], [295, 297], [297, 289], [297, 298], [302, 303], [302, 307], [303, 304], [303, 307], [307, 308], [307, 310], [310, 311], [310, 313], [313, 314], [313, 316]]}
# gained: {"lines": [197, 201, 202, 203, 210, 214, 215, 217, 218, 219, 220, 221, 227, 228, 229, 236, 237, 238, 246, 247, 248, 252, 255, 256, 259, 260, 261, 262, 263, 265, 266, 267, 268, 269, 270, 271, 276, 277, 278, 281, 285, 289, 290, 291, 302, 303, 304, 307, 308, 310, 311, 313, 314, 316], "branches": [[201, 202], [201, 210], [202, 201], [202, 203], [210, 214], [210, 252], [218, 219], [219, 220], [227, 228], [228, 229], [236, 237], [237, 238], [246, 247], [247, 248], [255, 256], [255, 259], [256, 255], [260, 261], [260, 276], [261, 260], [261, 262], [262, 263], [262, 265], [265, 266], [265, 269], [266, 261], [266, 267], [269, 261], [269, 270], [276, 277], [276, 281], [277, 276], [277, 278], [281, 285], [285, 289], [285, 302], [289, 290], [290, 291], [302, 303], [302, 307], [303, 304], [307, 308], [307, 310], [310, 311], [313, 314]]}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.play_context import PlayContext
from ansible import constants as C

@pytest.fixture
def mock_task():
    task = Mock()
    task.delegate_to = None
    task.remote_user = 'remote_user'
    task.check_mode = True
    task.diff = True
    return task

@pytest.fixture
def mock_variables():
    return {
        'ansible_delegated_vars': {
            'delegated_host': {
                'ansible_connection': 'ssh',
                'ansible_ssh_host': '192.168.1.1',
                'ansible_ssh_port': 22,
                'ansible_ssh_user': 'user'
            }
        },
        'ansible_connection': 'local',
        'ansible_ssh_host': '127.0.0.1',
        'ansible_ssh_port': 2222,
        'ansible_ssh_user': 'local_user'
    }

@pytest.fixture
def mock_templar():
    templar = Mock()
    templar.template = Mock(return_value='delegated_host')
    return templar

@pytest.fixture
def play_context():
    return PlayContext()

def test_set_task_and_variable_override_no_delegate(play_context, mock_task, mock_variables, mock_templar):
    new_info = play_context.set_task_and_variable_override(mock_task, mock_variables, mock_templar)
    
    assert new_info.remote_user == 'local_user'
    assert new_info.check_mode is True
    assert new_info.diff is True
    assert new_info.connection == 'local'
    assert new_info.port == 2222
    assert new_info.executable == C.DEFAULT_EXECUTABLE

def test_set_task_and_variable_override_with_delegate(play_context, mock_task, mock_variables, mock_templar):
    mock_task.delegate_to = 'delegated_host'
    new_info = play_context.set_task_and_variable_override(mock_task, mock_variables, mock_templar)
    
    assert new_info.remote_user == 'user'
    assert new_info.check_mode is True
    assert new_info.diff is True
    assert new_info.connection == 'ssh'
    assert new_info.port == 22
    assert new_info.executable == C.DEFAULT_EXECUTABLE

def test_set_task_and_variable_override_no_log(play_context, mock_task, mock_variables, mock_templar):
    mock_task.no_log = None
    new_info = play_context.set_task_and_variable_override(mock_task, mock_variables, mock_templar)
    
    assert new_info.no_log == C.DEFAULT_NO_LOG

def test_set_task_and_variable_override_become_pass(play_context, mock_task, mock_variables, mock_templar):
    mock_variables['ansible_become_pass'] = 'password'
    new_info = play_context.set_task_and_variable_override(mock_task, mock_variables, mock_templar)
    
    assert new_info.port == 2222
    assert new_info.executable == C.DEFAULT_EXECUTABLE
