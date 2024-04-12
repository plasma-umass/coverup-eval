# file flutils/pathutils.py:336-384
# lines [336, 370, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384]
# branches ['372->373', '372->374', '374->375', '374->376', '376->377', '376->378', '378->379', '378->380', '380->381', '380->382', '382->383', '382->384']

import os
import pytest
import socket
import tempfile
from pathlib import Path
from flutils.pathutils import exists_as

def test_exists_as(tmp_path):
    # Test for directory
    assert exists_as(tmp_path) == 'directory'

    # Test for file
    file_path = tmp_path / 'test_file.txt'
    file_path.touch()
    assert exists_as(file_path) == 'file'

    # Test for block device, if possible
    if os.name != 'nt':  # Block devices are not available on Windows
        block_device_path = next(Path('/dev').glob('loop*'), None)
        if block_device_path:
            assert exists_as(block_device_path) == 'block device'

    # Test for char device
    char_device_path = '/dev/null' if os.name != 'nt' else 'NUL'
    assert exists_as(char_device_path) == 'char device'

    # Test for FIFO, if possible
    if os.name != 'nt':  # FIFOs are not available on Windows
        fifo_path = tmp_path / 'test_fifo'
        os.mkfifo(fifo_path)
        assert exists_as(fifo_path) == 'FIFO'

    # Test for socket, if possible
    if hasattr(socket, 'AF_UNIX'):
        socket_path = tmp_path / 'test_socket'
        sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        sock.bind(str(socket_path))
        assert exists_as(socket_path) == 'socket'
        sock.close()

    # Test for non-existent path
    non_existent_path = tmp_path / 'non_existent'
    assert exists_as(non_existent_path) == ''

    # Test for broken symlink
    broken_symlink_path = tmp_path / 'broken_symlink'
    broken_symlink_path.symlink_to(non_existent_path)
    assert exists_as(broken_symlink_path) == ''

    # Cleanup is handled by pytest's tmp_path fixture
