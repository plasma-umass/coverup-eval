# file: lib/ansible/cli/arguments/option_helpers.py:41-47
# asked: {"lines": [41, 42, 43, 44, 46, 47], "branches": []}
# gained: {"lines": [41, 42, 43, 44, 46, 47], "branches": []}

import pytest
import argparse
from ansible.cli.arguments.option_helpers import UnrecognizedArgument

def test_unrecognized_argument_init():
    option_strings = ['--test']
    dest = 'test'
    action = UnrecognizedArgument(option_strings, dest)
    assert action.option_strings == option_strings
    assert action.dest == dest
    assert action.const is True
    assert action.default is None
    assert action.required is False
    assert action.help is None
    assert action.nargs == 0

def test_unrecognized_argument_call(mocker):
    parser = mocker.Mock(spec=argparse.ArgumentParser)
    namespace = argparse.Namespace()
    values = None
    option_string = '--test'
    
    action = UnrecognizedArgument(['--test'], 'test')
    action(parser, namespace, values, option_string)
    
    parser.error.assert_called_once_with('unrecognized arguments: --test')
