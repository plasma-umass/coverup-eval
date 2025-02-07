# file: lib/ansible/cli/arguments/option_helpers.py:41-47
# asked: {"lines": [47], "branches": []}
# gained: {"lines": [47], "branches": []}

import pytest
import argparse
from ansible.cli.arguments.option_helpers import UnrecognizedArgument

def test_unrecognized_argument_call(monkeypatch):
    def mock_error(message):
        assert message == 'unrecognized arguments: --foo'
        raise SystemExit(2)

    parser = argparse.ArgumentParser()
    parser.error = mock_error
    namespace = argparse.Namespace()
    action = UnrecognizedArgument(option_strings=['--foo'], dest='foo')

    with pytest.raises(SystemExit) as excinfo:
        action(parser, namespace, None, option_string='--foo')
    assert excinfo.value.code == 2
