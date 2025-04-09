# file: lib/ansible/parsing/dataloader.py:181-195
# asked: {"lines": [181, 186, 187, 189, 190, 192, 193, 195], "branches": [[189, 190], [189, 192]]}
# gained: {"lines": [181, 186, 187, 189, 190, 192, 193, 195], "branches": [[189, 190], [189, 192]]}

import pytest
from unittest.mock import patch
from ansible.parsing.dataloader import DataLoader
import os

@pytest.fixture
def dataloader():
    return DataLoader()

def test_path_dwim_absolute_path(dataloader):
    given = "/absolute/path"
    expected = "/absolute/path"
    result = dataloader.path_dwim(given)
    assert result == expected

def test_path_dwim_home_path(dataloader):
    given = "~/home/path"
    expected = os.path.expanduser("~/home/path")
    result = dataloader.path_dwim(given)
    assert result == expected

def test_path_dwim_relative_path(dataloader):
    given = "relative/path"
    dataloader._basedir = "/base/dir"
    expected = "/base/dir/relative/path"
    result = dataloader.path_dwim(given)
    assert result == expected

def test_path_dwim_unquote(dataloader):
    given = "%7E/home/path"
    expected = os.path.expanduser("~/home/path")
    with patch('ansible.parsing.dataloader.unquote', return_value="~/home/path"):
        result = dataloader.path_dwim(given)
    assert result == expected

def test_path_dwim_to_text(dataloader):
    given = b"/absolute/path"
    expected = "/absolute/path"
    result = dataloader.path_dwim(given)
    assert result == expected
