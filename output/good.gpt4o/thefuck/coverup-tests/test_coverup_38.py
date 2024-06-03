# file thefuck/shells/generic.py:98-101
# lines [98, 99, 100, 101]
# branches ['99->100', '99->101']

import pytest
import six
from thefuck.shells.generic import Generic

@pytest.fixture
def generic():
    return Generic()

def test_decode_utf8_py2(mocker, generic):
    mocker.patch('six.PY2', True)
    command_parts = [b'echo', b'hello']
    result = generic.decode_utf8(command_parts)
    assert result == ['echo', 'hello']

def test_decode_utf8_py3(mocker, generic):
    mocker.patch('six.PY2', False)
    command_parts = ['echo', 'hello']
    result = generic.decode_utf8(command_parts)
    assert result == command_parts
