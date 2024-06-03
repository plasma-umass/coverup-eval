# file lib/ansible/modules/cron.py:302-333
# lines [306, 307, 308, 309, 311, 312, 313, 315, 316, 319, 320, 323, 325, 326, 328, 329, 332, 333]
# branches ['306->307', '306->308', '308->309', '308->311', '319->320', '319->323', '323->325', '323->332', '328->329', '328->332', '332->exit', '332->333']

import pytest
import os
import tempfile
from unittest import mock
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_module():
    module = mock.Mock()
    module.run_command.return_value = (0, '', '')
    module.selinux_enabled.return_value = True
    return module

@pytest.fixture
def cron_tab(mock_module):
    cron_tab = CronTab(module=mock_module)
    cron_tab.cron_file = None
    cron_tab.b_cron_file = '/tmp/test_cron_file'
    return cron_tab

def test_write_with_backup_file(cron_tab):
    backup_file = '/tmp/backup_cron_file'
    with mock.patch('builtins.open', mock.mock_open()) as mock_file:
        cron_tab.write(backup_file=backup_file)
        mock_file.assert_called_once_with(backup_file, 'wb')
        mock_file().write.assert_called_once_with(cron_tab.render().encode())
        mock_file().close.assert_called_once()

def test_write_without_cron_file(cron_tab):
    cron_tab.cron_file = None
    with mock.patch('tempfile.mkstemp', return_value=(1, '/tmp/temp_cron_file')) as mock_mkstemp, \
         mock.patch('os.chmod') as mock_chmod, \
         mock.patch('os.fdopen', mock.mock_open()) as mock_fdopen, \
         mock.patch('os.unlink') as mock_unlink:
        cron_tab.write()
        mock_mkstemp.assert_called_once_with(prefix='crontab')
        mock_chmod.assert_called_once_with('/tmp/temp_cron_file', int('0644', 8))
        mock_fdopen().write.assert_called_once_with(cron_tab.render().encode())
        mock_fdopen().close.assert_called_once()
        cron_tab.module.run_command.assert_any_call(cron_tab._write_execute('/tmp/temp_cron_file'), use_unsafe_shell=True)
        mock_unlink.assert_called_once_with('/tmp/temp_cron_file')

def test_write_with_selinux(cron_tab):
    cron_tab.cron_file = '/tmp/test_cron_file'
    with mock.patch('builtins.open', mock.mock_open()) as mock_file:
        cron_tab.write()
        mock_file.assert_called_once_with(cron_tab.b_cron_file, 'wb')
        mock_file().write.assert_called_once_with(cron_tab.render().encode())
        mock_file().close.assert_called_once()
        cron_tab.module.set_default_selinux_context.assert_called_once_with(cron_tab.cron_file, False)
