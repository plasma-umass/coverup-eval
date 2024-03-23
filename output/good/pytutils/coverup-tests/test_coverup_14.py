# file pytutils/log.py:81-97
# lines [81, 89, 91, 92, 93, 94, 95, 96, 97]
# branches []

import logging
import pytest
from unittest.mock import patch
from pytutils.log import configure, DEFAULT_CONFIG

def test_configure_with_basic_config(mocker):
    # Mock the dictConfig to raise a TypeError
    mocker.patch('logging.config.dictConfig', side_effect=TypeError)
    # Mock the basicConfig to ensure it is called and works as expected
    basic_config_mock = mocker.patch('logging.basicConfig')

    # Call configure with a basic config that should trigger the fallback
    configure(config={'invalid': 'config'})

    # Assert that basicConfig was called as a result of the TypeError
    basic_config_mock.assert_called_once_with(invalid='config')

    # Cleanup: no cleanup needed as we are using mocks

def test_configure_with_basic_config_raising_exception(mocker):
    # Mock the dictConfig to raise a TypeError
    mocker.patch('logging.config.dictConfig', side_effect=TypeError)
    # Mock the basicConfig to raise an Exception
    mocker.patch('logging.basicConfig', side_effect=Exception)

    # Call configure and expect an Exception due to the basicConfig failure
    with pytest.raises(Exception):
        configure(config={'invalid': 'config'})

    # Cleanup: no cleanup needed as we are using mocks
