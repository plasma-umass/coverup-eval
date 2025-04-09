# file lib/ansible/modules/cron.py:223-224
# lines [223, 224]
# branches []

import pytest
from ansible.modules.cron import CronTabError

def test_crontab_error():
    with pytest.raises(CronTabError):
        raise CronTabError("This is a test error")

