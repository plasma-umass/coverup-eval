# file: lib/ansible/plugins/action/pause.py:70-72
# asked: {"lines": [71, 72], "branches": []}
# gained: {"lines": [71, 72], "branches": []}

import pytest
from io import BytesIO
from ansible.plugins.action.pause import clear_line

def test_clear_line():
    # Create a BytesIO object to mock stdout
    mock_stdout = BytesIO()

    # Call the function with the mock stdout
    clear_line(mock_stdout)

    # Get the output from the mock stdout
    output = mock_stdout.getvalue()

    # Assert that the correct escape sequences were written to stdout
    assert output == b'\x1b[\r\x1b[\x1b[K'

    # Clean up
    mock_stdout.close()
