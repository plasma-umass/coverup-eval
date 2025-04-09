# file thefuck/rules/dirty_unzip.py:40-42
# lines [40, 41, 42]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.dirty_unzip import get_new_command
from thefuck.shells import shell
import os

# Assuming the _zip_file function is defined elsewhere in the module
# and it extracts the zip file name from the command
# If it's not defined, we'll need to mock it

@pytest.fixture
def mock_zip_file(mocker):
    return mocker.patch('thefuck.rules.dirty_unzip._zip_file', return_value='archive.zip')

def test_get_new_command(mock_zip_file, tmpdir):
    test_zip_file = tmpdir.join('archive.zip')
    test_zip_file.write('content')

    command = Command('unzip', 'unzip archive.zip')
    new_command = get_new_command(command)

    expected_command = 'unzip -d archive'
    assert new_command == expected_command

    # Clean up
    test_zip_file.remove()
