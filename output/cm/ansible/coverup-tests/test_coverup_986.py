# file lib/ansible/modules/cron.py:353-354
# lines [353, 354]
# branches []

import pytest
from ansible.modules.cron import CronTab

# Mock class to simulate the behavior of the actual system's crontab
class MockCronTab(CronTab):
    def __init__(self):
        self.jobs = {}
        self.removed = False

    def do_remove_job(self, name):
        self.removed = name in self.jobs
        if self.removed:
            del self.jobs[name]
        return self.removed

    def _update_job(self, name, job, method):
        return method(name)

# Test function to improve coverage for remove_job method
def test_remove_job(mocker):
    # Setup
    mock_crontab = MockCronTab()
    job_name = "test_job"
    mock_crontab.jobs[job_name] = "0 5 * * * /path/to/command"

    # Exercise
    result = mock_crontab.remove_job(job_name)

    # Verify
    assert result is True
    assert job_name not in mock_crontab.jobs
    assert mock_crontab.removed is True

    # Cleanup - nothing to do since we are using a mock object
