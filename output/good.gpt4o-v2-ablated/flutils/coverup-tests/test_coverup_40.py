# file: flutils/pathutils.py:336-384
# asked: {"lines": [370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384], "branches": [[372, 373], [372, 374], [374, 375], [374, 376], [376, 377], [376, 378], [378, 379], [378, 380], [380, 381], [380, 382], [382, 383], [382, 384]]}
# gained: {"lines": [370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384], "branches": [[372, 373], [372, 374], [374, 375], [374, 376], [376, 377], [376, 378], [378, 379], [378, 380], [380, 381], [380, 382], [382, 383], [382, 384]]}

import pytest
import os
import tempfile
import pathlib
from unittest.mock import patch
from flutils.pathutils import exists_as

@pytest.fixture
def temp_dir():
    dirpath = tempfile.mkdtemp()
    yield dirpath
    os.rmdir(dirpath)

@pytest.fixture
def temp_file():
    fd, filepath = tempfile.mkstemp()
    os.close(fd)
    yield filepath
    os.remove(filepath)

@pytest.fixture
def temp_fifo():
    fifo_path = tempfile.mktemp()
    os.mkfifo(fifo_path)
    yield fifo_path
    os.remove(fifo_path)

@pytest.fixture
def temp_socket():
    import socket
    sock_path = tempfile.mktemp()
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.bind(sock_path)
    yield sock_path
    sock.close()
    os.remove(sock_path)

def test_exists_as_directory(temp_dir):
    assert exists_as(temp_dir) == 'directory'

def test_exists_as_file(temp_file):
    assert exists_as(temp_file) == 'file'

def test_exists_as_block_device(monkeypatch):
    path = pathlib.Path('/dev/sda')
    monkeypatch.setattr(pathlib.Path, 'is_block_device', lambda self: True)
    assert exists_as(path) == 'block device'

def test_exists_as_char_device(monkeypatch):
    path = pathlib.Path('/dev/tty')
    monkeypatch.setattr(pathlib.Path, 'is_char_device', lambda self: True)
    assert exists_as(path) == 'char device'

def test_exists_as_fifo(temp_fifo):
    assert exists_as(temp_fifo) == 'FIFO'

def test_exists_as_socket(temp_socket):
    assert exists_as(temp_socket) == 'socket'

def test_exists_as_nonexistent():
    assert exists_as('/nonexistent/path') == ''

def test_exists_as_permission_error(monkeypatch):
    path = pathlib.Path('/root/secret')
    monkeypatch.setattr(pathlib.Path, 'exists', lambda self: True)
    monkeypatch.setattr(pathlib.Path, 'is_dir', lambda self: False)
    monkeypatch.setattr(pathlib.Path, 'is_file', lambda self: False)
    monkeypatch.setattr(pathlib.Path, 'is_block_device', lambda self: False)
    monkeypatch.setattr(pathlib.Path, 'is_char_device', lambda self: False)
    monkeypatch.setattr(pathlib.Path, 'is_fifo', lambda self: False)
    monkeypatch.setattr(pathlib.Path, 'is_socket', lambda self: False)
    assert exists_as(path) == ''
