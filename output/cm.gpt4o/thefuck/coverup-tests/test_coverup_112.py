# file thefuck/shells/generic.py:93-96
# lines [95]
# branches ['94->95']

import pytest
import six
from thefuck.shells.generic import Generic

@pytest.fixture
def generic():
    return Generic()

def test_encode_utf8_py2(mocker, generic):
    mocker.patch('six.PY2', True)
    command = 'test'
    encoded_command = generic.encode_utf8(command)
    assert encoded_command == command.encode('utf8')

def test_encode_utf8_py3(mocker, generic):
    mocker.patch('six.PY2', False)
    command = 'test'
    encoded_command = generic.encode_utf8(command)
    assert encoded_command == command
