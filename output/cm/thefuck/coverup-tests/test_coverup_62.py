# file thefuck/rules/cat_dir.py:5-10
# lines [5, 6, 7, 8, 9]
# branches []

import os
import pytest
from thefuck.types import Command
from thefuck.rules.cat_dir import match

@pytest.fixture
def cat_dir(tmp_path):
    dir_path = tmp_path / "testdir"
    dir_path.mkdir()
    return str(dir_path)

def test_match_with_directory(cat_dir, mocker):
    mocker.patch('os.path.isdir', return_value=True)
    command = Command('cat ' + cat_dir, 'cat: ' + cat_dir + ': Is a directory')
    assert match(command)

def test_not_match_with_non_directory(cat_dir, mocker):
    mocker.patch('os.path.isdir', return_value=False)
    command = Command('cat ' + cat_dir, 'cat: ' + cat_dir + ': Is a directory')
    assert not match(command)

def test_not_match_with_non_cat_command(cat_dir, mocker):
    mocker.patch('os.path.isdir', return_value=True)
    command = Command('ls ' + cat_dir, 'ls: ' + cat_dir + ': Is a directory')
    assert not match(command)
