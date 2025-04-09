# file: lib/ansible/cli/arguments/option_helpers.py:216-221
# asked: {"lines": [216, 218, 219, 220, 221], "branches": []}
# gained: {"lines": [216, 218, 219, 220, 221], "branches": []}

import pytest
from argparse import ArgumentParser, Namespace
from ansible.cli.arguments.option_helpers import add_async_options
import ansible.constants as C

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_async_options_defaults(parser):
    add_async_options(parser)
    args = parser.parse_args([])
    assert args.poll_interval == C.DEFAULT_POLL_INTERVAL
    assert args.seconds == 0

def test_add_async_options_custom_poll_interval(parser):
    add_async_options(parser)
    args = parser.parse_args(['-P', '10'])
    assert args.poll_interval == 10

def test_add_async_options_custom_background_seconds(parser):
    add_async_options(parser)
    args = parser.parse_args(['-B', '20'])
    assert args.seconds == 20

def test_add_async_options_custom_both(parser):
    add_async_options(parser)
    args = parser.parse_args(['-P', '15', '-B', '30'])
    assert args.poll_interval == 15
    assert args.seconds == 30
