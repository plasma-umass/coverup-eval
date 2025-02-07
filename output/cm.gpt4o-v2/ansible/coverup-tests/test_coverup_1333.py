# file: lib/ansible/cli/arguments/option_helpers.py:112-152
# asked: {"lines": [114, 115, 117, 118, 119, 120, 122, 123, 125, 126, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 140, 141, 142, 144, 145, 146, 148, 149, 151, 152], "branches": [[115, 117], [115, 151], [117, 118], [117, 128], [122, 123], [122, 125], [130, 131], [130, 133], [134, 135], [134, 140], [145, 146], [145, 148]]}
# gained: {"lines": [114, 115, 117, 118, 119, 120, 122, 125, 126, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 140, 141, 142, 144, 145, 146, 149, 151, 152], "branches": [[115, 117], [115, 151], [117, 118], [117, 128], [122, 125], [130, 131], [130, 133], [134, 135], [134, 140], [145, 146]]}

import os
import pytest
import time
from unittest import mock
from ansible.module_utils.common.yaml import yaml_load
from ansible.cli.arguments.option_helpers import _git_repo_info

@pytest.fixture
def mock_repo(tmp_path):
    repo_path = tmp_path / ".git"
    repo_path.mkdir()
    head_path = repo_path / "HEAD"
    head_path.write_text("ref: refs/heads/main")
    branch_path = repo_path / "refs" / "heads" / "main"
    branch_path.parent.mkdir(parents=True)
    branch_path.write_text("1234567890abcdef")
    return repo_path

def test_git_repo_info_with_valid_repo(mock_repo):
    result = _git_repo_info(str(mock_repo))
    assert result.startswith("(main 1234567890) last updated")

def test_git_repo_info_with_detached_head(mock_repo):
    head_path = mock_repo / "HEAD"
    head_path.write_text("1234567890abcdef")
    result = _git_repo_info(str(mock_repo))
    assert result.startswith("(detached HEAD 1234567890) last updated")

def test_git_repo_info_with_gitfile(tmp_path, monkeypatch):
    repo_path = tmp_path / "submodule"
    repo_path.mkdir()
    gitfile_path = repo_path / ".git"
    gitfile_path.write_text("gitdir: ../.git/modules/submodule")
    submodule_path = tmp_path / ".git" / "modules" / "submodule"
    submodule_path.mkdir(parents=True)
    head_path = submodule_path / "HEAD"
    head_path.write_text("ref: refs/heads/main")
    branch_path = submodule_path / "refs" / "heads" / "main"
    branch_path.parent.mkdir(parents=True)
    branch_path.write_text("1234567890abcdef")

    with mock.patch("ansible.cli.arguments.option_helpers.yaml_load", return_value={"gitdir": "../.git/modules/submodule"}):
        result = _git_repo_info(str(gitfile_path))
        assert result.startswith("(main 1234567890) last updated")

def test_git_repo_info_with_invalid_gitfile(tmp_path, monkeypatch):
    repo_path = tmp_path / "submodule"
    repo_path.mkdir()
    gitfile_path = repo_path / ".git"
    gitfile_path.write_text("invalid content")

    with mock.patch("ansible.cli.arguments.option_helpers.yaml_load", return_value=None):
        result = _git_repo_info(str(gitfile_path))
        assert result == ''

def test_git_repo_info_with_nonexistent_path():
    result = _git_repo_info("/nonexistent/path")
    assert result == ''
