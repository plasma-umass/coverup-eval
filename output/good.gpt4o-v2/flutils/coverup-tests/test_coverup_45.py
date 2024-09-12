# file: flutils/pathutils.py:336-384
# asked: {"lines": [336, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384], "branches": [[372, 373], [372, 374], [374, 375], [374, 376], [376, 377], [376, 378], [378, 379], [378, 380], [380, 381], [380, 382], [382, 383], [382, 384]]}
# gained: {"lines": [336, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384], "branches": [[372, 373], [372, 374], [374, 375], [374, 376], [376, 377], [376, 378], [378, 379], [378, 380], [380, 381], [380, 382], [382, 383], [382, 384]]}

import os
import pytest
from unittest import mock
from flutils.pathutils import exists_as, normalize_path

@pytest.fixture
def mock_normalize_path():
    with mock.patch('flutils.pathutils.normalize_path') as mock_normalize:
        yield mock_normalize

@pytest.fixture
def mock_path():
    mock_path = mock.Mock()
    mock_path.is_dir.return_value = False
    mock_path.is_file.return_value = False
    mock_path.is_block_device.return_value = False
    mock_path.is_char_device.return_value = False
    mock_path.is_fifo.return_value = False
    mock_path.is_socket.return_value = False
    return mock_path

def test_exists_as_directory(mock_normalize_path, mock_path):
    mock_path.is_dir.return_value = True
    mock_normalize_path.return_value = mock_path

    assert exists_as('some/directory') == 'directory'

def test_exists_as_file(mock_normalize_path, mock_path):
    mock_path.is_file.return_value = True
    mock_normalize_path.return_value = mock_path

    assert exists_as('some/file') == 'file'

def test_exists_as_block_device(mock_normalize_path, mock_path):
    mock_path.is_block_device.return_value = True
    mock_normalize_path.return_value = mock_path

    assert exists_as('some/block_device') == 'block device'

def test_exists_as_char_device(mock_normalize_path, mock_path):
    mock_path.is_char_device.return_value = True
    mock_normalize_path.return_value = mock_path

    assert exists_as('some/char_device') == 'char device'

def test_exists_as_fifo(mock_normalize_path, mock_path):
    mock_path.is_fifo.return_value = True
    mock_normalize_path.return_value = mock_path

    assert exists_as('some/fifo') == 'FIFO'

def test_exists_as_socket(mock_normalize_path, mock_path):
    mock_path.is_socket.return_value = True
    mock_normalize_path.return_value = mock_path

    assert exists_as('some/socket') == 'socket'

def test_exists_as_nonexistent(mock_normalize_path, mock_path):
    mock_normalize_path.return_value = mock_path

    assert exists_as('some/nonexistent') == ''
