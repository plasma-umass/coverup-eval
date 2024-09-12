# file: lib/ansible/utils/context_objects.py:63-82
# asked: {"lines": [63, 64, 74, 75, 76, 77, 78, 80, 81, 82], "branches": [[76, 77], [76, 78]]}
# gained: {"lines": [63, 64, 74, 75, 76, 77, 78, 80, 81, 82], "branches": [[76, 77], [76, 78]]}

import pytest
from ansible.utils.context_objects import CLIArgs, _make_immutable
from unittest.mock import patch, MagicMock

def test_cliargs_init():
    # Mock the _make_immutable function
    with patch('ansible.utils.context_objects._make_immutable', side_effect=lambda x: x):
        mapping = {'key1': 'value1', 'key2': 'value2'}
        cli_args = CLIArgs(mapping)
        
        # Verify that the CLIArgs object is initialized correctly
        assert cli_args['key1'] == 'value1'
        assert cli_args['key2'] == 'value2'

def test_cliargs_from_options():
    # Mock the options object
    options = MagicMock()
    options.key1 = 'value1'
    options.key2 = 'value2'
    
    # Mock the _make_immutable function
    with patch('ansible.utils.context_objects._make_immutable', side_effect=lambda x: x):
        cli_args = CLIArgs.from_options(options)
        
        # Verify that the CLIArgs object is initialized correctly from options
        assert cli_args['key1'] == 'value1'
        assert cli_args['key2'] == 'value2'
