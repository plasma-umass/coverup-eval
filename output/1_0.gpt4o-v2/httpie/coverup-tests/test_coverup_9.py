# file: httpie/status.py:23-40
# asked: {"lines": [23, 30, 32, 33, 35, 36, 38, 40], "branches": [[30, 32], [30, 33], [33, 35], [33, 36], [36, 38], [36, 40]]}
# gained: {"lines": [23, 30, 32, 33, 35, 36, 38, 40], "branches": [[30, 32], [30, 33], [33, 35], [33, 36], [36, 38], [36, 40]]}

import pytest
from httpie.status import http_status_to_exit_status, ExitStatus

def test_http_status_to_exit_status_redirect():
    assert http_status_to_exit_status(301) == ExitStatus.ERROR_HTTP_3XX
    assert http_status_to_exit_status(301, follow=True) == ExitStatus.SUCCESS

def test_http_status_to_exit_status_client_error():
    assert http_status_to_exit_status(404) == ExitStatus.ERROR_HTTP_4XX

def test_http_status_to_exit_status_server_error():
    assert http_status_to_exit_status(500) == ExitStatus.ERROR_HTTP_5XX

def test_http_status_to_exit_status_success():
    assert http_status_to_exit_status(200) == ExitStatus.SUCCESS
