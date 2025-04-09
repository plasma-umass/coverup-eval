# file flutils/setuputils/cfg.py:32-41
# lines [32, 35, 36, 37, 38, 39, 40, 41]
# branches ['35->exit', '35->36', '38->35', '38->39', '40->35', '40->41']

import pytest
from configparser import ConfigParser
from typing import Tuple, Generator
from unittest.mock import MagicMock

# Assuming the module structure is as follows:
# flutils/
# ├── setuputils/
# │   └── cfg.py (contains the _each_setup_cfg_command_section function)
# └── tests/
#     └── test_cfg.py (we are adding our test here)

# Import the function from the actual module
from flutils.setuputils.cfg import _each_setup_cfg_command_section

# Test function to improve coverage
def test_each_setup_cfg_command_section():
    # Create a mock ConfigParser with some sections
    parser = ConfigParser()
    parser.add_section('setup.command.test_command')
    parser.add_section('setup.command.')
    parser.add_section('not_a_command_section')
    parser.add_section('setup.command.with.extra.dots')

    # Call the function and convert the result to a list for assertions
    result = list(_each_setup_cfg_command_section(parser))

    # Expected results
    expected = [
        ('setup.command.test_command', 'test_command'),
        ('setup.command.with.extra.dots', 'with.extra.dots')
    ]

    # Assert that the result matches the expected output
    assert result == expected

# If using pytest-mock, you can create a fixture to clean up after the test
@pytest.fixture(autouse=True)
def cleanup(mocker):
    # This fixture will run after each test function automatically
    # due to the 'autouse=True' parameter.
    yield  # This allows the test to run before the cleanup
    mocker.stopall()  # Stop all patches started with mocker
