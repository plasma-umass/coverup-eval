# file: lib/ansible/modules/cron.py:505-516
# asked: {"lines": [505, 509, 510, 511, 513, 514, 515, 516], "branches": [[510, 511], [510, 513], [514, 515], [514, 516]]}
# gained: {"lines": [505, 509, 510, 511, 513, 514, 515, 516], "branches": [[510, 511], [510, 513], [514, 515], [514, 516]]}

import pytest
from ansible.modules.cron import CronTab

@pytest.fixture
def mock_module(mocker):
    module = mocker.Mock()
    module.get_bin_path.return_value = '/usr/bin/crontab'
    module.run_command.return_value = (0, '', '')
    return module

@pytest.fixture
def crontab(mock_module):
    crontab = CronTab(module=mock_module)
    crontab.lines = []
    return crontab

def test_render_empty_crontab(crontab):
    crontab.lines = []
    assert crontab.render() == ''

def test_render_non_empty_crontab(crontab):
    crontab.lines = ['* * * * * /path/to/command']
    assert crontab.render() == '* * * * * /path/to/command\n'

def test_render_crontab_with_multiple_lines(crontab):
    crontab.lines = ['* * * * * /path/to/command', '0 0 * * * /path/to/another_command']
    assert crontab.render() == '* * * * * /path/to/command\n0 0 * * * /path/to/another_command\n'
