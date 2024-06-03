# file lib/ansible/parsing/dataloader.py:116-118
# lines [116, 117, 118]
# branches []

import os
import pytest
from unittest.mock import patch
from ansible.parsing.dataloader import DataLoader

@pytest.fixture
def dataloader():
    return DataLoader()

def test_is_directory_with_mocked_path_dwim(dataloader, mocker):
    mock_path_dwim = mocker.patch.object(dataloader, 'path_dwim', return_value='/mocked/path')
    mock_isdir = mocker.patch('os.path.isdir', return_value=True)
    mock_to_bytes = mocker.patch('ansible.parsing.dataloader.to_bytes', return_value=b'/mocked/path')

    result = dataloader.is_directory('/some/path')

    mock_path_dwim.assert_called_once_with('/some/path')
    mock_to_bytes.assert_called_once_with('/mocked/path', errors='surrogate_or_strict')
    mock_isdir.assert_called_once_with(b'/mocked/path')
    assert result is True
