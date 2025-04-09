# file lib/ansible/modules/cron.py:302-333
# lines [307, 320, 329]
# branches ['306->307', '319->320', '328->329']

import os
import pytest
from ansible.modules.cron import CronTab

@pytest.fixture
def cron_tab(mocker):
    module_mock = mocker.MagicMock()
    module_mock.selinux_enabled.return_value = False
    module_mock.fail_json.side_effect = Exception('error occurred')
    module_mock.run_command.return_value = (0, '', '')  # Mock run_command to return a tuple
    cron_tab = CronTab(module=module_mock)
    cron_tab.cron_file = None
    cron_tab.render = mocker.MagicMock(return_value='* * * * * echo "hello world"')
    return cron_tab

def test_crontab_write_backup(mocker, cron_tab):
    mocker.patch('os.fdopen')
    mocker.patch('tempfile.mkstemp', return_value=(None, '/tmp/crontmp'))
    mocker.patch('os.chmod')
    mocker.patch('os.unlink')

    backup_file = '/tmp/cron_backup'
    cron_tab.write(backup_file=backup_file)

    assert os.fdopen.call_count == 0
    assert os.unlink.call_count == 0
    assert cron_tab.module.run_command.call_count == 1  # run_command is called once for reading the crontab

    # Cleanup
    if os.path.exists(backup_file):
        os.remove(backup_file)

def test_crontab_write_no_backup_failure(mocker, cron_tab):
    mocker.patch('os.fdopen')
    mocker.patch('tempfile.mkstemp', return_value=(None, '/tmp/crontmp'))
    mocker.patch('os.chmod')
    mocker.patch('os.unlink')
    mocker.patch('ansible.modules.cron.CronTab._write_execute', return_value='crontab /tmp/crontmp')
    cron_tab.module.run_command.return_value = (1, '', 'error occurred')

    with pytest.raises(Exception) as excinfo:
        cron_tab.write(backup_file=None)
    assert 'error occurred' in str(excinfo.value)

    assert os.fdopen.call_count == 1
    assert os.unlink.call_count == 1
    assert cron_tab.module.run_command.call_count == 2  # One for read, one for write

    # Cleanup
    tmp_file = '/tmp/crontmp'
    if os.path.exists(tmp_file):
        os.remove(tmp_file)
