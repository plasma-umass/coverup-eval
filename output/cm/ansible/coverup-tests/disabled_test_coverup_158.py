# file lib/ansible/plugins/callback/default.py:190-220
# lines [190, 199, 200, 201, 202, 204, 207, 208, 209, 211, 212, 214, 215, 217, 218, 220]
# branches ['200->201', '200->204', '208->209', '208->211', '211->212', '211->214', '217->218', '217->220']

import pytest
from ansible.plugins.callback.default import CallbackModule
from ansible.utils.display import Display
from ansible.playbook.task import Task
from unittest.mock import MagicMock

# Mock the configuration and task
class MockConfig:
    DISPLAY_ARGS_TO_STDOUT = True

@pytest.fixture
def mock_display(mocker):
    display = Display(verbosity=2)
    mocker.patch.object(display, 'banner')
    mocker.patch.object(display, 'verbosity', new_callable=mocker.PropertyMock(return_value=2))
    return display

@pytest.fixture
def mock_task(mocker):
    task = Task()
    task._uuid = '1234'
    task.args = {'arg1': 'value1', 'arg2': 'value2'}
    task.no_log = False
    task.check_mode = False
    mocker.patch.object(task, 'get_name', return_value="TestTask")
    return task

@pytest.fixture
def callback_module(mock_display):
    callback = CallbackModule()
    callback._display = mock_display
    callback._task_type_cache = {}
    callback._last_task_name = None
    callback._last_task_banner = None
    callback.check_mode_markers = True
    return callback

def test_print_task_banner(mock_display, mock_task, callback_module, mocker):
    # Set the global configuration to our mock
    mocker.patch('ansible.plugins.callback.default.C.DISPLAY_ARGS_TO_STDOUT', new=True)

    # Run the method we want to test
    callback_module._print_task_banner(mock_task)

    # Check that the banner was called with the expected string
    expected_banner = "TASK [TestTask arg1=value1, arg2=value2]"
    mock_display.banner.assert_called_once_with(expected_banner)

    # Check that the verbosity condition was met and _print_task_path was called
    assert callback_module._last_task_banner == mock_task._uuid

    # Clean up after the test
    callback_module._task_type_cache.pop(mock_task._uuid, None)
