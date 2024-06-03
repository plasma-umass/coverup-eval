# file thefuck/rules/dirty_unzip.py:45-57
# lines [45, 46, 47, 48, 50, 52, 53, 54, 57]
# branches ['47->exit', '47->48', '48->50', '48->52']

import os
import zipfile
import pytest
from unittest import mock
from thefuck.rules.dirty_unzip import side_effect

@pytest.fixture
def create_test_zip(tmp_path):
    zip_path = tmp_path / "test.zip"
    with zipfile.ZipFile(zip_path, 'w') as archive:
        archive.writestr("testfile.txt", "This is a test file.")
        archive.writestr("../outsidefile.txt", "This file is outside the current directory.")
    return zip_path

def test_side_effect(create_test_zip, mocker):
    old_cmd = mock.Mock()
    old_cmd.script = str(create_test_zip)
    command = mock.Mock()

    # Mock _zip_file to return the path to our test zip
    mocker.patch('thefuck.rules.dirty_unzip._zip_file', return_value=str(create_test_zip))

    # Mock os.remove to track calls
    mock_remove = mocker.patch('os.remove')

    side_effect(old_cmd, command)

    # Assert that os.remove was called for the file inside the zip
    mock_remove.assert_called_once_with('testfile.txt')

    # Assert that os.remove was not called for the file outside the current directory
    assert not any(call.args[0] == '../outsidefile.txt' for call in mock_remove.call_args_list)
