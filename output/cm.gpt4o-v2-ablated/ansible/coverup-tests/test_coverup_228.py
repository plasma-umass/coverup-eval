# file: lib/ansible/cli/arguments/option_helpers.py:41-47
# asked: {"lines": [41, 42, 43, 44, 46, 47], "branches": []}
# gained: {"lines": [41, 42, 43, 44, 46, 47], "branches": []}

import pytest
import argparse

from ansible.cli.arguments.option_helpers import UnrecognizedArgument

def test_unrecognized_argument_action(monkeypatch):
    parser = argparse.ArgumentParser()
    parser.register('action', 'unrecognized', UnrecognizedArgument)
    parser.add_argument('--foo', action='unrecognized')

    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(['--foo', 'bar'])
    
    assert excinfo.value.code == 2

    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(['--foo'])
    
    assert excinfo.value.code == 2
