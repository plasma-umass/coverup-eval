# file httpie/status.py:23-40
# lines [23, 30, 32, 33, 35, 36, 38, 40]
# branches ['30->32', '30->33', '33->35', '33->36', '36->38', '36->40']

import pytest
from httpie.status import http_status_to_exit_status, ExitStatus

@pytest.mark.parametrize("http_status, follow, expected_exit_status", [
    (301, False, ExitStatus.ERROR_HTTP_3XX),
    (400, False, ExitStatus.ERROR_HTTP_4XX),
    (500, False, ExitStatus.ERROR_HTTP_5XX),
    (200, False, ExitStatus.SUCCESS),
    (301, True, ExitStatus.SUCCESS),  # This case tests the 'follow' branch
])
def test_http_status_to_exit_status(http_status, follow, expected_exit_status):
    assert http_status_to_exit_status(http_status, follow) == expected_exit_status
