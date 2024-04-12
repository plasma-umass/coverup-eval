# file lib/ansible/playbook/included_file.py:63-221
# lines [63, 64, 65, 66, 68, 70, 71, 73, 74, 75, 77, 78, 79, 80, 82, 84, 86, 87, 89, 90, 91, 92, 93, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 112, 115, 116, 118, 120, 121, 123, 126, 127, 128, 129, 130, 131, 132, 133, 135, 136, 137, 138, 139, 140, 142, 144, 145, 147, 148, 149, 150, 151, 152, 153, 154, 156, 158, 159, 160, 162, 164, 165, 167, 169, 170, 171, 172, 173, 174, 175, 176, 178, 180, 181, 184, 185, 186, 188, 189, 190, 191, 192, 193, 195, 196, 197, 199, 201, 202, 203, 204, 205, 208, 209, 210, 211, 213, 214, 215, 217, 219, 221]
# branches ['68->70', '68->221', '73->68', '73->74', '74->75', '74->77', '77->78', '77->82', '78->79', '78->80', '84->68', '84->86', '86->87', '86->89', '99->100', '99->101', '101->102', '101->103', '103->104', '103->105', '105->106', '105->107', '107->108', '107->112', '115->116', '115->118', '120->121', '120->184', '123->126', '123->169', '128->129', '128->169', '129->130', '129->132', '132->133', '132->135', '144->145', '144->147', '149->150', '149->162', '153->154', '153->164', '164->165', '164->167', '169->170', '169->180', '170->171', '170->178', '185->186', '185->188', '190->191', '190->195', '191->190', '191->192', '196->197', '196->199', '203->204']

import os
from unittest.mock import MagicMock, patch

import pytest

from ansible.playbook.included_file import IncludedFile
from ansible.playbook.task_include import TaskInclude
from ansible.template import Templar
from ansible.utils.display import Display
from ansible.errors import AnsibleError
from ansible.utils.unsafe_proxy import AnsibleUnsafeText
from ansible.module_utils._text import to_text
from ansible.playbook.handler import Handler
from ansible.playbook.role_include import IncludeRole
from ansible.vars.manager import VariableManager
from ansible.playbook.play import Play
from ansible.inventory.host import Host
from ansible.playbook.task import Task
from ansible import constants as C


@pytest.fixture
def setup_mocks(mocker):
    # Mocking the necessary components for the test
    display_mock = mocker.patch('ansible.utils.display.Display', autospec=True)
    display_mock.deprecated = MagicMock()
    display_mock.warning = MagicMock()

    loader_mock = mocker.MagicMock()
    loader_mock.get_basedir.return_value = '/fake/base/dir'
    loader_mock.path_dwim.return_value = '/fake/dwim/path'
    loader_mock.path_dwim_relative.side_effect = lambda basedir, dirname, include_target, is_role=False: os.path.join(dirname, include_target)

    variable_manager_mock = mocker.MagicMock(spec=VariableManager)
    variable_manager_mock.get_vars.return_value = {}

    iterator_mock = mocker.MagicMock()
    iterator_mock._play = Play()

    templar_mock = mocker.patch('ansible.template.Templar', autospec=True)
    templar_mock.template.side_effect = lambda x: x  # No templating, return the value as is

    os_stat_mock = mocker.patch('os.stat', autospec=True)

    return {
        'display_mock': display_mock,
        'loader_mock': loader_mock,
        'variable_manager_mock': variable_manager_mock,
        'iterator_mock': iterator_mock,
        'templar_mock': templar_mock,
        'os_stat_mock': os_stat_mock,
    }


def test_process_include_results(setup_mocks):
    # Using the setup_mocks fixture to provide mock objects
    loader_mock = setup_mocks['loader_mock']
    variable_manager_mock = setup_mocks['variable_manager_mock']
    iterator_mock = setup_mocks['iterator_mock']
    os_stat_mock = setup_mocks['os_stat_mock']

    # Setting up the constants to be used in the test
    C._ACTION_ALL_INCLUDES = ['include', 'include_tasks', 'import_tasks', 'import_playbook']
    C._ACTION_INCLUDE = 'include'
    C._ACTION_ALL_INCLUDE_TASKS = ['include_tasks', 'import_tasks']

    # Creating a fake result to be processed
    fake_result = MagicMock()
    fake_result._host = Host(name='fake_host')
    fake_result._task = Task()
    fake_result._task.action = 'include_tasks'
    fake_result._task.loop = None
    fake_result._result = {'include': '/fake/include/path'}

    # Creating a fake parent task
    fake_parent_task = TaskInclude()
    fake_parent_task._parent = None
    fake_parent_task.args = {'_raw_params': '/fake/parent/path'}

    # Assigning the fake parent task to the fake result task
    fake_result._task._parent = fake_parent_task

    # Mocking os.stat to simulate the file existence
    os_stat_mock.side_effect = lambda x: x

    # Calling the method under test
    included_files = IncludedFile.process_include_results(
        [fake_result],
        iterator_mock,
        loader_mock,
        variable_manager_mock
    )

    # Assertions to ensure the test is correct and improves coverage
    assert len(included_files) == 1
    assert included_files[0]._filename == loader_mock.path_dwim_relative(loader_mock.get_basedir(), '/fake/parent/path', fake_result._result['include'])
    assert included_files[0]._task == fake_result._task
    assert fake_result._host in included_files[0]._hosts

    # Clean up the constants
    del C._ACTION_ALL_INCLUDES
    del C._ACTION_INCLUDE
    del C._ACTION_ALL_INCLUDE_TASKS
