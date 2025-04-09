# file lib/ansible/plugins/action/include_vars.py:72-151
# lines [72, 75, 77, 78, 80, 81, 84, 85, 86, 87, 88, 89, 90, 91, 92, 94, 96, 97, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 113, 114, 115, 116, 117, 119, 120, 121, 122, 124, 125, 127, 128, 129, 131, 132, 133, 134, 136, 138, 139, 140, 141, 142, 143, 144, 145, 147, 148, 149, 151]
# branches ['77->78', '77->80', '86->87', '86->96', '87->88', '87->89', '89->90', '89->91', '91->92', '91->94', '96->97', '96->100', '103->104', '103->119', '106->107', '106->109', '109->110', '109->113', '113->114', '113->131', '115->116', '115->117', '124->125', '124->131', '131->132', '131->136', '138->139', '138->141', '141->142', '141->147', '143->144', '143->147']

import pytest
from unittest.mock import MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.action.include_vars import ActionModule

# Mock the required components for the ActionModule
@pytest.fixture
def action_module_args():
    task = MagicMock()
    connection = MagicMock()
    play_context = MagicMock()
    loader = MagicMock()
    templar = MagicMock()
    shared_loader_obj = MagicMock()
    return {
        'task': task,
        'connection': connection,
        'play_context': play_context,
        'loader': loader,
        'templar': templar,
        'shared_loader_obj': shared_loader_obj
    }

# Test function to cover missing lines/branches
def test_include_vars_with_invalid_args(action_module_args):
    # Create an instance of the ActionModule with invalid arguments
    action_module_args['task'].args = {'invalid_arg': 'value'}
    action_module = ActionModule(**action_module_args)

    # Expect AnsibleError to be raised due to invalid argument
    with pytest.raises(AnsibleError) as excinfo:
        action_module.run(task_vars={})

    # Verify the exception message
    assert 'invalid_arg is not a valid option in include_vars' in str(excinfo.value)

# Test function to cover mixing file only and dir only arguments
def test_include_vars_with_mixed_args(action_module_args):
    # Create an instance of the ActionModule with mixed arguments
    action_module_args['task'].args = {'file': 'some_file.yml', 'dir': 'some_dir'}
    action_module = ActionModule(**action_module_args)

    # Expect AnsibleError to be raised due to mixing file only and dir only arguments
    with pytest.raises(AnsibleError) as excinfo:
        action_module.run(task_vars={})

    # Verify the exception message
    assert 'You are mixing file only and dir only arguments, these are incompatible' in str(excinfo.value)
