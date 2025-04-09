# file: flutils/pathutils.py:336-384
# asked: {"lines": [336, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384], "branches": [[372, 373], [372, 374], [374, 375], [374, 376], [376, 377], [376, 378], [378, 379], [378, 380], [380, 381], [380, 382], [382, 383], [382, 384]]}
# gained: {"lines": [336, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384], "branches": [[372, 373], [372, 374], [374, 375], [374, 376], [376, 377], [376, 378], [378, 379], [378, 380], [380, 381], [380, 382], [382, 383], [382, 384]]}

import os
import socket
import pytest
from unittest.mock import patch, MagicMock
from flutils.pathutils import exists_as, normalize_path

@pytest.fixture
def mock_normalize_path():
    with patch('flutils.pathutils.normalize_path') as mock:
        yield mock

@pytest.fixture
def temp_file(tmp_path):
    file = tmp_path / "temp_file"
    file.touch()
    yield file

@pytest.fixture
def temp_dir(tmp_path):
    dir = tmp_path / "temp_dir"
    dir.mkdir()
    yield dir

@pytest.fixture
def temp_fifo(tmp_path):
    fifo = tmp_path / "temp_fifo"
    os.mkfifo(fifo)
    yield fifo

@pytest.fixture
def temp_socket(tmp_path):
    sock_path = tmp_path / "temp_socket"
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(str(sock_path))
    yield sock_path
    sock.close()

def test_exists_as_directory(mock_normalize_path, temp_dir):
    mock_normalize_path.return_value = temp_dir
    assert exists_as(temp_dir) == 'directory'

def test_exists_as_file(mock_normalize_path, temp_file):
    mock_normalize_path.return_value = temp_file
    assert exists_as(temp_file) == 'file'

def test_exists_as_block_device(mock_normalize_path):
    mock_path = MagicMock()
    mock_path.is_dir.return_value = False
    mock_path.is_file.return_value = False
    mock_path.is_block_device.return_value = True
    mock_normalize_path.return_value = mock_path
    assert exists_as(mock_path) == 'block device'

def test_exists_as_char_device(mock_normalize_path):
    mock_path = MagicMock()
    mock_path.is_dir.return_value = False
    mock_path.is_file.return_value = False
    mock_path.is_block_device.return_value = False
    mock_path.is_char_device.return_value = True
    mock_normalize_path.return_value = mock_path
    assert exists_as(mock_path) == 'char device'

def test_exists_as_fifo(mock_normalize_path, temp_fifo):
    mock_normalize_path.return_value = temp_fifo
    assert exists_as(temp_fifo) == 'FIFO'

def test_exists_as_socket(mock_normalize_path, temp_socket):
    mock_normalize_path.return_value = temp_socket
    assert exists_as(temp_socket) == 'socket'

def test_exists_as_nonexistent(mock_normalize_path):
    mock_path = MagicMock()
    mock_path.is_dir.return_value = False
    mock_path.is_file.return_value = False
    mock_path.is_block_device.return_value = False
    mock_path.is_char_device.return_value = False
    mock_path.is_fifo.return_value = False
    mock_path.is_socket.return_value = False
    mock_normalize_path.return_value = mock_path
    assert exists_as(mock_path) == ''
