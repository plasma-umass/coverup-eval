# file semantic_release/helpers.py:16-39
# lines [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
# branches ['27->28', '27->29', '29->30', '29->39', '30->31', '30->32', '32->33', '32->34', '34->35', '34->36']

import pytest
from requests import Session
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from semantic_release.helpers import build_requests_session

def test_build_requests_session_with_raise_for_status_and_retry_defaults(mocker):
    session_mock = mocker.patch('semantic_release.helpers.Session')
    adapter_mock = mocker.patch('semantic_release.helpers.HTTPAdapter')

    session = build_requests_session()

    assert session_mock.called
    assert session_mock.return_value.hooks["response"]
    assert adapter_mock.called
    assert isinstance(adapter_mock.call_args[1]['max_retries'], Retry)

def test_build_requests_session_without_raise_for_status_and_retry_as_int(mocker):
    session_mock = mocker.patch('semantic_release.helpers.Session')
    adapter_mock = mocker.patch('semantic_release.helpers.HTTPAdapter')

    session = build_requests_session(raise_for_status=False, retry=5)

    assert session_mock.called
    assert "response" not in session_mock.return_value.hooks
    assert adapter_mock.called
    assert isinstance(adapter_mock.call_args[1]['max_retries'], Retry)
    assert adapter_mock.call_args[1]['max_retries'].total == 5

def test_build_requests_session_with_invalid_retry_type(mocker):
    session_mock = mocker.patch('semantic_release.helpers.Session')

    with pytest.raises(ValueError):
        build_requests_session(retry='invalid_type')
