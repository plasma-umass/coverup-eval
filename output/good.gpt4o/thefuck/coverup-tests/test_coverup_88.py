# file thefuck/rules/pacman_invalid_option.py:15-17
# lines [15, 16, 17]
# branches []

import re
import pytest
from thefuck.rules.pacman_invalid_option import get_new_command
from thefuck.types import Command

def test_get_new_command():
    command = Command(script='pacman -d something', output='')
    new_command = get_new_command(command)
    assert new_command == 'pacman -D something'

    command = Command(script='pacman -f something', output='')
    new_command = get_new_command(command)
    assert new_command == 'pacman -F something'

    command = Command(script='pacman -q something', output='')
    new_command = get_new_command(command)
    assert new_command == 'pacman -Q something'

    command = Command(script='pacman -r something', output='')
    new_command = get_new_command(command)
    assert new_command == 'pacman -R something'

    command = Command(script='pacman -s something', output='')
    new_command = get_new_command(command)
    assert new_command == 'pacman -S something'

    command = Command(script='pacman -t something', output='')
    new_command = get_new_command(command)
    assert new_command == 'pacman -T something'

    command = Command(script='pacman -u something', output='')
    new_command = get_new_command(command)
    assert new_command == 'pacman -U something'

    command = Command(script='pacman -v something', output='')
    new_command = get_new_command(command)
    assert new_command == 'pacman -V something'
