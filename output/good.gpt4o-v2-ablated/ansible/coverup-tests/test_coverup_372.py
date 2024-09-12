# file: lib/ansible/modules/cron.py:223-224
# asked: {"lines": [223, 224], "branches": []}
# gained: {"lines": [223, 224], "branches": []}

import pytest

# Import the CronTabError class
from ansible.modules.cron import CronTabError

def test_crontab_error():
    with pytest.raises(CronTabError):
        raise CronTabError("This is a test error")

    try:
        raise CronTabError("This is another test error")
    except CronTabError as e:
        assert str(e) == "This is another test error"
