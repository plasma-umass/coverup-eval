# file thefuck/logs.py:93-114
# lines [93, 94, 95, 96, 98, 99, 100, 102, 103, 104, 105, 107, 108, 109, 110, 111, 112, 114]
# branches ['98->99', '98->114', '107->108', '107->114']

import pytest
from thefuck.logs import how_to_configure_alias
from collections import namedtuple
from unittest.mock import patch
import colorama
import sys

# Define a namedtuple for configuration details
ConfigurationDetails = namedtuple('ConfigurationDetails', 'content path reload can_configure_automatically')

@pytest.fixture
def mock_print(mocker):
    return mocker.patch('builtins.print')

def test_how_to_configure_alias_with_configuration_details_and_can_configure_automatically(mock_print):
    # Create a ConfigurationDetails instance with can_configure_automatically set to True
    configuration_details = ConfigurationDetails(
        content='eval "$(thefuck --alias)"',
        path='.bashrc',
        reload='source ~/.bashrc',
        can_configure_automatically=True
    )

    # Call the function with the configuration details
    how_to_configure_alias(configuration_details)

    # Check that the output contains the expected strings
    expected_output = [
        "Seems like",
        "Please put",
        "eval \"$(thefuck --alias)\"",
        ".bashrc",
        "source ~/.bashrc",
        "Or run",
        "More details - https://github.com/nvbn/thefuck#manual-installation"
    ]
    for expected in expected_output:
        assert any(expected in call_args[0][0] for call_args in mock_print.call_args_list)

def test_how_to_configure_alias_without_configuration_details(mock_print):
    # Call the function without configuration details
    how_to_configure_alias(None)

    # Check that the output contains the expected strings
    expected_output = [
        "Seems like",
        "More details - https://github.com/nvbn/thefuck#manual-installation"
    ]
    for expected in expected_output:
        assert any(expected in call_args[0][0] for call_args in mock_print.call_args_list)

    # Check that the output does not contain configuration details
    unexpected_output = [
        "Please put",
        "Or run"
    ]
    for unexpected in unexpected_output:
        assert not any(unexpected in call_args[0][0] for call_args in mock_print.call_args_list)
