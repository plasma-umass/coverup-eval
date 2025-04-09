# file: lib/ansible/modules/cron.py:534-545
# asked: {"lines": [538, 539, 540, 541, 542, 543, 544, 545], "branches": [[539, 540], [539, 545], [540, 541], [540, 543], [543, 544], [543, 545]]}
# gained: {"lines": [538, 539, 540, 541, 542, 543, 544, 545], "branches": [[539, 540], [539, 545], [540, 541], [540, 543], [543, 544], [543, 545]]}

import pytest
import platform
import os
import pwd
import shlex

from ansible.modules.cron import CronTab

@pytest.fixture
def mock_getpwuid(mocker):
    mock = mocker.patch('pwd.getpwuid')
    mock.return_value = ['mockuser']
    return mock

@pytest.fixture
def mock_getuid(mocker):
    mock = mocker.patch('os.getuid')
    mock.return_value = 1000
    return mock

@pytest.fixture
def mock_platform_system(mocker):
    mock = mocker.patch('platform.system')
    return mock

@pytest.fixture
def mock_shlex_quote(mocker):
    mock = mocker.patch('shlex.quote', side_effect=lambda x: x)
    return mock

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock()
    module.run_command.return_value = (0, '', '')
    return module

def test_write_execute_no_user(mock_shlex_quote, mock_module):
    cron = CronTab(module=mock_module)
    cron.user = None
    cron.cron_cmd = 'crontab'
    result = cron._write_execute('/path/to/crontab')
    assert result == 'crontab  /path/to/crontab'

def test_write_execute_sunos_user(mock_platform_system, mock_shlex_quote, mock_module):
    mock_platform_system.return_value = 'SunOS'
    cron = CronTab(module=mock_module)
    cron.user = 'testuser'
    cron.cron_cmd = 'crontab'
    result = cron._write_execute('/path/to/crontab')
    assert result == "chown testuser /path/to/crontab ; su 'testuser' -c 'crontab /path/to/crontab'"

def test_write_execute_hpux_user(mock_platform_system, mock_shlex_quote, mock_module):
    mock_platform_system.return_value = 'HP-UX'
    cron = CronTab(module=mock_module)
    cron.user = 'testuser'
    cron.cron_cmd = 'crontab'
    result = cron._write_execute('/path/to/crontab')
    assert result == "chown testuser /path/to/crontab ; su 'testuser' -c 'crontab /path/to/crontab'"

def test_write_execute_aix_user(mock_platform_system, mock_shlex_quote, mock_module):
    mock_platform_system.return_value = 'AIX'
    cron = CronTab(module=mock_module)
    cron.user = 'testuser'
    cron.cron_cmd = 'crontab'
    result = cron._write_execute('/path/to/crontab')
    assert result == "chown testuser /path/to/crontab ; su 'testuser' -c 'crontab /path/to/crontab'"

def test_write_execute_different_user(mock_getpwuid, mock_getuid, mock_shlex_quote, mock_module):
    cron = CronTab(module=mock_module)
    cron.user = 'differentuser'
    cron.cron_cmd = 'crontab'
    result = cron._write_execute('/path/to/crontab')
    assert result == 'crontab -u differentuser /path/to/crontab'

def test_write_execute_same_user(mock_getpwuid, mock_getuid, mock_shlex_quote, mock_module):
    cron = CronTab(module=mock_module)
    cron.user = 'mockuser'
    cron.cron_cmd = 'crontab'
    result = cron._write_execute('/path/to/crontab')
    assert result == 'crontab  /path/to/crontab'
