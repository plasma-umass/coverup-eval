# file thefuck/rules/rm_root.py:6-11
# lines [6, 7, 8, 9, 10, 11]
# branches []

import pytest
from thefuck.types import Command
from thefuck.rules.rm_root import match

@pytest.fixture
def rm_root_command():
    return Command('rm /', 'rm: it is dangerous to operate recursively on ‘/’\nrm: use --no-preserve-root to override this failsafe')

def test_match(mocker, rm_root_command):
    mocker.patch('thefuck.rules.rm_root.sudo_support', lambda x: x)
    assert match(rm_root_command)

def test_not_match_no_rm_in_script(mocker):
    mocker.patch('thefuck.rules.rm_root.sudo_support', lambda x: x)
    command = Command('ls /', 'ls: cannot access /: No such file or directory')
    assert not match(command)

def test_not_match_no_slash_in_script(mocker):
    mocker.patch('thefuck.rules.rm_root.sudo_support', lambda x: x)
    command = Command('rm -rf', 'rm: missing operand')
    assert not match(command)

def test_not_match_no_preserve_root_in_script(mocker):
    mocker.patch('thefuck.rules.rm_root.sudo_support', lambda x: x)
    command = Command('rm --no-preserve-root /', 'rm: it is dangerous to operate recursively on ‘/’')
    assert not match(command)

def test_not_match_no_preserve_root_in_output(mocker):
    mocker.patch('thefuck.rules.rm_root.sudo_support', lambda x: x)
    command = Command('rm /', 'rm: refusing to remove ‘/’ directory: use --preserve-root')
    assert not match(command)
