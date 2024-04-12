# file py_backwards/conf.py:12-14
# lines [12, 13, 14]
# branches ['13->exit', '13->14']

import pytest
from argparse import Namespace
from py_backwards import conf

# Assuming the 'settings' object is a singleton or similar pattern that needs to be reset after the test
original_debug_value = conf.settings.debug

@pytest.fixture
def reset_settings():
    # Fixture to reset settings after each test
    yield
    conf.settings.debug = original_debug_value

def test_init_settings_with_debug_enabled(reset_settings, mocker):
    # Mock the Namespace to simulate the presence of the 'debug' argument
    args = mocker.Mock(spec=Namespace)
    args.debug = True

    # Call the function with the mocked arguments
    conf.init_settings(args)

    # Assert that the settings.debug is now True
    assert conf.settings.debug is True

def test_init_settings_with_debug_disabled(reset_settings, mocker):
    # Mock the Namespace to simulate the absence of the 'debug' argument
    args = mocker.Mock(spec=Namespace)
    args.debug = False

    # Call the function with the mocked arguments
    conf.init_settings(args)

    # Assert that the settings.debug has not changed
    assert conf.settings.debug is original_debug_value
