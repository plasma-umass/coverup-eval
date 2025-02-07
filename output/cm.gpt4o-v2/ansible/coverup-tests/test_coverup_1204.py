# file: lib/ansible/modules/cron.py:428-433
# asked: {"lines": [429, 430, 431, 433], "branches": [[429, 430], [429, 433], [430, 429], [430, 431]]}
# gained: {"lines": [429, 430, 431, 433], "branches": [[429, 430], [429, 433], [430, 429], [430, 431]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.modules.cron import CronTab

@pytest.fixture
def cron_tab():
    module = MagicMock()
    with patch.object(CronTab, 'read', return_value=None):
        return CronTab(module)

def test_find_env_found(cron_tab):
    cron_tab.lines = ["FOO=bar", "BAZ=qux"]
    result = cron_tab.find_env("FOO")
    assert result == [0, "FOO=bar"]

def test_find_env_not_found(cron_tab):
    cron_tab.lines = ["FOO=bar", "BAZ=qux"]
    result = cron_tab.find_env("NOT_FOUND")
    assert result == []

def test_find_env_empty_lines(cron_tab):
    cron_tab.lines = []
    result = cron_tab.find_env("FOO")
    assert result == []
