# file: lib/ansible/modules/subversion.py:161-163
# asked: {"lines": [161, 162, 163], "branches": []}
# gained: {"lines": [161, 162, 163], "branches": []}

import pytest
from unittest.mock import Mock, patch
from ansible.module_utils.compat.version import LooseVersion
from ansible.modules.subversion import Subversion

@pytest.fixture
def mock_module():
    return Mock()

@pytest.fixture
def subversion(mock_module):
    return Subversion(
        module=mock_module,
        dest="dummy_dest",
        repo="dummy_repo",
        revision="dummy_revision",
        username="dummy_user",
        password="dummy_pass",
        svn_path="dummy_svn_path",
        validate_certs=True
    )

def test_has_option_password_from_stdin(subversion, mock_module):
    mock_module.run_command.return_value = (0, '1.10.0', '')

    result = subversion.has_option_password_from_stdin()

    assert result is True
    mock_module.run_command.assert_called_once_with(['dummy_svn_path', '--version', '--quiet'], check_rc=True)

def test_has_option_password_from_stdin_false(subversion, mock_module):
    mock_module.run_command.return_value = (0, '1.9.9', '')

    result = subversion.has_option_password_from_stdin()

    assert result is False
    mock_module.run_command.assert_called_once_with(['dummy_svn_path', '--version', '--quiet'], check_rc=True)
