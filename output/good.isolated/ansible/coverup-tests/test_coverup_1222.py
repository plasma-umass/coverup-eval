# file lib/ansible/modules/subversion.py:242-257
# lines [244, 245, 246, 247, 249, 251, 252, 253, 255, 257]
# branches ['246->247', '246->249', '252->253', '252->255']

import re
import pytest
from unittest.mock import MagicMock

# Assuming the Subversion class is part of a module named subversion
from ansible.modules.subversion import Subversion

@pytest.fixture
def svn_mock(mocker):
    mocker.patch('ansible.modules.subversion.Subversion._exec', return_value=["Revision: 123", "URL: http://example.com"])
    mock_module = MagicMock()
    return Subversion(mock_module, 'dest', 'repo', 'revision', 'username', 'password', 'svn_path', True)

@pytest.fixture
def svn_mock_no_rev_no_url(mocker):
    mocker.patch('ansible.modules.subversion.Subversion._exec', return_value=["No revision info", "No URL info"])
    mock_module = MagicMock()
    return Subversion(mock_module, 'dest', 'repo', 'revision', 'username', 'password', 'svn_path', True)

def test_get_revision_with_rev_and_url(svn_mock):
    rev, url = svn_mock.get_revision()
    assert rev == "Revision: 123"
    assert url == "URL: http://example.com"

def test_get_revision_without_rev_and_url(svn_mock_no_rev_no_url):
    rev, url = svn_mock_no_rev_no_url.get_revision()
    assert rev == "Unable to get revision"
    assert url == "Unable to get URL"
