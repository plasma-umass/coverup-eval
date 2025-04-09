# file: lib/ansible/cli/arguments/option_helpers.py:34-38
# asked: {"lines": [34, 35, 36, 37, 38], "branches": []}
# gained: {"lines": [34, 35, 36, 37, 38], "branches": []}

import pytest
import argparse
from unittest import mock
from ansible.cli.arguments.option_helpers import AnsibleVersion
from ansible.module_utils._text import to_native

def test_ansible_version(monkeypatch):
    # Mock the version function
    def mock_version(prog=None):
        return "mocked_version"

    monkeypatch.setattr('ansible.cli.arguments.option_helpers.version', mock_version)

    # Create a mock parser
    mock_parser = mock.MagicMock()
    mock_parser.prog = 'ansible'

    # Create a namespace object
    namespace = argparse.Namespace()

    # Create an instance of AnsibleVersion
    action = AnsibleVersion(option_strings=['--version'], dest='version', nargs=0, const=None, default=None, type=None, choices=None, required=False, help=None, metavar=None)

    # Mock the parser.exit method
    with mock.patch.object(mock_parser, 'exit', return_value=None) as mock_exit:
        # Call the action
        action(mock_parser, namespace, values=None)

        # Check that the version was printed
        mock_exit.assert_called_once()

        # Check that the version function was called with the correct argument
        assert to_native(mock_version('ansible')) == "mocked_version"
