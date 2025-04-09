# file: lib/ansible/cli/arguments/option_helpers.py:216-221
# asked: {"lines": [216, 218, 219, 220, 221], "branches": []}
# gained: {"lines": [216, 218, 219, 220, 221], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_async_options
from ansible import constants as C

def test_add_async_options():
    parser = ArgumentParser()
    add_async_options(parser)
    args = parser.parse_args(['-P', '10', '-B', '20'])
    
    assert args.poll_interval == 10
    assert args.seconds == 20

    args = parser.parse_args([])
    
    assert args.poll_interval == C.DEFAULT_POLL_INTERVAL
    assert args.seconds == 0
