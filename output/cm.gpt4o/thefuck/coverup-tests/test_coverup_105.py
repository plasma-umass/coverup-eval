# file thefuck/shells/generic.py:116-122
# lines [116]
# branches []

import pytest
from unittest.mock import patch, MagicMock
from thefuck.shells.generic import Generic

@pytest.fixture
def generic():
    return Generic()

def test_put_to_history(generic, mocker):
    mocker.patch('thefuck.shells.generic.Generic.put_to_history', return_value=None)
    command = "echo 'Hello, World!'"
    generic.put_to_history(command)
    generic.put_to_history.assert_called_once_with(command)
