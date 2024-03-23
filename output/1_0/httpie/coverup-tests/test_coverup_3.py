# file httpie/status.py:4-20
# lines [4, 5, 6, 7, 8, 9, 12, 13, 14, 16, 17, 20]
# branches []

import pytest
from httpie.status import ExitStatus

def test_exit_status_enum():
    assert ExitStatus.SUCCESS == 0
    assert ExitStatus.ERROR == 1
    assert ExitStatus.ERROR_TIMEOUT == 2
    assert ExitStatus.ERROR_HTTP_3XX == 3
    assert ExitStatus.ERROR_HTTP_4XX == 4
    assert ExitStatus.ERROR_HTTP_5XX == 5
    assert ExitStatus.ERROR_TOO_MANY_REDIRECTS == 6
    assert ExitStatus.PLUGIN_ERROR == 7
    assert ExitStatus.ERROR_CTRL_C == 130

    # Ensure all members are unique
    assert len(ExitStatus) == len(set(ExitStatus))
