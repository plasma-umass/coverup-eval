# file: lib/ansible/modules/cron.py:435-453
# asked: {"lines": [435, 437, 439, 440, 442, 444, 445, 446, 448, 450, 451, 453], "branches": [[439, 440], [439, 442], [444, 445], [444, 450], [445, 446], [445, 448], [450, 451], [450, 453]]}
# gained: {"lines": [435, 437, 439, 440, 442, 444, 445, 446, 448, 450, 451, 453], "branches": [[439, 440], [439, 442], [444, 445], [444, 450], [445, 446], [445, 448], [450, 451], [450, 453]]}

import pytest
from ansible.modules.cron import CronTab

@pytest.fixture
def cron_tab(mocker):
    module = mocker.Mock()
    module.run_command = mocker.Mock(return_value=(0, "", ""))
    cron_tab = CronTab(module, user="testuser", cron_file="/etc/cron.d/testcron")
    return cron_tab

def test_get_cron_job_disabled(cron_tab):
    result = cron_tab.get_cron_job("0", "1", "2", "3", "4", "echo 'Hello'", None, True)
    assert result == "#0 1 2 3 4 testuser echo 'Hello'"

def test_get_cron_job_special_with_cron_file(cron_tab):
    result = cron_tab.get_cron_job("*", "*", "*", "*", "*", "echo 'Hello'", "reboot", False)
    assert result == "@reboot testuser echo 'Hello'"

def test_get_cron_job_special_without_cron_file(mocker):
    module = mocker.Mock()
    module.run_command = mocker.Mock(return_value=(0, "", ""))
    cron_tab = CronTab(module, user="testuser", cron_file=None)
    result = cron_tab.get_cron_job("*", "*", "*", "*", "*", "echo 'Hello'", "reboot", False)
    assert result == "@reboot echo 'Hello'"

def test_get_cron_job_with_cron_file(cron_tab):
    result = cron_tab.get_cron_job("0", "1", "2", "3", "4", "echo 'Hello'", None, False)
    assert result == "0 1 2 3 4 testuser echo 'Hello'"

def test_get_cron_job_without_cron_file(mocker):
    module = mocker.Mock()
    module.run_command = mocker.Mock(return_value=(0, "", ""))
    cron_tab = CronTab(module, user="testuser", cron_file=None)
    result = cron_tab.get_cron_job("0", "1", "2", "3", "4", "echo 'Hello'", None, False)
    assert result == "0 1 2 3 4 echo 'Hello'"
