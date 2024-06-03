# file thefuck/rules/django_south_merge.py:1-4
# lines [1, 2, 3, 4]
# branches []

import pytest
from thefuck.rules.django_south_merge import match

def test_match():
    command = type('Command', (object,), {})()
    command.script = 'python manage.py migrate'
    command.output = '--merge: will just attempt the migration'
    
    assert match(command) == True

    command.script = 'python manage.py runserver'
    assert match(command) == False

    command.script = 'python manage.py migrate'
    command.output = 'some other output'
    assert match(command) == False

    command.script = 'python manage.py migrate'
    command.output = '--merge: will just attempt the migration'
    assert match(command) == True
