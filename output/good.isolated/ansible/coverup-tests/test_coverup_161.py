# file lib/ansible/modules/dpkg_selections.py:55-82
# lines [55, 56, 57, 58, 59, 61, 64, 66, 67, 70, 71, 72, 74, 76, 78, 79, 81, 82]
# branches ['71->72', '71->74', '78->79', '78->81']

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_ansible_module(mocker):
    mock_module = MagicMock()
    mocker.patch('ansible.modules.dpkg_selections.AnsibleModule', return_value=mock_module)
    return mock_module

def test_dpkg_selections(mock_ansible_module):
    mock_module = mock_ansible_module
    mock_module.params = {
        'name': 'fakepackage',
        'selection': 'install'
    }
    mock_module.check_mode = False
    mock_module.get_bin_path.return_value = '/usr/bin/dpkg'
    mock_module.run_command.side_effect = [
        (0, 'fakepackage\tdeinstall', ''),  # Simulate dpkg --get-selections output
        (0, '', '')  # Simulate dpkg --set-selections output
    ]

    from ansible.modules.dpkg_selections import main
    main()

    assert mock_module.run_command.call_count == 2
    mock_module.run_command.assert_any_call(['/usr/bin/dpkg', '--get-selections', 'fakepackage'], check_rc=True)
    mock_module.run_command.assert_any_call(['/usr/bin/dpkg', '--set-selections'], data="fakepackage install", check_rc=True)
    mock_module.exit_json.assert_called_once_with(changed=True, before='deinstall', after='install')
