# file thefuck/rules/django_south_merge.py:7-8
# lines [7, 8]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.django_south_merge import get_new_command

def test_get_new_command():
    command = Command('python manage.py migrate app', '')
    new_command = get_new_command(command)
    assert new_command == 'python manage.py migrate app --merge'
