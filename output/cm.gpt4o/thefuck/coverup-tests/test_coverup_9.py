# file thefuck/rules/choco_install.py:10-22
# lines [10, 12, 13, 14, 16, 18, 21, 22]
# branches ['12->13', '12->22', '13->12', '13->21']

import pytest
from thefuck.rules.choco_install import get_new_command
from thefuck.types import Command

def test_get_new_command():
    # Test case where the package name is found and modified
    command = Command('choco install somepackage', ['choco', 'install', 'somepackage'])
    new_command = get_new_command(command)
    assert new_command == 'choco install somepackage.install'

    # Test case where the package name is not found (should return empty list)
    command = Command('choco install -y', ['choco', 'install', '-y'])
    new_command = get_new_command(command)
    assert new_command == []

    # Test case where the package name contains '=' (should be considered a parameter)
    command = Command('choco install somepackage=1.0', ['choco', 'install', 'somepackage=1.0'])
    new_command = get_new_command(command)
    assert new_command == []

    # Test case where the package name contains '/' (should be considered a parameter)
    command = Command('choco install some/package', ['choco', 'install', 'some/package'])
    new_command = get_new_command(command)
    assert new_command == []

    # Test case where the package name starts with '-' (should be considered a parameter)
    command = Command('choco install -somepackage', ['choco', 'install', '-somepackage'])
    new_command = get_new_command(command)
    assert new_command == []

    # Test case where the package name is 'chocolatey' (should be considered a package)
    command = Command('choco install chocolatey', ['choco', 'install', 'chocolatey'])
    new_command = get_new_command(command)
    assert new_command == 'choco install chocolatey.install'
