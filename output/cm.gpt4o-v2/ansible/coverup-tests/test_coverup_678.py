# file: lib/ansible/cli/arguments/option_helpers.py:155-158
# asked: {"lines": [155, 156, 157, 158], "branches": []}
# gained: {"lines": [155, 156, 157, 158], "branches": []}

import os
import pytest
from unittest import mock

from ansible.cli.arguments.option_helpers import _gitinfo, _git_repo_info

@pytest.fixture
def mock_git_repo_info(monkeypatch):
    def mock_info(repo_path):
        return "mocked git info"
    monkeypatch.setattr('ansible.cli.arguments.option_helpers._git_repo_info', mock_info)

def test_gitinfo(monkeypatch, mock_git_repo_info):
    # Mock os.path functions to simulate the environment
    monkeypatch.setattr(os.path, 'dirname', lambda _: '/mocked/path')
    monkeypatch.setattr(os.path, 'normpath', lambda path: path)
    monkeypatch.setattr(os.path, 'join', lambda *args: '/'.join(args))

    result = _gitinfo()
    assert result == "mocked git info"
