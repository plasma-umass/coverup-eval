# file thefuck/entrypoints/not_configured.py:91-114
# lines [98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 114]
# branches ['100->104', '100->114', '104->105', '104->107', '107->108', '107->112']

import pytest
from unittest import mock
from thefuck.entrypoints.not_configured import main, _is_already_configured, _is_second_run, _configure, _record_first_run
from thefuck import logs
from thefuck.conf import settings
from thefuck.shells import shell

@pytest.fixture
def mock_settings(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured.settings')

@pytest.fixture
def mock_logs(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured.logs')

@pytest.fixture
def mock_shell(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured.shell')

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

def test_main_first_run(mock_settings, mock_logs, mock_shell, mock_is_already_configured, mock_is_second_run, mock_configure, mock_record_first_run):
    mock_shell.how_to_configure.return_value = mock.Mock(can_configure_automatically=True)
    mock_is_already_configured.return_value = False
    mock_is_second_run.return_value = False

    main()

    mock_settings.init.assert_called_once()
    mock_shell.how_to_configure.assert_called_once()
    mock_is_already_configured.assert_called_once()
    mock_is_second_run.assert_called_once()
    mock_record_first_run.assert_called_once()
    mock_logs.how_to_configure_alias.assert_called_once()

def test_main_second_run(mock_settings, mock_logs, mock_shell, mock_is_already_configured, mock_is_second_run, mock_configure, mock_record_first_run):
    mock_shell.how_to_configure.return_value = mock.Mock(can_configure_automatically=True)
    mock_is_already_configured.return_value = False
    mock_is_second_run.return_value = True

    main()

    mock_settings.init.assert_called_once()
    mock_shell.how_to_configure.assert_called_once()
    mock_is_already_configured.assert_called_once()
    mock_is_second_run.assert_called_once()
    mock_configure.assert_called_once()
    mock_logs.configured_successfully.assert_called_once()

def test_main_already_configured(mock_settings, mock_logs, mock_shell, mock_is_already_configured, mock_is_second_run, mock_configure, mock_record_first_run):
    mock_shell.how_to_configure.return_value = mock.Mock(can_configure_automatically=True)
    mock_is_already_configured.return_value = True

    main()

    mock_settings.init.assert_called_once()
    mock_shell.how_to_configure.assert_called_once()
    mock_is_already_configured.assert_called_once()
    mock_logs.already_configured.assert_called_once()
    mock_is_second_run.assert_not_called()
    mock_configure.assert_not_called()
    mock_record_first_run.assert_not_called()
    mock_logs.how_to_configure_alias.assert_not_called()
