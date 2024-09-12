# file: lib/ansible/modules/pip.py:363-378
# asked: {"lines": [366, 367, 368, 369, 372, 373, 374, 375, 376, 378], "branches": [[372, 373], [372, 378], [375, 376], [375, 378]]}
# gained: {"lines": [366, 367, 368, 369, 372, 373, 374, 375, 376, 378], "branches": [[372, 373], [372, 378], [375, 376], [375, 378]]}

import pytest
from unittest.mock import Mock, patch
from ansible.modules.pip import _get_packages

@pytest.fixture
def mock_module():
    module = Mock()
    module.run_command = Mock()
    module.get_bin_path = Mock(return_value='/usr/bin/locale')
    return module

def test_get_packages_list_success(mock_module):
    mock_module.run_command.side_effect = [
        (0, 'C\n', ''),  # locale -a command
        (0, 'package==1.0.0\n', '')  # pip list command
    ]
    pip = ['pip']
    chdir = '/some/path'
    
    command, out, err = _get_packages(mock_module, pip, chdir)
    
    assert command == 'pip list --format=freeze'
    assert out == 'package==1.0.0\n'
    assert err == ''
    assert mock_module.run_command.call_count == 2
    mock_module.run_command.assert_any_call(['/usr/bin/locale', '-a'])
    mock_module.run_command.assert_any_call(['pip', 'list', '--format=freeze'], cwd=chdir, environ_update={'LANG': 'C', 'LC_ALL': 'C', 'LC_MESSAGES': 'C'})

def test_get_packages_list_fail_freeze_success(mock_module):
    mock_module.run_command.side_effect = [
        (0, 'C\n', ''),  # locale -a command
        (1, '', 'error'),  # pip list fails
        (0, 'package==1.0.0\n', '')  # pip freeze succeeds
    ]
    pip = ['pip']
    chdir = '/some/path'
    
    command, out, err = _get_packages(mock_module, pip, chdir)
    
    assert command == 'pip freeze'
    assert out == 'package==1.0.0\n'
    assert err == ''
    assert mock_module.run_command.call_count == 3
    mock_module.run_command.assert_any_call(['/usr/bin/locale', '-a'])
    mock_module.run_command.assert_any_call(['pip', 'list', '--format=freeze'], cwd=chdir, environ_update={'LANG': 'C', 'LC_ALL': 'C', 'LC_MESSAGES': 'C'})
    mock_module.run_command.assert_any_call(['pip', 'freeze'], cwd=chdir)

def test_get_packages_list_and_freeze_fail(mock_module):
    mock_module.run_command.side_effect = [
        (0, 'C\n', ''),  # locale -a command
        (1, '', 'error'),  # pip list fails
        (1, '', 'error')  # pip freeze fails
    ]
    pip = ['pip']
    chdir = '/some/path'
    
    with patch('ansible.modules.pip._fail') as mock_fail:
        _get_packages(mock_module, pip, chdir)
        mock_fail.assert_called_once_with(mock_module, ['pip', 'freeze'], '', 'error')
