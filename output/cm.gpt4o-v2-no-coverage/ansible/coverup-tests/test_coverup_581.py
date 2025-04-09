# file: lib/ansible/modules/subversion.py:206-213
# asked: {"lines": [206, 208, 209, 210, 211, 213], "branches": [[209, 210], [209, 211]]}
# gained: {"lines": [206, 208, 209, 210, 211, 213], "branches": [[209, 210], [209, 211]]}

import pytest
from unittest.mock import MagicMock

# Assuming the Subversion class is defined in the module ansible.modules.subversion
from ansible.modules.subversion import Subversion

class TestSubversion:
    @pytest.fixture
    def subversion(self):
        module = MagicMock()
        dest = "/path/to/dest"
        repo = "http://example.com/repo"
        revision = "1234"
        username = "user"
        password = "pass"
        svn_path = "/usr/bin/svn"
        validate_certs = True
        return Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)

    def test_export_without_force(self, subversion, mocker):
        mock_exec = mocker.patch.object(subversion, '_exec')
        subversion.export()
        mock_exec.assert_called_once_with(['export', '-r', '1234', 'http://example.com/repo', '/path/to/dest'])

    def test_export_with_force(self, subversion, mocker):
        mock_exec = mocker.patch.object(subversion, '_exec')
        subversion.export(force=True)
        mock_exec.assert_called_once_with(['export', '--force', '-r', '1234', 'http://example.com/repo', '/path/to/dest'])
