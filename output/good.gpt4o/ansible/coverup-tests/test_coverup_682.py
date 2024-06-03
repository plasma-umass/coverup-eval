# file lib/ansible/cli/arguments/option_helpers.py:361-364
# lines [361, 363, 364]
# branches []

import pytest
from argparse import ArgumentParser
from unittest.mock import patch

# Assuming the function add_runtask_options is imported from the module
from ansible.cli.arguments.option_helpers import add_runtask_options

def test_add_runtask_options():
    parser = ArgumentParser()
    add_runtask_options(parser)
    
    # Test with no extra-vars
    args = parser.parse_args([])
    assert args.extra_vars == []

    # Test with extra-vars as key=value
    args = parser.parse_args(['-e', 'key=value'])
    assert args.extra_vars == ['key=value']

    # Test with extra-vars as YAML/JSON file
    with patch('ansible.cli.arguments.option_helpers.maybe_unfrack_path', return_value='@/path/to/file'):
        args = parser.parse_args(['-e', '@/path/to/file'])
        assert args.extra_vars == ['@/path/to/file']

    # Test with multiple extra-vars
    args = parser.parse_args(['-e', 'key1=value1', '-e', 'key2=value2'])
    assert args.extra_vars == ['key1=value1', 'key2=value2']
