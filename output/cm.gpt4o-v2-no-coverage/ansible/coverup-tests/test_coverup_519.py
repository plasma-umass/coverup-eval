# file: lib/ansible/modules/subversion.py:151-159
# asked: {"lines": [151, 152, 153, 154, 155, 156, 157, 158, 159], "branches": []}
# gained: {"lines": [151, 152, 153, 154, 155, 156, 157, 158, 159], "branches": []}

import pytest
from ansible.modules.subversion import Subversion

def test_subversion_init():
    module = object()
    dest = "/path/to/dest"
    repo = "http://example.com/repo"
    revision = "1234"
    username = "user"
    password = "pass"
    svn_path = "/usr/bin/svn"
    validate_certs = True

    svn = Subversion(module, dest, repo, revision, username, password, svn_path, validate_certs)

    assert svn.module == module
    assert svn.dest == dest
    assert svn.repo == repo
    assert svn.revision == revision
    assert svn.username == username
    assert svn.password == password
    assert svn.svn_path == svn_path
    assert svn.validate_certs == validate_certs
