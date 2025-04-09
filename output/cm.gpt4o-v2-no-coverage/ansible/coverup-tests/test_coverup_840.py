# file: lib/ansible/modules/subversion.py:161-163
# asked: {"lines": [161, 162, 163], "branches": []}
# gained: {"lines": [161, 162, 163], "branches": []}

import pytest
from unittest.mock import MagicMock
from ansible.module_utils.compat.version import LooseVersion
from ansible.modules.subversion import Subversion

@pytest.fixture
def mock_module():
    return MagicMock()

@pytest.fixture
def subversion(mock_module):
    return Subversion(
        module=mock_module,
        dest='dest',
        repo='repo',
        revision='revision',
        username='username',
        password='password',
        svn_path='svn',
        validate_certs=True
    )

def test_has_option_password_from_stdin_true(subversion, mock_module):
    mock_module.run_command.return_value = (0, '1.10.0', '')
    assert subversion.has_option_password_from_stdin() == True

def test_has_option_password_from_stdin_false(subversion, mock_module):
    mock_module.run_command.return_value = (0, '1.9.9', '')
    assert subversion.has_option_password_from_stdin() == False

def test_has_option_password_from_stdin_error(subversion, mock_module):
    mock_module.run_command.return_value = (1, '', 'error')
    with pytest.raises(Exception):
        subversion.has_option_password_from_stdin()
