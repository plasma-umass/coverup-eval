# file lib/ansible/modules/pip.py:628-631
# lines [628, 629, 630, 631]
# branches ['629->630', '629->631']

import pytest
from unittest.mock import MagicMock

# Assuming the Package class is defined in ansible.modules.pip
from ansible.modules.pip import Package

def test_package_str_plain_package(mocker):
    # Mock the to_native function
    to_native_mock = mocker.patch('ansible.modules.pip.to_native', return_value='mocked_requirement')

    # Create an instance of the Package class with _plain_package set to True
    package = Package('requirement')
    package._plain_package = True
    package._requirement = 'requirement'

    # Assert that the __str__ method returns the mocked requirement
    assert str(package) == 'mocked_requirement'
    to_native_mock.assert_called_once_with('requirement')

def test_package_str_not_plain_package():
    # Create an instance of the Package class with _plain_package set to False
    package = Package('package_name')
    package._plain_package = False
    package.package_name = 'package_name'

    # Assert that the __str__ method returns the package name
    assert str(package) == 'package_name'
