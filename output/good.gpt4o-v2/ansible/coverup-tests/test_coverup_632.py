# file: lib/ansible/cli/arguments/option_helpers.py:34-38
# asked: {"lines": [34, 35, 36, 37, 38], "branches": []}
# gained: {"lines": [34, 35, 36, 37, 38], "branches": []}

import pytest
import argparse
from ansible.module_utils._text import to_native
from ansible.cli.arguments.option_helpers import AnsibleVersion
from ansible.release import __version__ as ansible_version
from unittest.mock import patch

class TestAnsibleVersion:
    
    @patch('ansible.cli.arguments.option_helpers.version', return_value=ansible_version)
    @patch('argparse.ArgumentParser.exit')
    @patch('builtins.print')
    def test_ansible_version_action(self, mock_print, mock_exit, mock_version):
        parser = argparse.ArgumentParser(prog='ansible-playbook')
        namespace = argparse.Namespace()
        action = AnsibleVersion(option_strings=['--version'], dest='version', nargs=0)
        
        action(parser, namespace, values=None)
        
        mock_print.assert_called_once_with(to_native(ansible_version))
        mock_exit.assert_called_once()

