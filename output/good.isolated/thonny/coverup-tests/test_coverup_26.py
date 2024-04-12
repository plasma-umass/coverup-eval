# file thonny/jedi_utils.py:52-67
# lines [53, 55, 56, 57, 58, 59, 60, 62, 64, 65, 67]
# branches ['55->56', '55->64']

import pytest
from unittest.mock import Mock, patch

@pytest.fixture
def mock_jedi(mocker):
    jedi_mock = mocker.patch('jedi.Script')
    return jedi_mock

@pytest.fixture
def mock_logger(mocker):
    logger_mock = mocker.patch('thonny.jedi_utils.logger')
    return logger_mock

@pytest.fixture
def mock_tweak_completions(mocker):
    tweak_completions_mock = mocker.patch('thonny.jedi_utils._tweak_completions', return_value=[])
    return tweak_completions_mock

@pytest.fixture
def mock_using_older_jedi(mocker):
    using_older_jedi_mock = mocker.patch('thonny.jedi_utils._using_older_jedi', return_value=True)
    return using_older_jedi_mock

def test_get_script_completions_with_older_jedi_exception(mock_jedi, mock_logger, mock_tweak_completions, mock_using_older_jedi):
    from thonny.jedi_utils import get_script_completions

    source = "import os"
    row = 1
    column = 7
    filename = "test.py"
    sys_path = None

    # Configure the mock to raise an exception when Script is called with sys_path
    mock_jedi.side_effect = [Exception("Test Exception"), Mock()]

    completions = get_script_completions(source, row, column, filename, sys_path)

    # Verify that the logger was called due to the exception
    mock_logger.info.assert_called_once()

    # Verify that the completions were tweaked
    mock_tweak_completions.assert_called_once()

    # Verify that the completions are returned correctly
    assert completions == []

    # Cleanup
    mock_jedi.side_effect = None
