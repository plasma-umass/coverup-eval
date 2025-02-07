# file: lib/ansible/cli/arguments/option_helpers.py:293-298
# asked: {"lines": [293, 295, 296, 297, 298], "branches": []}
# gained: {"lines": [293, 295, 296, 297, 298], "branches": []}

import pytest
from argparse import ArgumentParser
from ansible.cli.arguments.option_helpers import add_meta_options
from ansible import constants as C

def test_add_meta_options():
    parser = ArgumentParser()
    add_meta_options(parser)
    args = parser.parse_args(['--force-handlers', '--flush-cache'])
    
    assert args.force_handlers == True
    assert args.flush_cache == True

    args = parser.parse_args([])
    
    assert args.force_handlers == C.DEFAULT_FORCE_HANDLERS
    assert args.flush_cache == False
