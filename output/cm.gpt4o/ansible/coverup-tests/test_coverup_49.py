# file lib/ansible/cli/arguments/option_helpers.py:112-152
# lines [112, 114, 115, 117, 118, 119, 120, 122, 123, 125, 126, 127, 128, 129, 130, 131, 133, 134, 135, 136, 137, 140, 141, 142, 144, 145, 146, 148, 149, 151, 152]
# branches ['115->117', '115->151', '117->118', '117->128', '122->123', '122->125', '130->131', '130->133', '134->135', '134->140', '145->146', '145->148']

import os
import time
import pytest
import tempfile
from unittest import mock
from ansible.cli.arguments.option_helpers import _git_repo_info

@pytest.fixture
def mock_time():
    with mock.patch('time.localtime') as mock_localtime, \
         mock.patch('time.strftime') as mock_strftime, \
         mock.patch('time.daylight', 0), \
         mock.patch('time.timezone', 0), \
         mock.patch('time.altzone', 0):
        mock_localtime.return_value = time.struct_time((2023, 1, 1, 0, 0, 0, 6, 1, 0))
        mock_strftime.return_value = "2023/01/01 00:00:00"
        yield

@pytest.fixture
def git_repo():
    with tempfile.TemporaryDirectory() as repo_dir:
        os.makedirs(os.path.join(repo_dir, '.git', 'refs', 'heads'))
        head_path = os.path.join(repo_dir, '.git', 'HEAD')
        branch_path = os.path.join(repo_dir, '.git', 'refs', 'heads', 'main')
        with open(head_path, 'w') as f:
            f.write('ref: refs/heads/main\n')
        with open(branch_path, 'w') as f:
            f.write('1234567890abcdef1234567890abcdef12345678\n')
        yield repo_dir

@pytest.fixture
def git_submodule():
    with tempfile.TemporaryDirectory() as repo_dir:
        os.makedirs(os.path.join(repo_dir, 'submodule'))
        submodule_git_path = os.path.join(repo_dir, 'submodule', '.git')
        with open(submodule_git_path, 'w') as f:
            f.write('gitdir: ../.git/modules/submodule\n')
        os.makedirs(os.path.join(repo_dir, '.git', 'modules', 'submodule', 'refs', 'heads'))
        head_path = os.path.join(repo_dir, '.git', 'modules', 'submodule', 'HEAD')
        branch_path = os.path.join(repo_dir, '.git', 'modules', 'submodule', 'refs', 'heads', 'main')
        with open(head_path, 'w') as f:
            f.write('ref: refs/heads/main\n')
        with open(branch_path, 'w') as f:
            f.write('1234567890abcdef1234567890abcdef12345678\n')
        yield os.path.join(repo_dir, 'submodule')

def test_git_repo_info(mock_time, git_repo):
    result = _git_repo_info(os.path.join(git_repo, '.git'))
    assert result == "(main 1234567890) last updated 2023/01/01 00:00:00 (GMT +000)"

def test_git_submodule_info(mock_time, git_submodule):
    result = _git_repo_info(os.path.join(git_submodule, '.git'))
    assert result == "(main 1234567890) last updated 2023/01/01 00:00:00 (GMT +000)"
