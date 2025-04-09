# file thefuck/entrypoints/not_configured.py:91-114
# lines []
# branches ['100->114']

import pytest
from thefuck.entrypoints.not_configured import main
from thefuck import logs
from unittest.mock import Mock

@pytest.fixture
def mock_settings(mocker):
    settings_mock = mocker.patch('thefuck.entrypoints.not_configured.settings')
    settings_mock.init = Mock()
    return settings_mock

@pytest.fixture
def mock_shell(mocker):
    shell_mock = mocker.patch('thefuck.entrypoints.not_configured.shell')
    shell_mock.how_to_configure = Mock(return_value=Mock(
        can_configure_automatically=False))
    return shell_mock

@pytest.fixture
def mock_logs(mocker):
    logs_mock = mocker.patch('thefuck.entrypoints.not_configured.logs')
    return logs_mock

@pytest.fixture
def mock_is_already_configured(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured._is_already_configured')

@pytest.fixture
def mock_is_second_run(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured._is_second_run')

@pytest.fixture
def mock_configure(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured._configure')

@pytest.fixture
def mock_record_first_run(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured._record_first_run')

def test_main_with_cannot_configure_automatically(
        mock_settings, mock_shell, mock_logs, mock_is_already_configured,
        mock_is_second_run, mock_configure, mock_record_first_run):
    main()
    mock_logs.how_to_configure_alias.assert_called_once()
    mock_is_already_configured.assert_not_called()
    mock_is_second_run.assert_not_called()
    mock_configure.assert_not_called()
    mock_record_first_run.assert_not_called()
