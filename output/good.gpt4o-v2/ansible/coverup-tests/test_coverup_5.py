# file: lib/ansible/playbook/included_file.py:63-221
# asked: {"lines": [63, 64, 65, 66, 68, 70, 71, 73, 74, 75, 77, 78, 79, 80, 82, 84, 86, 87, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 112, 115, 116, 118, 120, 121, 123, 126, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 142, 144, 145, 147, 148, 149, 150, 151, 152, 153, 154, 156, 158, 159, 160, 162, 164, 165, 167, 169, 170, 171, 172, 173, 174, 175, 176, 178, 180, 181, 184, 185, 186, 188, 189, 190, 191, 192, 193, 195, 196, 197, 199, 201, 202, 203, 204, 205, 208, 209, 210, 211, 213, 214, 215, 217, 219, 221], "branches": [[68, 70], [68, 221], [73, 68], [73, 74], [74, 75], [74, 77], [77, 78], [77, 82], [78, 79], [78, 80], [84, 68], [84, 86], [86, 87], [86, 89], [99, 100], [99, 101], [101, 102], [101, 103], [103, 104], [103, 105], [105, 106], [105, 107], [107, 108], [107, 112], [115, 116], [115, 118], [120, 121], [120, 184], [123, 126], [123, 169], [128, 129], [128, 169], [129, 130], [129, 132], [132, 133], [132, 135], [144, 145], [144, 147], [149, 150], [149, 162], [153, 154], [153, 164], [164, 165], [164, 167], [169, 170], [169, 180], [170, 171], [170, 178], [185, 186], [185, 188], [190, 191], [190, 195], [191, 190], [191, 192], [196, 197], [196, 199], [203, 204]]}
# gained: {"lines": [63, 64, 65, 66, 68, 70, 71, 73, 74, 75, 77, 82, 84, 86, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99, 101, 103, 105, 107, 112, 115, 116, 118, 120, 121, 123, 169, 170, 178, 180, 181, 201, 202, 203, 204, 205, 209, 210, 211, 213, 214, 219, 221], "branches": [[68, 70], [68, 221], [73, 74], [74, 75], [77, 82], [84, 68], [84, 86], [86, 89], [99, 101], [101, 103], [103, 105], [105, 107], [107, 112], [115, 116], [120, 121], [123, 169], [169, 170], [170, 178], [203, 204]]}

import pytest
from unittest.mock import Mock, patch
from ansible.playbook.included_file import IncludedFile

@pytest.fixture
def mock_iterator():
    iterator = Mock()
    iterator._play = Mock()
    return iterator

@pytest.fixture
def mock_loader():
    loader = Mock()
    loader.get_basedir.return_value = '/basedir'
    loader.path_dwim.return_value = 'some_include_file.yml'
    return loader

@pytest.fixture
def mock_variable_manager():
    variable_manager = Mock()
    variable_manager.get_vars.return_value = {}
    return variable_manager

@pytest.fixture
def mock_result():
    return Mock()

@pytest.fixture
def mock_task():
    task = Mock()
    task.action = 'include'
    task.loop = None
    task.no_log = False
    task._parent = None
    task._role = None
    task.get_search_path.return_value = ['/search_path']
    return task

@pytest.fixture
def mock_host():
    return Mock()

def test_process_include_results(mock_iterator, mock_loader, mock_variable_manager, mock_result, mock_task, mock_host):
    mock_result._host = mock_host
    mock_result._task = mock_task
    mock_result._result = {'include_args': {}, 'include': 'some_include_file.yml'}

    results = [mock_result]

    with patch('ansible.playbook.included_file.display') as mock_display, \
         patch('ansible.playbook.included_file.Templar') as MockTemplar, \
         patch('ansible.playbook.included_file.os.path.exists', return_value=True), \
         patch('ansible.playbook.included_file.os.stat'):
        
        MockTemplar.return_value.template.side_effect = lambda x: x

        included_files = IncludedFile.process_include_results(results, mock_iterator, mock_loader, mock_variable_manager)

        assert len(included_files) == 1
        assert included_files[0]._filename == 'some_include_file.yml'
        assert included_files[0]._args == {}
        assert included_files[0]._vars == {}
        assert included_files[0]._task == mock_task
        assert included_files[0]._hosts == [mock_host]
