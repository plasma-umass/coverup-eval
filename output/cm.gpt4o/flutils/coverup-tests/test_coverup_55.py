# file flutils/pathutils.py:336-384
# lines [336, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384]
# branches ['372->373', '372->374', '374->375', '374->376', '376->377', '376->378', '378->379', '378->380', '380->381', '380->382', '382->383', '382->384']

import os
import pytest
import tempfile
import socket
from unittest import mock
from flutils.pathutils import exists_as

@pytest.fixture
def temp_file():
    fd, path = tempfile.mkstemp()
    os.close(fd)
    yield path
    os.remove(path)

@pytest.fixture
def temp_dir():
    path = tempfile.mkdtemp()
    yield path
    os.rmdir(path)

@pytest.fixture
def temp_fifo():
    path = tempfile.mktemp()
    os.mkfifo(path)
    yield path
    os.remove(path)

@pytest.fixture
def temp_socket():
    path = tempfile.mktemp()
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(path)
    yield path
    sock.close()
    os.remove(path)

def test_exists_as_directory(temp_dir):
    assert exists_as(temp_dir) == 'directory'

def test_exists_as_file(temp_file):
    assert exists_as(temp_file) == 'file'

def test_exists_as_fifo(temp_fifo):
    assert exists_as(temp_fifo) == 'FIFO'

def test_exists_as_socket(temp_socket):
    assert exists_as(temp_socket) == 'socket'

def test_exists_as_block_device(mocker):
    mock_path = mocker.Mock()
    mock_path.is_dir.return_value = False
    mock_path.is_file.return_value = False
    mock_path.is_block_device.return_value = True
    mock_path.is_char_device.return_value = False
    mock_path.is_fifo.return_value = False
    mock_path.is_socket.return_value = False
    mocker.patch('flutils.pathutils.normalize_path', return_value=mock_path)
    assert exists_as('/dev/sda') == 'block device'

def test_exists_as_char_device(mocker):
    mock_path = mocker.Mock()
    mock_path.is_dir.return_value = False
    mock_path.is_file.return_value = False
    mock_path.is_block_device.return_value = False
    mock_path.is_char_device.return_value = True
    mock_path.is_fifo.return_value = False
    mock_path.is_socket.return_value = False
    mocker.patch('flutils.pathutils.normalize_path', return_value=mock_path)
    assert exists_as('/dev/tty') == 'char device'

def test_exists_as_nonexistent():
    assert exists_as('/nonexistent/path') == ''
