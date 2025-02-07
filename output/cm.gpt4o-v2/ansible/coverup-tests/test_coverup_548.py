# file: lib/ansible/parsing/dataloader.py:409-418
# asked: {"lines": [409, 414, 415, 416, 417, 418], "branches": [[414, 0], [414, 415]]}
# gained: {"lines": [409, 414, 415, 416, 417, 418], "branches": [[414, 0], [414, 415]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.parsing.dataloader import DataLoader
from ansible.utils.display import Display

@pytest.fixture
def dataloader():
    return DataLoader()

def test_cleanup_all_tmp_files(dataloader, mocker):
    # Setup
    mocker.patch.object(dataloader, 'cleanup_tmp_file')
    mock_display_warning = mocker.patch.object(Display, 'warning')
    dataloader._tempfiles = {'/tmp/testfile1', '/tmp/testfile2'}

    # Mock cleanup_tmp_file to raise an exception for one file
    def side_effect(file_path):
        if file_path == '/tmp/testfile2':
            raise Exception("Test exception")
        else:
            dataloader._tempfiles.remove(file_path)
    dataloader.cleanup_tmp_file.side_effect = side_effect

    # Execute
    dataloader.cleanup_all_tmp_files()

    # Verify
    dataloader.cleanup_tmp_file.assert_any_call('/tmp/testfile1')
    dataloader.cleanup_tmp_file.assert_any_call('/tmp/testfile2')
    assert mock_display_warning.called
    assert mock_display_warning.call_args[0][0] == "Unable to cleanup temp files: Test exception"
    assert dataloader._tempfiles == {'/tmp/testfile2'}
