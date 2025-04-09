# file: lib/ansible/modules/subversion.py:198-204
# asked: {"lines": [200, 201, 202, 203, 204], "branches": [[201, 202], [201, 203]]}
# gained: {"lines": [200, 201, 202, 203, 204], "branches": [[201, 202], [201, 203]]}

import pytest
from unittest.mock import MagicMock
from ansible.modules.subversion import Subversion

class TestSubversion:
    @pytest.fixture
    def svn(self):
        module = MagicMock()
        dest = "/path/to/dest"
        repo = "http://example.com/repo"
        revision = "1234"
        username = "user"
        password = "pass"
        svn_path = "/usr/bin/svn"
        validate_certs = True
        return Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)

    def test_checkout_without_force(self, svn, mocker):
        mock_exec = mocker.patch.object(svn, '_exec')
        svn.checkout()
        mock_exec.assert_called_once_with(['checkout', '-r', svn.revision, svn.repo, svn.dest])

    def test_checkout_with_force(self, svn, mocker):
        mock_exec = mocker.patch.object(svn, '_exec')
        svn.checkout(force=True)
        mock_exec.assert_called_once_with(['checkout', '--force', '-r', svn.revision, svn.repo, svn.dest])
