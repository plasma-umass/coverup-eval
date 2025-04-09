# file lib/ansible/parsing/dataloader.py:345-357
# lines [347, 348, 349, 350, 351, 352, 353, 354, 356, 357]
# branches []

import os
import tempfile
import pytest
from unittest import mock
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def mock_tempfile(mocker):
    mock_fd = mocker.patch('tempfile.mkstemp', return_value=(1, '/mocked/path/to/tempfile'))
    mock_open = mocker.patch('os.fdopen', mock.mock_open())
    mock_remove = mocker.patch('os.remove')
    return mock_fd, mock_open, mock_remove

def test_create_content_tempfile_success(mock_tempfile):
    data_loader = DataLoader()
    content = b"test content"
    temp_file_path = data_loader._create_content_tempfile(content)
    
    mock_tempfile[1].return_value.write.assert_called_once_with(content)
    assert temp_file_path == '/mocked/path/to/tempfile'

def test_create_content_tempfile_exception(mock_tempfile):
    data_loader = DataLoader()
    content = b"test content"
    
    mock_tempfile[1].return_value.write.side_effect = Exception("write error")
    
    with pytest.raises(Exception, match="write error"):
        data_loader._create_content_tempfile(content)
    
    mock_tempfile[2].assert_called_once_with('/mocked/path/to/tempfile')
    mock_tempfile[1].return_value.close.assert_called_once()
