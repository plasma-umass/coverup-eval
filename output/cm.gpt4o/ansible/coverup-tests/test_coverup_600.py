# file lib/ansible/cli/arguments/option_helpers.py:373-378
# lines [373, 375, 376, 377, 378]
# branches []

import pytest
from unittest import mock
from argparse import ArgumentParser
import ansible.constants as C

def test_add_subset_options():
    from ansible.cli.arguments.option_helpers import add_subset_options

    parser = ArgumentParser()
    add_subset_options(parser)

    args = parser.parse_args(['-t', 'tag1', '--skip-tags', 'tag2'])

    assert args.tags == ['tag1']
    assert args.skip_tags == ['tag2']

    # Clean up to ensure no side effects
    del parser
    del args
