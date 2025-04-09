# file lib/ansible/parsing/dataloader.py:454-468
# lines [454, 455, 456, 457, 459, 460, 462, 463, 464, 466, 468]
# branches ['456->457', '456->468', '457->456', '457->459', '462->463', '462->464', '464->456', '464->466']

import os
import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_get_dir_vars_files(dataloader, mocker):
    # Mock the list_directory, is_directory, and is_file methods
    mock_list_directory = mocker.patch.object(dataloader, 'list_directory')
    mock_list_directory.side_effect = [
        ['file1.yml', 'file2.txt', '.hidden', 'backup~', 'subdir'],
        ['file1.yml', 'file2.txt']  # Contents of 'subdir'
    ]
    mocker.patch.object(dataloader, 'is_directory', side_effect=lambda x: x.endswith('subdir'))
    mocker.patch.object(dataloader, 'is_file', side_effect=lambda x: not x.endswith('subdir'))

    # Define the path and extensions
    path = '/some/path'
    extensions = ['.yml', '.yaml']

    # Call the method
    result = dataloader._get_dir_vars_files(path, extensions)

    # Assertions to verify the correct files are found
    assert '/some/path/file1.yml' in result
    assert '/some/path/file2.txt' not in result
    assert '/some/path/.hidden' not in result
    assert '/some/path/backup~' not in result
    assert '/some/path/subdir/file1.yml' in result
    assert '/some/path/subdir/file2.txt' not in result

    # Clean up any side effects
    mocker.stopall()
