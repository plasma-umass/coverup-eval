# file lib/ansible/cli/arguments/option_helpers.py:361-364
# lines [361, 363, 364]
# branches []

import pytest
from ansible.cli.arguments.option_helpers import add_runtask_options
from argparse import ArgumentParser

# Define a fixture for the ArgumentParser
@pytest.fixture
def parser():
    return ArgumentParser()

# Define a test function to improve coverage
def test_add_runtask_options(parser, tmp_path):
    # Create a temporary file to simulate a file with '@' prefix
    temp_file = tmp_path / "vars.yml"
    temp_file.write_text("key: value")

    # Use the parser fixture to add runtask options
    add_runtask_options(parser)

    # Parse the arguments with a file and without a file
    args_with_file = parser.parse_args(['-e', f"@{temp_file}"])
    args_without_file = parser.parse_args(['-e', 'key=value'])

    # Assertions to check if the extra_vars are correctly set
    assert args_with_file.extra_vars[0].endswith('vars.yml')
    assert args_without_file.extra_vars == ['key=value']

    # Cleanup is not necessary as pytest handles the temporary directory
