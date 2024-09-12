# file: lib/ansible/cli/arguments/option_helpers.py:34-38
# asked: {"lines": [34, 35, 36, 37, 38], "branches": []}
# gained: {"lines": [34, 35, 36, 37, 38], "branches": []}

import argparse
import pytest
from unittest import mock
from ansible.cli.arguments.option_helpers import AnsibleVersion

def test_ansible_version_action(monkeypatch):
    # Mock the version function to return a specific version
    mock_version = mock.Mock(return_value='2.9.10')
    monkeypatch.setattr('ansible.cli.arguments.option_helpers.version', mock_version)
    
    # Mock the to_native function to return the version as is
    mock_to_native = mock.Mock(side_effect=lambda x: x)
    monkeypatch.setattr('ansible.cli.arguments.option_helpers.to_native', mock_to_native)
    
    # Create a parser and add the custom action
    parser = argparse.ArgumentParser(prog='ansible-playbook')
    parser.add_argument('--version', action=AnsibleVersion, nargs=0)
    
    # Mock the parser's exit method to prevent the test from exiting
    with mock.patch.object(parser, 'exit', side_effect=SystemExit) as mock_exit:
        with pytest.raises(SystemExit):
            parser.parse_args(['--version'])
        
        # Check that the version and to_native functions were called correctly
        mock_version.assert_called_once_with('ansible-playbook')
        mock_to_native.assert_called_once_with('2.9.10')
        
        # Check that the exit method was called
        mock_exit.assert_called_once()

