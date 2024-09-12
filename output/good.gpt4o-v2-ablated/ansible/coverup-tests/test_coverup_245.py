# file: lib/ansible/cli/arguments/option_helpers.py:293-298
# asked: {"lines": [293, 295, 296, 297, 298], "branches": []}
# gained: {"lines": [293, 295, 296, 297, 298], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_meta_options
from ansible import constants as C

@pytest.fixture
def parser():
    return ArgumentParser()

def test_add_meta_options_force_handlers(parser, monkeypatch):
    monkeypatch.setattr(C, 'DEFAULT_FORCE_HANDLERS', False)
    add_meta_options(parser)
    args = parser.parse_args(['--force-handlers'])
    assert args.force_handlers is True

def test_add_meta_options_flush_cache(parser):
    add_meta_options(parser)
    args = parser.parse_args(['--flush-cache'])
    assert args.flush_cache is True

def test_add_meta_options_defaults(parser, monkeypatch):
    monkeypatch.setattr(C, 'DEFAULT_FORCE_HANDLERS', False)
    add_meta_options(parser)
    args = parser.parse_args([])
    assert args.force_handlers == C.DEFAULT_FORCE_HANDLERS
    assert args.flush_cache is False
