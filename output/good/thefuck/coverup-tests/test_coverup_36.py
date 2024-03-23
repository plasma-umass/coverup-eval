# file thefuck/shells/generic.py:98-101
# lines [98, 99, 100, 101]
# branches ['99->100', '99->101']

import pytest
from thefuck.shells.generic import Generic
from unittest.mock import patch

@pytest.fixture
def generic_shell():
    return Generic()

def test_decode_utf8_py2(generic_shell):
    with patch('six.PY2', True):
        command_parts = [b'foo', b'bar']
        decoded_parts = generic_shell.decode_utf8(command_parts)
        assert decoded_parts == ['foo', 'bar']

def test_decode_utf8_not_py2(generic_shell):
    with patch('six.PY2', False):
        command_parts = ['foo', 'bar']
        decoded_parts = generic_shell.decode_utf8(command_parts)
        assert decoded_parts == command_parts
