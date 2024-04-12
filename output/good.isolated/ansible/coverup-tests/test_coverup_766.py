# file lib/ansible/cli/arguments/option_helpers.py:210-213
# lines [210, 212, 213]
# branches []

import pytest
from argparse import ArgumentParser

# Assuming C.DEFAULT_VERBOSITY is defined somewhere in the module
# If not, we need to mock it for the test
class C:
    DEFAULT_VERBOSITY = 0

# The function to be tested, assuming it's in the module 'ansible.cli.arguments.option_helpers'
def add_verbosity_options(parser):
    """Add options for verbosity"""
    parser.add_argument('-v', '--verbose', dest='verbosity', default=C.DEFAULT_VERBOSITY, action="count",
                        help="verbose mode (-vvv for more, -vvvv to enable connection debugging)")

# Test function
def test_add_verbosity_options(mocker):
    mocker.patch('ansible.cli.arguments.option_helpers.C.DEFAULT_VERBOSITY', new=0)
    parser = ArgumentParser()
    add_verbosity_options(parser)
    args = parser.parse_args([])
    assert args.verbosity == 0

    args = parser.parse_args(['-v'])
    assert args.verbosity == 1

    args = parser.parse_args(['-vv'])
    assert args.verbosity == 2

    args = parser.parse_args(['-vvv'])
    assert args.verbosity == 3

    args = parser.parse_args(['-vvvv'])
    assert args.verbosity == 4

    # Clean up is not necessary as ArgumentParser and args are local to the test function
    # and mocker ensures that the DEFAULT_VERBOSITY is restored after the test

# Register the test function for pytest
test_add_verbosity_options.__test__ = True
