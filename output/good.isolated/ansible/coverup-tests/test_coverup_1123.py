# file lib/ansible/playbook/included_file.py:63-221
# lines [65, 66, 68, 70, 71, 73, 74, 75, 77, 78, 79, 80, 82, 84, 86, 87, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 112, 115, 116, 118, 120, 121, 123, 126, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 142, 144, 145, 147, 148, 149, 150, 151, 152, 153, 154, 156, 158, 159, 160, 162, 164, 165, 167, 169, 170, 171, 172, 173, 174, 175, 176, 178, 180, 181, 184, 185, 186, 188, 189, 190, 191, 192, 193, 195, 196, 197, 199, 201, 202, 203, 204, 205, 208, 209, 210, 211, 213, 214, 215, 217, 219, 221]
# branches ['68->70', '68->221', '73->68', '73->74', '74->75', '74->77', '77->78', '77->82', '78->79', '78->80', '84->68', '84->86', '86->87', '86->89', '99->100', '99->101', '101->102', '101->103', '103->104', '103->105', '105->106', '105->107', '107->108', '107->112', '115->116', '115->118', '120->121', '120->184', '123->126', '123->169', '128->129', '128->169', '129->130', '129->132', '132->133', '132->135', '144->145', '144->147', '149->150', '149->162', '153->154', '153->164', '164->165', '164->167', '169->170', '169->180', '170->171', '170->178', '185->186', '185->188', '190->191', '190->195', '191->190', '191->192', '196->197', '196->199', '203->204']

import os
import pytest
from ansible.playbook.included_file import IncludedFile
from ansible.playbook.task_include import TaskInclude
from ansible.playbook.handler import Handler
from ansible.template import Templar
from ansible.utils.display import Display
from ansible.errors import AnsibleError
from ansible.utils.sentinel import Sentinel
from ansible.utils.unsafe_proxy import AnsibleUnsafeText
from ansible.module_utils._text import to_text
from ansible.vars.manager import VariableManager
from ansible.playbook.play import Play
from ansible.playbook.task import Task
from ansible.inventory.host import Host
from ansible.parsing.dataloader import DataLoader
from ansible.utils.collection_loader import AnsibleCollectionConfig

# Mock the constants
class C:
    _ACTION_ALL_INCLUDES = ['include', 'include_tasks', 'import_playbook', 'import_tasks']
    _ACTION_INCLUDE = 'include'
    _ACTION_ALL_INCLUDE_TASKS = ['include_tasks', 'import_tasks']

# Mock the display module
display = Display()

# Mock the remove_omit function
def remove_omit(d, omit_token):
    return {k: v for k, v in d.items() if v != omit_token}

# Mock the IncludeRole class
class IncludeRole(TaskInclude):
    def __init__(self, role_path):
        self._role_path = role_path

@pytest.fixture
def setup_loader(mocker):
    loader = DataLoader()
    mocker.patch.object(loader, 'get_basedir', return_value='/fake/base/dir')
    mocker.patch.object(loader, 'path_dwim', return_value='/fake/path_dwim')
    mocker.patch.object(loader, 'path_dwim_relative', return_value='/fake/path_dwim_relative')
    return loader

@pytest.fixture
def setup_variable_manager(mocker):
    variable_manager = VariableManager()
    mocker.patch.object(variable_manager, 'get_vars', return_value={})
    return variable_manager

@pytest.fixture
def setup_iterator(mocker):
    iterator = mocker.MagicMock()
    iterator._play = Play()
    return iterator

@pytest.fixture
def setup_original_task(mocker):
    original_task = Task()
    original_task.action = 'include_tasks'
    original_task.loop = None
    original_task.no_log = False
    original_task._parent = None
    return original_task

@pytest.fixture
def setup_host():
    return Host(name='fake-host')

@pytest.fixture
def setup_result(mocker, setup_original_task, setup_host):
    result = mocker.MagicMock()
    result._host = setup_host
    result._task = setup_original_task
    result._result = {'include': '/fake/include/path'}
    return result

def test_process_include_results(setup_loader, setup_variable_manager, setup_iterator, setup_original_task, setup_host, setup_result):
    results = [setup_result]

    included_files = IncludedFile.process_include_results(results, setup_iterator, setup_loader, setup_variable_manager)

    assert len(included_files) == 1
    inc_file = included_files[0]
    assert inc_file._filename == '/fake/path_dwim'
    assert inc_file._hosts == [setup_host]

    # Cleanup
    if os.path.exists('/fake/base/dir'):
        os.rmdir('/fake/base/dir')
    if os.path.exists('/fake/path_dwim'):
        os.remove('/fake/path_dwim')
    if os.path.exists('/fake/path_dwim_relative'):
        os.remove('/fake/path_dwim_relative')
