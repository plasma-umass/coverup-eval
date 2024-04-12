# file lib/ansible/modules/debconf.py:113-126
# lines [113, 114, 115, 117, 118, 120, 122, 123, 124, 126]
# branches ['117->118', '117->120', '122->123', '122->126']

import pytest
from ansible.module_utils.basic import AnsibleModule

def test_get_selections_success(mocker):
    # Mocking the AnsibleModule methods
    module_mock = mocker.MagicMock(spec=AnsibleModule)
    module_mock.get_bin_path.return_value = '/usr/bin/debconf-show'
    module_mock.run_command.return_value = (0, "package: value\n*package2: value2", "")

    # Mocking the get_selections function
    from ansible.modules.debconf import get_selections

    # Call the function with the mocked module
    selections = get_selections(module_mock, 'package')

    # Assertions to check if the function behaves as expected
    assert selections == {'package': 'value', 'package2': 'value2'}
    module_mock.get_bin_path.assert_called_once_with('debconf-show', True)
    module_mock.run_command.assert_called_once()

def test_get_selections_failure(mocker):
    # Mocking the AnsibleModule methods
    module_mock = mocker.MagicMock(spec=AnsibleModule)
    module_mock.get_bin_path.return_value = '/usr/bin/debconf-show'
    module_mock.run_command.return_value = (1, "", "Error message")
    module_mock.fail_json.side_effect = SystemExit("failure")

    # Mocking the get_selections function
    from ansible.modules.debconf import get_selections

    # Using pytest.raises to check if the correct exception is raised
    with pytest.raises(SystemExit) as e:
        get_selections(module_mock, 'package')

    # Assertions to check if the fail_json method was called
    module_mock.fail_json.assert_called_once_with(msg="Error message")
    module_mock.get_bin_path.assert_called_once_with('debconf-show', True)
    module_mock.run_command.assert_called_once()
    assert str(e.value) == "failure"
