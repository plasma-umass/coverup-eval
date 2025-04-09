# file: flutils/pathutils.py:336-384
# asked: {"lines": [336, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384], "branches": [[372, 373], [372, 374], [374, 375], [374, 376], [376, 377], [376, 378], [378, 379], [378, 380], [380, 381], [380, 382], [382, 383], [382, 384]]}
# gained: {"lines": [336, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384], "branches": [[372, 373], [372, 374], [374, 375], [374, 376], [376, 377], [376, 378], [378, 379], [378, 380], [380, 381], [380, 382], [382, 383], [382, 384]]}

import pytest
import os
import stat
import tempfile
from pathlib import Path
from flutils.pathutils import exists_as

@pytest.fixture
def temp_path():
    with tempfile.TemporaryDirectory() as tmpdir:
        yield Path(tmpdir)

def test_exists_as_directory(temp_path):
    assert exists_as(temp_path) == 'directory'

def test_exists_as_file(temp_path):
    file_path = temp_path / 'test_file'
    file_path.touch()
    assert exists_as(file_path) == 'file'

def test_exists_as_block_device(monkeypatch):
    def mock_is_block_device(path):
        return True

    monkeypatch.setattr(Path, 'is_block_device', mock_is_block_device)
    assert exists_as('/dev/sda') == 'block device'

def test_exists_as_char_device(monkeypatch):
    def mock_is_char_device(path):
        return True

    monkeypatch.setattr(Path, 'is_char_device', mock_is_char_device)
    assert exists_as('/dev/tty') == 'char device'

def test_exists_as_fifo(temp_path):
    fifo_path = temp_path / 'test_fifo'
    os.mkfifo(fifo_path)
    assert exists_as(fifo_path) == 'FIFO'

def test_exists_as_socket(temp_path):
    socket_path = temp_path / 'test_socket'
    os.mknod(socket_path, stat.S_IFSOCK)
    assert exists_as(socket_path) == 'socket'

def test_exists_as_nonexistent(temp_path):
    nonexistent_path = temp_path / 'nonexistent'
    assert exists_as(nonexistent_path) == ''

def test_exists_as_broken_symlink(temp_path):
    target_path = temp_path / 'target'
    symlink_path = temp_path / 'symlink'
    symlink_path.symlink_to(target_path)
    assert exists_as(symlink_path) == ''
