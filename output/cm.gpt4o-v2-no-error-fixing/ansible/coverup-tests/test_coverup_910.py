# file: lib/ansible/cli/arguments/option_helpers.py:34-38
# asked: {"lines": [36, 37, 38], "branches": []}
# gained: {"lines": [36, 37, 38], "branches": []}

import argparse
import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.arguments.option_helpers import AnsibleVersion

def test_ansible_version_call(monkeypatch):
    # Mock the version function and the parser.exit method
    mock_version = MagicMock(return_value="2.9.10")
    mock_exit = MagicMock()
    
    # Apply the monkeypatch for the version function and parser.exit
    monkeypatch.setattr("ansible.cli.arguments.option_helpers.version", mock_version)
    monkeypatch.setattr("argparse.ArgumentParser.exit", mock_exit)
    
    # Create a parser and add the AnsibleVersion action
    parser = argparse.ArgumentParser(prog="ansible-playbook")
    parser.add_argument("--version", action=AnsibleVersion, nargs=0)
    
    # Parse the arguments to trigger the __call__ method
    parser.parse_args(["--version"])
    
    # Assertions to verify the expected behavior
    mock_version.assert_called_once_with("ansible-playbook")
    mock_exit.assert_called_once()
