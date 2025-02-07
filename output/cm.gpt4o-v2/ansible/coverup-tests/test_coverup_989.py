# file: lib/ansible/modules/cron.py:223-224
# asked: {"lines": [223, 224], "branches": []}
# gained: {"lines": [223, 224], "branches": []}

import pytest

def test_crontaberror_exception():
    from ansible.modules.cron import CronTabError
    with pytest.raises(CronTabError):
        raise CronTabError("This is a test exception")
