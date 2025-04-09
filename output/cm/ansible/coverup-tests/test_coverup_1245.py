# file lib/ansible/cli/arguments/option_helpers.py:340-358
# lines [347, 348, 350, 352, 353, 354, 355, 356, 358]
# branches ['347->348', '347->350']

import pytest
from argparse import ArgumentParser
from unittest.mock import MagicMock

# Assuming C and unfrack_path() are defined elsewhere in the ansible.cli.arguments.option_helpers module
from ansible.cli.arguments.option_helpers import add_runas_prompt_options, C, unfrack_path

@pytest.fixture
def parser():
    return ArgumentParser()

@pytest.fixture
def runas_group():
    return "Runas Options"

def test_add_runas_prompt_options_with_runas_group(parser, runas_group, mocker):
    mocker.patch.object(parser, 'add_argument_group')
    mocker.patch.object(parser, 'add_mutually_exclusive_group', return_value=MagicMock())

    add_runas_prompt_options(parser, runas_group)

    parser.add_argument_group.assert_any_call(runas_group)
    parser.add_mutually_exclusive_group.assert_called_once()

    # Verify that the mutually exclusive group was added to the parser
    assert parser.add_argument_group.call_count == 2, "Expected two calls to add_argument_group, one for runas_group and one for runas_pass_group"

    # Cleanup is handled by pytest fixtures, no additional cleanup is necessary
