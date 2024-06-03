# file httpie/client.py:33-131
# lines [33, 36, 38, 39, 40, 41, 42, 43, 44, 45, 47, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 62, 63, 64, 65, 67, 68, 69, 71, 73, 75, 77, 79, 80, 81, 82, 83, 84, 86, 87, 88, 89, 91, 92, 93, 94, 95, 96, 97, 98, 100, 101, 102, 103, 104, 108, 109, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 124, 125, 126, 127, 129, 131]
# branches ['40->41', '40->49', '62->63', '62->75', '65->67', '65->71', '71->73', '71->75', '75->77', '75->79', '81->82', '81->86', '86->87', '86->91', '93->94', '93->124', '95->96', '95->122', '113->114', '113->121', '114->115', '114->116', '116->117', '116->121', '118->119', '118->120', '124->exit', '124->125', '125->exit', '125->126']

import pytest
import argparse
from pathlib import Path
from unittest.mock import Mock, patch
import requests
from httpie.client import collect_messages

@pytest.fixture
def mock_get_httpie_session(mocker):
    return mocker.patch('httpie.client.get_httpie_session')

@pytest.fixture
def mock_make_request_kwargs(mocker):
    return mocker.patch('httpie.client.make_request_kwargs')

@pytest.fixture
def mock_make_send_kwargs(mocker):
    return mocker.patch('httpie.client.make_send_kwargs')

@pytest.fixture
def mock_make_send_kwargs_mergeable_from_env(mocker):
    return mocker.patch('httpie.client.make_send_kwargs_mergeable_from_env')

@pytest.fixture
def mock_build_requests_session(mocker):
    return mocker.patch('httpie.client.build_requests_session')

@pytest.fixture
def mock_dump_request(mocker):
    return mocker.patch('httpie.client.dump_request')

@pytest.fixture
def mock_ensure_path_as_is(mocker):
    return mocker.patch('httpie.client.ensure_path_as_is')

@pytest.fixture
def mock_compress_request(mocker):
    return mocker.patch('httpie.client.compress_request')

@pytest.fixture
def mock_get_expired_cookies(mocker):
    return mocker.patch('httpie.client.get_expired_cookies')

@pytest.fixture
def mock_max_headers(mocker):
    return mocker.patch('httpie.client.max_headers')

@pytest.fixture
def mock_requests_session(mocker):
    session = Mock()
    session.prepare_request.return_value = Mock()
    session.send.return_value = Mock()
    session.merge_environment_settings.return_value = {}
    return session

def test_collect_messages(
    mock_get_httpie_session,
    mock_make_request_kwargs,
    mock_make_send_kwargs,
    mock_make_send_kwargs_mergeable_from_env,
    mock_build_requests_session,
    mock_dump_request,
    mock_ensure_path_as_is,
    mock_compress_request,
    mock_get_expired_cookies,
    mock_max_headers,
    mock_requests_session,
    mocker
):
    args = argparse.Namespace(
        session='test_session',
        session_read_only=None,
        headers={'Host': 'example.com'},
        url='http://example.com',
        ssl_version=None,
        ciphers=None,
        auth_plugin=None,
        debug=True,
        path_as_is=True,
        compress=2,
        offline=False,
        max_headers=10,
        max_redirects=1,
        follow=True,
        all=False
    )
    config_dir = Path('/tmp')
    request_body_read_callback = None

    mock_get_httpie_session.return_value = Mock(headers={}, cookies={}, auth=None)
    mock_make_request_kwargs.return_value = {'headers': {}, 'auth': None}
    mock_make_send_kwargs.return_value = {}
    mock_make_send_kwargs_mergeable_from_env.return_value = {'verify': True}
    mock_build_requests_session.return_value = mock_requests_session

    with pytest.raises(requests.TooManyRedirects):
        messages = list(collect_messages(args, config_dir, request_body_read_callback))

    assert mock_get_httpie_session.called
    assert mock_make_request_kwargs.called
    assert mock_make_send_kwargs.called
    assert mock_make_send_kwargs_mergeable_from_env.called
    assert mock_build_requests_session.called
    assert mock_dump_request.called
    assert mock_ensure_path_as_is.called
    assert mock_compress_request.called
    assert mock_requests_session.prepare_request.called
    assert mock_requests_session.send.called
    assert mock_get_expired_cookies.called
    assert mock_max_headers.called
