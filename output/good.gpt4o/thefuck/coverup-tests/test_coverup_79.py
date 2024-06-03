# file thefuck/rules/django_south_merge.py:7-8
# lines [7, 8]
# branches []

import pytest
from thefuck.rules.django_south_merge import get_new_command

def test_get_new_command():
    command = type('Command', (object,), {'script': 'migrate'})()
    new_command = get_new_command(command)
    assert new_command == 'migrate --merge'
