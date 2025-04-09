# file: lib/ansible/cli/arguments/option_helpers.py:216-221
# asked: {"lines": [216, 218, 219, 220, 221], "branches": []}
# gained: {"lines": [216, 218, 219, 220, 221], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_async_options
import ansible.constants as C

def test_add_async_options(monkeypatch):
    # Create a parser object
    parser = ArgumentParser()

    # Mock the default poll interval
    default_poll_interval = 15
    monkeypatch.setattr(C, 'DEFAULT_POLL_INTERVAL', default_poll_interval)

    # Call the function to add async options to the parser
    add_async_options(parser)

    # Parse arguments to ensure the options are added correctly
    args = parser.parse_args(['-P', '10', '-B', '20'])

    # Assertions to verify the options are set correctly
    assert args.poll_interval == 10
    assert args.seconds == 20

    # Parse arguments with default values
    args = parser.parse_args([])

    # Assertions to verify the default values
    assert args.poll_interval == default_poll_interval
    assert args.seconds == 0
