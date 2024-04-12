# file lib/ansible/plugins/action/include_vars.py:191-206
# lines [199, 200, 201, 202, 203, 204, 205, 206]
# branches ['199->200', '199->206', '201->199', '201->202']

import pytest
from ansible.errors import AnsibleError
from ansible.plugins.action.include_vars import ActionModule

def test_ignore_file_exception(mocker):
    # Mock the ActionModule with a specific ignore_files list containing an invalid regex
    action_module = ActionModule(None, None, None, None, None, None)
    action_module.ignore_files = ['[']

    # Ensure that the invalid regex raises an AnsibleError
    with pytest.raises(AnsibleError) as excinfo:
        action_module._ignore_file('testfile')

    # Check that the exception message is correct
    assert 'Invalid regular expression' in str(excinfo.value)

    # No cleanup required as we are not modifying any persistent state
