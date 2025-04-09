# file: lib/ansible/cli/arguments/option_helpers.py:232-240
# asked: {"lines": [232, 234, 235, 236, 237, 238, 239], "branches": []}
# gained: {"lines": [232, 234, 235, 236, 237, 238, 239], "branches": []}

import pytest
from argparse import ArgumentParser

def test_add_check_options(monkeypatch):
    from ansible.cli.arguments.option_helpers import add_check_options

    parser = ArgumentParser()
    add_check_options(parser)
    args = parser.parse_args(['--check', '--syntax-check', '--diff'])

    assert args.check is True
    assert args.syntax is True
    assert args.diff is True

    # Clean up by resetting the parser
    monkeypatch.setattr('argparse.ArgumentParser', ArgumentParser)
