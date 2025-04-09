# file lib/ansible/cli/arguments/option_helpers.py:277-280
# lines [279, 280]
# branches []

import pytest
from unittest import mock
from argparse import ArgumentParser
import ansible.constants as C
from ansible.cli.arguments.option_helpers import add_fork_options

def test_add_fork_options(mocker):
    parser = ArgumentParser()
    mocker.patch('ansible.constants.DEFAULT_FORKS', 5)
    
    add_fork_options(parser)
    
    args = parser.parse_args(['--forks', '10'])
    assert args.forks == 10
    
    args = parser.parse_args([])
    assert args.forks == 5
