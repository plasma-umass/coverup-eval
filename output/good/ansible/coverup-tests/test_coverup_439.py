# file lib/ansible/modules/cron.py:464-471
# lines [464, 465, 467, 468, 469, 471]
# branches ['467->468', '467->471', '468->467', '468->469']

import pytest
from ansible.modules.cron import CronTab
import re

# Mocking the CronTab class to test get_envnames method
class TestCronTab:
    @pytest.fixture
    def crontab(self, mocker):
        mocker.patch.object(CronTab, '__init__', lambda self: None)
        ct = CronTab()
        ct.lines = [
            'MAILTO=user@example.com',
            'PATH=/usr/bin:/bin',
            '* * * * * echo "Hello, World!"',
            'SHELL=/bin/bash',
            '# Comment line',
            'Not an env setting'
        ]
        return ct

    def test_get_envnames(self, crontab):
        envnames = crontab.get_envnames()
        assert 'MAILTO' in envnames
        assert 'PATH' in envnames
        assert 'SHELL' in envnames
        assert len(envnames) == 3  # Only the env settings should be included

        # Ensure that non-env lines are not included
        assert 'echo "Hello, World!"' not in envnames
        assert 'Not an env setting' not in envnames
        assert '# Comment line' not in envnames
