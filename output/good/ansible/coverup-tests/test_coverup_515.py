# file lib/ansible/cli/arguments/option_helpers.py:232-240
# lines [232, 234, 235, 236, 237, 238, 239]
# branches []

import pytest
from ansible.cli.arguments.option_helpers import add_check_options
from argparse import ArgumentParser

def test_add_check_options(mocker):
    parser = ArgumentParser()
    mocker.patch('ansible.constants.DIFF_ALWAYS', False)
    add_check_options(parser)
    
    args = parser.parse_args(['--check'])
    assert args.check is True
    assert args.syntax is False
    assert args.diff is False

    args = parser.parse_args(['--syntax-check'])
    assert args.check is False
    assert args.syntax is True
    assert args.diff is False

    args = parser.parse_args(['-D'])
    assert args.check is False
    assert args.syntax is False
    assert args.diff is True

    # Cleanup is not necessary as ArgumentParser and mocker do not have side effects outside the test function
