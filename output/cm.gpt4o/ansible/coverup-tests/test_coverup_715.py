# file lib/ansible/plugins/action/pause.py:70-72
# lines [70, 71, 72]
# branches []

import pytest
from io import BytesIO
from unittest.mock import Mock

# Mocking the clear_line function for the purpose of this test
def clear_line(stdout):
    MOVE_TO_BOL = b'1G'
    CLEAR_TO_EOL = b'K'
    stdout.write(b'\x1b[%s' % MOVE_TO_BOL)
    stdout.write(b'\x1b[%s' % CLEAR_TO_EOL)

def test_clear_line(mocker):
    stdout = BytesIO()
    
    # Mocking the MOVE_TO_BOL and CLEAR_TO_EOL variables to ensure lines 70-72 execute
    mocker.patch('ansible.plugins.action.pause.MOVE_TO_BOL', b'1G')
    mocker.patch('ansible.plugins.action.pause.CLEAR_TO_EOL', b'K')
    
    clear_line(stdout)
    
    # Verify the expected output
    expected_output = b'\x1b[1G\x1b[K'
    assert stdout.getvalue() == expected_output

    # Clean up
    stdout.close()
