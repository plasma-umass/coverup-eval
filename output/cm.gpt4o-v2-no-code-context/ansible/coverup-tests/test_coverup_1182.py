# file: lib/ansible/cli/arguments/option_helpers.py:41-47
# asked: {"lines": [43, 44, 47], "branches": []}
# gained: {"lines": [43, 44, 47], "branches": []}

import argparse
import pytest

from ansible.cli.arguments.option_helpers import UnrecognizedArgument

def test_unrecognized_argument_init():
    action = UnrecognizedArgument(option_strings=['--foo'], dest='foo')
    assert action.option_strings == ['--foo']
    assert action.dest == 'foo'
    assert action.nargs == 0
    assert action.const is True
    assert action.default is None
    assert action.required is False
    assert action.help is None

def test_unrecognized_argument_call(monkeypatch):
    parser = argparse.ArgumentParser()
    parser.register('action', 'unrecognized', UnrecognizedArgument)
    parser.add_argument('--foo', action='unrecognized')

    def mock_error(message):
        raise ValueError(message)

    monkeypatch.setattr(parser, 'error', mock_error)

    with pytest.raises(ValueError, match='unrecognized arguments: --foo'):
        parser.parse_args(['--foo'])
