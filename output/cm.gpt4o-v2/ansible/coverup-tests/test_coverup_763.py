# file: lib/ansible/plugins/action/pause.py:70-72
# asked: {"lines": [70, 71, 72], "branches": []}
# gained: {"lines": [70, 71, 72], "branches": []}

import pytest
from io import BytesIO
from ansible.plugins.action.pause import clear_line, MOVE_TO_BOL, CLEAR_TO_EOL

def test_clear_line():
    # Create a BytesIO object to mock stdout
    mock_stdout = BytesIO()

    # Call the function with the mock stdout
    clear_line(mock_stdout)

    # Get the output from the mock stdout
    output = mock_stdout.getvalue()

    # Assert that the correct escape sequences were written to stdout
    expected_output = b'\x1b[%s\x1b[%s' % (MOVE_TO_BOL, CLEAR_TO_EOL)
    assert output == expected_output

    # Clean up
    mock_stdout.close()
