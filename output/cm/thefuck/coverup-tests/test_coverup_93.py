# file thefuck/entrypoints/not_configured.py:91-114
# lines [91, 98, 99, 100, 101, 102, 104, 105, 106, 107, 108, 109, 110, 112, 114]
# branches ['100->104', '100->114', '104->105', '104->107', '107->108', '107->112']

import pytest
from unittest.mock import Mock, patch

@pytest.fixture
def mock_settings(mocker):
    mocker.patch('thefuck.settings.init')

@pytest.fixture
def mock_shell(mocker):
    mock_configuration_details = Mock()
    mock_configuration_details.can_configure_automatically = True
    mocker.patch('thefuck.shell.how_to_configure', return_value=mock_configuration_details)
    return mock_configuration_details

@pytest.fixture
def mock_logs(mocker):
    mocker.patch('thefuck.logs.already_configured')
    mocker.patch('thefuck.logs.configured_successfully')
    mocker.patch('thefuck.logs.how_to_configure_alias')

@pytest.fixture
def mock_configure(mocker):
    mocker.patch('thefuck.entrypoints.not_configured._configure')

@pytest.fixture
def mock_record_first_run(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured._record_first_run')

@pytest.fixture
def mock_is_already_configured(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured._is_already_configured')

@pytest.fixture
def mock_is_second_run(mocker):
    return mocker.patch('thefuck.entrypoints.not_configured._is_second_run')

@patch('thefuck.entrypoints.not_configured.settings')
@patch('thefuck.entrypoints.not_configured.shell')
@patch('thefuck.entrypoints.not_configured.logs')
def test_main_already_configured(mock_logs, mock_shell, mock_settings, mock_is_already_configured, mock_is_second_run):
    mock_is_already_configured.return_value = True
    mock_is_second_run.return_value = False
    from thefuck.entrypoints.not_configured import main
    main()
    mock_logs.already_configured.assert_called_once()

@patch('thefuck.entrypoints.not_configured.settings')
@patch('thefuck.entrypoints.not_configured.shell')
@patch('thefuck.entrypoints.not_configured.logs')
def test_main_configure_successfully(mock_logs, mock_shell, mock_settings, mock_configure, mock_is_already_configured, mock_is_second_run):
    mock_is_already_configured.return_value = False
    mock_is_second_run.return_value = True
    from thefuck.entrypoints.not_configured import main
    main()
    mock_logs.configured_successfully.assert_called_once()

@patch('thefuck.entrypoints.not_configured.settings')
@patch('thefuck.entrypoints.not_configured.shell')
@patch('thefuck.entrypoints.not_configured.logs')
@patch('thefuck.entrypoints.not_configured._record_first_run')
def test_main_record_first_run(mock_record_first_run, mock_logs, mock_shell, mock_settings, mock_is_already_configured, mock_is_second_run):
    mock_is_already_configured.return_value = False
    mock_is_second_run.return_value = False
    from thefuck.entrypoints.not_configured import main
    main()
    mock_record_first_run.assert_called_once()
    mock_logs.how_to_configure_alias.assert_called_once()
