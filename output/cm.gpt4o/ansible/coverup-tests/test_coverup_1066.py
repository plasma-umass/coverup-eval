# file lib/ansible/modules/subversion.py:165-191
# lines [167, 168, 169, 170, 172, 173, 174, 175, 176, 177, 178, 179, 180, 182, 184, 185, 186, 188, 189, 191]
# branches ['172->173', '172->174', '175->176', '175->177', '177->178', '177->185', '178->179', '178->182', '188->189', '188->191']

import pytest
from unittest.mock import Mock, patch

# Assuming the Subversion class is imported from ansible.modules.subversion
from ansible.modules.subversion import Subversion

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def subversion(mock_module):
    svn = Subversion(
        module=mock_module,
        dest='dest',
        repo='repo',
        revision='revision',
        username='testuser',
        password='testpass',
        svn_path='svn',
        validate_certs=False
    )
    return svn

def test_exec_with_password_from_stdin(subversion, mock_module):
    subversion.has_option_password_from_stdin = Mock(return_value=True)
    mock_module.run_command = Mock(return_value=(0, 'output', ''))

    result = subversion._exec(['info'])

    mock_module.run_command.assert_called_once_with(
        ['svn', '--non-interactive', '--no-auth-cache', '--trust-server-cert', '--username', 'testuser', '--password-from-stdin', 'info'],
        True,
        data='testpass'
    )
    assert result == ['output']

def test_exec_with_password_on_command_line(subversion, mock_module):
    subversion.has_option_password_from_stdin = Mock(return_value=False)
    mock_module.run_command = Mock(return_value=(0, 'output', ''))

    result = subversion._exec(['info'])

    mock_module.run_command.assert_called_once_with(
        ['svn', '--non-interactive', '--no-auth-cache', '--trust-server-cert', '--username', 'testuser', '--password', 'testpass', 'info'],
        True,
        data=None
    )
    assert result == ['output']

def test_exec_without_check_rc(subversion, mock_module):
    subversion.has_option_password_from_stdin = Mock(return_value=False)
    mock_module.run_command = Mock(return_value=(1, 'output', ''))

    result = subversion._exec(['info'], check_rc=False)

    mock_module.run_command.assert_called_once_with(
        ['svn', '--non-interactive', '--no-auth-cache', '--trust-server-cert', '--username', 'testuser', '--password', 'testpass', 'info'],
        False,
        data=None
    )
    assert result == 1
