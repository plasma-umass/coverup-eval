# file thefuck/shells/generic.py:93-96
# lines [93, 94, 95, 96]
# branches ['94->95', '94->96']

import pytest
import six
from thefuck.shells.generic import Generic

@pytest.mark.parametrize("command, expected", [
    ("test", b"test" if six.PY2 else "test"),
    ("another test", b"another test" if six.PY2 else "another test")
])
def test_encode_utf8(command, expected):
    generic = Generic()
    result = generic.encode_utf8(command)
    assert result == expected

# Clean up after the test
def test_cleanup(mocker):
    mocker.stopall()
