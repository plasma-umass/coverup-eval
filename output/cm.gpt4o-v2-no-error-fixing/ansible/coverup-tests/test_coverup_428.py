# file: lib/ansible/cli/arguments/option_helpers.py:293-298
# asked: {"lines": [293, 295, 296, 297, 298], "branches": []}
# gained: {"lines": [293, 295, 296, 297, 298], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_meta_options
from ansible import constants as C

def test_add_meta_options_force_handlers():
    parser = ArgumentParser()
    add_meta_options(parser)
    args = parser.parse_args(['--force-handlers'])
    assert args.force_handlers is True

def test_add_meta_options_flush_cache():
    parser = ArgumentParser()
    add_meta_options(parser)
    args = parser.parse_args(['--flush-cache'])
    assert args.flush_cache is True

def test_add_meta_options_defaults():
    parser = ArgumentParser()
    add_meta_options(parser)
    args = parser.parse_args([])
    assert args.force_handlers == C.DEFAULT_FORCE_HANDLERS
    assert args.flush_cache is False
