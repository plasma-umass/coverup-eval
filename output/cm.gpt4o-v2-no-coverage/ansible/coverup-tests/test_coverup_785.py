# file: lib/ansible/plugins/action/pause.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
from io import BytesIO
from ansible.plugins.action.pause import clear_line

def test_clear_line():
    # Setup
    stdout = BytesIO()

    # Execute
    clear_line(stdout)

    # Assert
    assert stdout.getvalue() == b'\x1b[\r\x1b[\x1b[K'

    # Cleanup
    stdout.close()
