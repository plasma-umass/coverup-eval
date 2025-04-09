# file lib/ansible/modules/lineinfile.py:262-281
# lines [264, 265, 266, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281]
# branches ['270->271', '270->278', '271->272', '271->273', '275->276', '275->278', '278->exit', '278->279']

import os
import pytest
import tempfile
from ansible.modules.lineinfile import write_changes

@pytest.fixture
def mock_module(mocker):
    mock_module = mocker.MagicMock()
    mock_module.tmpdir = tempfile.gettempdir()
    mock_module.params = {
        'validate': 'echo %s',
        'unsafe_writes': False
    }
    mock_module.run_command.return_value = (0, '', '')  # Simulate successful validation
    mock_module.atomic_move.side_effect = lambda src, dest, unsafe_writes: os.rename(src, dest)
    return mock_module

def test_write_changes_with_validation(mock_module):
    # Setup
    dest = tempfile.mktemp()
    b_lines = [b"line1\n", b"line2\n"]

    # Exercise
    write_changes(mock_module, b_lines, dest)

    # Verify
    with open(dest, 'rb') as f:
        content = f.readlines()
    assert content == b_lines
    mock_module.run_command.assert_called_once()
    assert os.path.exists(dest)

    # Cleanup
    os.remove(dest)
