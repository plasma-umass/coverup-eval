# file lib/ansible/modules/lineinfile.py:262-281
# lines [264, 265, 266, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281]
# branches ['270->271', '270->278', '271->272', '271->273', '275->276', '275->278', '278->exit', '278->279']

import os
import tempfile
import pytest
from unittest import mock
from ansible.module_utils.basic import AnsibleModule
from ansible.modules.lineinfile import write_changes

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock(spec=AnsibleModule)
    module.tmpdir = tempfile.gettempdir()
    module.params = {
        'validate': 'cat %s',
        'unsafe_writes': False
    }
    return module

def test_write_changes_with_validation(mock_module, mocker):
    b_lines = [b"line1\n", b"line2\n"]
    dest = os.path.join(tempfile.gettempdir(), 'testfile.txt')

    # Create the destination file to ensure it exists for the test
    with open(dest, 'wb') as f:
        f.writelines(b_lines)

    # Mock the run_command method to simulate a successful validation
    mock_module.run_command = mocker.Mock(return_value=(0, '', ''))

    # Mock the atomic_move method
    mock_module.atomic_move = mocker.Mock()

    write_changes(mock_module, b_lines, dest)

    # Check that the temporary file was created and written to
    tmpfile = mock_module.run_command.call_args[0][0].split()[1].decode('utf-8')
    assert os.path.exists(tmpfile)
    with open(tmpfile, 'rb') as f:
        assert f.readlines() == b_lines

    # Check that the validation command was run
    mock_module.run_command.assert_called_once_with(to_bytes('cat %s' % tmpfile, errors='surrogate_or_strict'))

    # Check that the atomic_move method was called
    mock_module.atomic_move.assert_called_once_with(
        tmpfile,
        to_native(os.path.realpath(to_bytes(dest, errors='surrogate_or_strict')), errors='surrogate_or_strict'),
        unsafe_writes=False
    )

    # Clean up
    if os.path.exists(dest):
        os.remove(dest)
    if os.path.exists(tmpfile):
        os.remove(tmpfile)

def to_bytes(data, errors='strict'):
    if isinstance(data, bytes):
        return data
    return data.encode('utf-8', errors)

def to_native(data, errors='strict'):
    if isinstance(data, str):
        return data
    return data.decode('utf-8', errors)
