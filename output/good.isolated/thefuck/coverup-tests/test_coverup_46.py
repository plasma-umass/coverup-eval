# file thefuck/shells/generic.py:93-96
# lines [93, 94, 95, 96]
# branches ['94->95', '94->96']

import pytest
from thefuck.shells.generic import Generic
from unittest.mock import patch

@pytest.fixture
def generic_shell():
    return Generic()

def test_encode_utf8_py2(generic_shell):
    with patch('thefuck.shells.generic.six.PY2', True):
        command = u'echo Привет'
        encoded_command = generic_shell.encode_utf8(command)
        assert encoded_command == command.encode('utf8')

def test_encode_utf8_not_py2(generic_shell):
    with patch('thefuck.shells.generic.six.PY2', False):
        command = 'echo Hello'
        encoded_command = generic_shell.encode_utf8(command)
        assert encoded_command == command
