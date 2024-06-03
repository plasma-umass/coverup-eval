# file lib/ansible/parsing/dataloader.py:409-418
# lines [409, 414, 415, 416, 417, 418]
# branches ['414->exit', '414->415']

import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader
from ansible.utils.display import Display

@pytest.fixture
def dataloader_with_tempfiles():
    dl = DataLoader()
    dl._tempfiles = ['/tmp/testfile1', '/tmp/testfile2']
    return dl

def test_cleanup_all_tmp_files(dataloader_with_tempfiles, mocker):
    mock_cleanup_tmp_file = mocker.patch.object(dataloader_with_tempfiles, 'cleanup_tmp_file')
    mock_display_warning = mocker.patch.object(Display, 'warning')

    # Simulate an exception for one of the temp files
    mock_cleanup_tmp_file.side_effect = [None, Exception("Test Exception")]

    dataloader_with_tempfiles.cleanup_all_tmp_files()

    # Check that cleanup_tmp_file was called for each tempfile
    assert mock_cleanup_tmp_file.call_count == 2
    mock_cleanup_tmp_file.assert_any_call('/tmp/testfile1')
    mock_cleanup_tmp_file.assert_any_call('/tmp/testfile2')

    # Check that the warning was displayed for the exception
    mock_display_warning.assert_called_once_with("Unable to cleanup temp files: Test Exception")
