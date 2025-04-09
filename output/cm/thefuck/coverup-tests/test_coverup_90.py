# file thefuck/rules/django_south_merge.py:1-4
# lines [1, 2, 3, 4]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.django_south_merge import match

@pytest.fixture
def django_south_merge_error():
    return "manage.py migrate --merge: will just attempt the migration"

def test_match_with_django_south_merge_error(django_south_merge_error):
    command = Command('python manage.py migrate', django_south_merge_error)
    assert match(command)

def test_no_match_with_django_south_merge_error(django_south_merge_error):
    command = Command('python manage.py makemigrations', django_south_merge_error)
    assert not match(command)

def test_no_match_with_different_error():
    command = Command('python manage.py migrate', 'Some other error')
    assert not match(command)

def test_no_match_with_no_manage_py_in_script():
    command = Command('python script.py migrate', '--merge: will just attempt the migration')
    assert not match(command)

def test_no_match_with_no_migrate_in_script():
    command = Command('python manage.py makemigrations', '--merge: will just attempt the migration')
    assert not match(command)
