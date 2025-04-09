# file: lib/ansible/parsing/dataloader.py:181-195
# asked: {"lines": [181, 186, 187, 189, 190, 192, 193, 195], "branches": [[189, 190], [189, 192]]}
# gained: {"lines": [181, 186, 187, 189, 190, 192, 193, 195], "branches": [[189, 190], [189, 192]]}

import os
import pytest
from unittest.mock import patch
from urllib.parse import unquote
from ansible.parsing.dataloader import DataLoader
from ansible.module_utils._text import to_text
from ansible.utils.path import unfrackpath

@pytest.fixture
def dataloader():
    return DataLoader()

def test_path_dwim_absolute_path(dataloader, mocker):
    given = "/absolute/path"
    mocker.patch('ansible.parsing.dataloader.unquote', return_value=given)
    mocker.patch('ansible.parsing.dataloader.to_text', side_effect=lambda x, errors='strict': x)
    mocker.patch('ansible.utils.path.unfrackpath', return_value=given)

    result = dataloader.path_dwim(given)
    assert result == given

def test_path_dwim_home_path(dataloader, mocker):
    given = "~/home/path"
    expanded_path = os.path.expanduser(given)
    mocker.patch('ansible.parsing.dataloader.unquote', return_value=given)
    mocker.patch('ansible.parsing.dataloader.to_text', side_effect=lambda x, errors='strict': x)
    mocker.patch('ansible.utils.path.unfrackpath', return_value=expanded_path)

    result = dataloader.path_dwim(given)
    assert result == expanded_path

def test_path_dwim_relative_path(dataloader, mocker):
    given = "relative/path"
    basedir = "/base/dir"
    expected_path = os.path.join(basedir, given)
    mocker.patch.object(dataloader, '_basedir', basedir)
    mocker.patch('ansible.parsing.dataloader.unquote', return_value=given)
    mocker.patch('ansible.parsing.dataloader.to_text', side_effect=lambda x, errors='strict': x)
    mocker.patch('ansible.utils.path.unfrackpath', return_value=expected_path)

    result = dataloader.path_dwim(given)
    assert result == expected_path
