# file lib/ansible/cli/arguments/option_helpers.py:34-38
# lines [36, 37, 38]
# branches []

import argparse
import pytest
from ansible.release import __version__ as ansible_version
from ansible.cli.arguments.option_helpers import AnsibleVersion
from ansible.module_utils._text import to_native

def test_ansible_version_action(mocker):
    # Mock the parser and namespace
    parser = mocker.MagicMock()
    namespace = mocker.MagicMock()
    parser.prog = 'ansible-test'

    # Mock the version function to return a specific version
    version_mock = mocker.patch('ansible.cli.arguments.option_helpers.version', return_value=ansible_version)

    # Mock the print function to check if it's called with the correct version
    print_mock = mocker.patch('builtins.print')

    # Mock the parser.exit so it doesn't actually exit
    exit_mock = mocker.patch.object(parser, 'exit')

    # Create the AnsibleVersion action
    action = AnsibleVersion(option_strings=[], dest='version')

    # Call the action
    action(parser, namespace, None)

    # Assert that the version function was called with the correct program name
    version_mock.assert_called_once_with('ansible-test')

    # Assert that the print function was called with the correct version
    expected_version = to_native(ansible_version)
    print_mock.assert_called_once_with(expected_version)

    # Assert that the parser.exit was called
    exit_mock.assert_called_once()
