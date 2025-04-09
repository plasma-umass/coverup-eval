# file: lib/ansible/modules/cron.py:223-224
# asked: {"lines": [223, 224], "branches": []}
# gained: {"lines": [223, 224], "branches": []}

import pytest

# Import the module where CronTabError is defined
from ansible.modules.cron import CronTabError

def test_crontab_error():
    with pytest.raises(CronTabError):
        raise CronTabError("This is a test error")
