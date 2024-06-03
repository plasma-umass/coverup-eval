# file lib/ansible/cli/arguments/option_helpers.py:34-38
# lines [34, 35, 36, 37, 38]
# branches []

import argparse
import pytest
from unittest import mock

# Assuming the AnsibleVersion class is defined in ansible.cli.arguments.option_helpers
from ansible.cli.arguments.option_helpers import AnsibleVersion

def test_ansible_version_action(mocker, capsys):
    # Mock the to_native and version functions
    mock_to_native = mocker.patch('ansible.cli.arguments.option_helpers.to_native', return_value='2.9.10')
    mock_version = mocker.patch('ansible.cli.arguments.option_helpers.version', return_value='2.9.10')

    # Create a parser and add the AnsibleVersion action
    parser = argparse.ArgumentParser(prog='ansible-playbook')
    parser.add_argument('--version', action=AnsibleVersion, nargs=0)

    # Mock the parser.exit method to prevent the test from exiting
    mock_exit = mocker.patch.object(parser, 'exit')

    # Parse the arguments
    parser.parse_args(['--version'])

    # Assertions to verify the expected behavior
    mock_to_native.assert_called_once_with('2.9.10')
    mock_version.assert_called_once_with('ansible-playbook')
    mock_exit.assert_called_once()

    # Verify the output
    captured = capsys.readouterr()
    assert captured.out.strip() == '2.9.10'
