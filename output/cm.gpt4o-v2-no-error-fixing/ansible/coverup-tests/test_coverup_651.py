# file: lib/ansible/modules/pip.py:305-307
# asked: {"lines": [305, 307], "branches": []}
# gained: {"lines": [305, 307], "branches": []}

import pytest
import re

# Assuming _is_vcs_url and _VCS_RE are defined in the module ansible.modules.pip
from ansible.modules.pip import _is_vcs_url, _VCS_RE

def test_is_vcs_url_git():
    url = "git+https://example.com/repo.git"
    assert _is_vcs_url(url) is not None

def test_is_vcs_url_svn():
    url = "svn+https://example.com/repo"
    assert _is_vcs_url(url) is not None

def test_is_vcs_url_hg():
    url = "hg+https://example.com/repo"
    assert _is_vcs_url(url) is not None

def test_is_vcs_url_bzr():
    url = "bzr+https://example.com/repo"
    assert _is_vcs_url(url) is not None

def test_is_not_vcs_url():
    url = "https://example.com/repo"
    assert _is_vcs_url(url) is None
