# file: lib/ansible/cli/arguments/option_helpers.py:28-31
# asked: {"lines": [28, 29, 30, 31], "branches": []}
# gained: {"lines": [28, 29, 30, 31], "branches": []}

import pytest
import argparse
import operator
from ansible.cli.arguments.option_helpers import SortingHelpFormatter

def test_sorting_help_formatter_add_arguments(monkeypatch):
    class MockAction:
        def __init__(self, option_strings):
            self.option_strings = option_strings

    actions = [MockAction(['--b']), MockAction(['--a']), MockAction(['--c'])]

    formatter = SortingHelpFormatter(prog='test')
    
    def mock_add_arguments(self, actions):
        assert [action.option_strings for action in actions] == [['--a'], ['--b'], ['--c']]
    
    monkeypatch.setattr(argparse.HelpFormatter, 'add_arguments', mock_add_arguments)
    
    formatter.add_arguments(actions)
