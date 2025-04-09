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
    mocker.patch.object(Display, 'warning')
    tmp_file_1 = '/tmp/file1'
    tmp_file_2 = '/tmp/file2'
    dataloader._tempfiles = {tmp_file_1, tmp_file_2}

    # Mock cleanup_tmp_file to raise an exception for tmp_file_2
    def mock_cleanup_tmp_file(file_path):
        if file_path == tmp_file_2:
            raise Exception("Mocked exception")
        dataloader._tempfiles.remove(file_path)

    mocker.patch.object(dataloader, 'cleanup_tmp_file', side_effect=mock_cleanup_tmp_file)

    # Execute
    dataloader.cleanup_all_tmp_files()

    # Verify
    dataloader.cleanup_tmp_file.assert_any_call(tmp_file_1)
    dataloader.cleanup_tmp_file.assert_any_call(tmp_file_2)
    assert tmp_file_1 not in dataloader._tempfiles
    assert tmp_file_2 not in dataloader._tempfiles or Display.warning.called
    Display.warning.assert_called_once_with("Unable to cleanup temp files: Mocked exception")
