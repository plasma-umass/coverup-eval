# file: lib/ansible/modules/pip.py:305-307
# asked: {"lines": [307], "branches": []}
# gained: {"lines": [307], "branches": []}

import pytest
import re
from ansible.modules.pip import _is_vcs_url, _VCS_RE

def test_is_vcs_url_git():
    assert _is_vcs_url("git+https://example.com/repo.git")
    
def test_is_vcs_url_svn():
    assert _is_vcs_url("svn+https://example.com/repo")
    
def test_is_vcs_url_hg():
    assert _is_vcs_url("hg+https://example.com/repo")
    
def test_is_vcs_url_bzr():
    assert _is_vcs_url("bzr+https://example.com/repo")
    
def test_is_not_vcs_url():
    assert not _is_vcs_url("https://example.com/repo")
    
def test_is_not_vcs_url_invalid():
    assert not _is_vcs_url("invalid+https://example.com/repo")
