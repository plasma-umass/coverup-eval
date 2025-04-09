# file thefuck/types.py:54-56
# lines [54, 55, 56]
# branches []

import pytest
from thefuck.types import Command

@pytest.fixture
def mock_command():
    return Command(script='echo hello', output='hello\n')

def test_command_repr(mock_command):
    expected_repr = u'Command(script=echo hello, output=hello\n)'
    assert repr(mock_command) == expected_repr
