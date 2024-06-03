# file lib/ansible/cli/arguments/option_helpers.py:41-47
# lines [41, 42, 43, 44, 46, 47]
# branches []

import pytest
import argparse
from ansible.cli.arguments.option_helpers import UnrecognizedArgument

def test_unrecognized_argument(mocker):
    parser = argparse.ArgumentParser()
    parser.register('action', 'unrecognized', UnrecognizedArgument)
    
    mock_error = mocker.patch.object(parser, 'error', autospec=True)
    
    parser.add_argument('--foo', action='unrecognized')
    
    parser.parse_args(['--foo'])
    
    mock_error.assert_called_once_with('unrecognized arguments: --foo')
