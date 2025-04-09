# file thefuck/rules/cat_dir.py:13-14
# lines [13, 14]
# branches []

import pytest
from thefuck.rules.cat_dir import get_new_command

def test_get_new_command():
    command = type('Command', (object,), {'script': 'cat directory'})()
    new_command = get_new_command(command)
    assert new_command == 'ls directory'

    command = type('Command', (object,), {'script': 'cat file.txt'})()
    new_command = get_new_command(command)
    assert new_command == 'ls file.txt'
