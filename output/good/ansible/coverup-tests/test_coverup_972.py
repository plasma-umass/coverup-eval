# file lib/ansible/modules/cron.py:223-224
# lines [223, 224]
# branches []

import pytest
from ansible.modules.cron import CronTabError

def test_crontab_error():
    with pytest.raises(CronTabError) as exc_info:
        raise CronTabError("Test error message")
    assert str(exc_info.value) == "Test error message"
