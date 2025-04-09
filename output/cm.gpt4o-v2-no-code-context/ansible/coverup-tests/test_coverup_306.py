# file: lib/ansible/utils/context_objects.py:63-82
# asked: {"lines": [63, 64, 74, 75, 76, 77, 78, 80, 81, 82], "branches": [[76, 77], [76, 78]]}
# gained: {"lines": [63, 64, 74, 75, 76, 77, 78, 80, 81, 82], "branches": [[76, 77], [76, 78]]}

import pytest
from ansible.utils.context_objects import CLIArgs

class TestCLIArgs:
    
    def test_cliargs_init(self):
        mapping = {'arg1': 'value1', 'arg2': 'value2'}
        cli_args = CLIArgs(mapping)
        assert cli_args['arg1'] == 'value1'
        assert cli_args['arg2'] == 'value2'
    
    def test_cliargs_from_options(self, mocker):
        options = mocker.Mock()
        options.arg1 = 'value1'
        options.arg2 = 'value2'
        cli_args = CLIArgs.from_options(options)
        assert cli_args['arg1'] == 'value1'
        assert cli_args['arg2'] == 'value2'
