# file: lib/ansible/modules/cron.py:293-300
# asked: {"lines": [293, 294, 295, 297, 298, 299, 300], "branches": [[294, 295], [294, 297], [297, 298], [297, 300], [298, 297], [298, 299]]}
# gained: {"lines": [293, 294, 295, 297, 298, 299, 300], "branches": [[294, 295], [294, 297], [297, 298], [297, 300], [298, 297], [298, 299]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.cron import CronTab

@pytest.fixture
def cron_tab():
    module = MagicMock()
    module.get_bin_path = MagicMock(return_value='/usr/bin/crontab')
    with patch.object(CronTab, 'read', return_value=None):
        return CronTab(module)

def test_is_empty_with_no_lines(cron_tab):
    cron_tab.lines = []
    assert cron_tab.is_empty() is True

def test_is_empty_with_only_empty_lines(cron_tab):
    cron_tab.lines = ["", "   ", "\t"]
    assert cron_tab.is_empty() is True

def test_is_empty_with_non_empty_line(cron_tab):
    cron_tab.lines = ["", "   ", "\t", "0 5 * * * /path/to/command"]
    assert cron_tab.is_empty() is False
