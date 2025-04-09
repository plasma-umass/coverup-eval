# file: httpie/client.py:243-297
# asked: {"lines": [], "branches": [[256, 265]]}
# gained: {"lines": [], "branches": [[256, 265]]}

import pytest
import json
import argparse
from httpie.client import make_request_kwargs

def test_make_request_kwargs_json_data(monkeypatch):
    class MockArgs:
        method = 'GET'
        url = 'http://example.com'
        headers = {}
        data = {'key': 'value'}
        json = True
        form = False
        files = None
        offline = False
        chunked = False
        auth = None
        params = {}
        multipart = False
        multipart_data = None
        boundary = None

    args = MockArgs()
    base_headers = {}

    def mock_make_default_headers(args):
        return {'User-Agent': 'test-agent'}

    def mock_finalize_headers(headers):
        return headers

    def mock_get_multipart_data_and_content_type(data, boundary, content_type):
        return data, 'multipart/form-data'

    def mock_prepare_request_body(body, body_read_callback, chunked, offline, content_length_header_value):
        return body

    monkeypatch.setattr('httpie.client.make_default_headers', mock_make_default_headers)
    monkeypatch.setattr('httpie.client.finalize_headers', mock_finalize_headers)
    monkeypatch.setattr('httpie.client.get_multipart_data_and_content_type', mock_get_multipart_data_and_content_type)
    monkeypatch.setattr('httpie.client.prepare_request_body', mock_prepare_request_body)

    kwargs = make_request_kwargs(args, base_headers)

    assert kwargs['method'] == 'get'
    assert kwargs['url'] == 'http://example.com'
    assert kwargs['headers']['User-Agent'] == 'test-agent'
    assert kwargs['data'] == json.dumps({'key': 'value'})

def test_make_request_kwargs_empty_json_data(monkeypatch):
    class MockArgs:
        method = 'GET'
        url = 'http://example.com'
        headers = {}
        data = {}
        json = True
        form = False
        files = None
        offline = False
        chunked = False
        auth = None
        params = {}
        multipart = False
        multipart_data = None
        boundary = None

    args = MockArgs()
    base_headers = {}

    def mock_make_default_headers(args):
        return {'User-Agent': 'test-agent'}

    def mock_finalize_headers(headers):
        return headers

    def mock_get_multipart_data_and_content_type(data, boundary, content_type):
        return data, 'multipart/form-data'

    def mock_prepare_request_body(body, body_read_callback, chunked, offline, content_length_header_value):
        return body

    monkeypatch.setattr('httpie.client.make_default_headers', mock_make_default_headers)
    monkeypatch.setattr('httpie.client.finalize_headers', mock_finalize_headers)
    monkeypatch.setattr('httpie.client.get_multipart_data_and_content_type', mock_get_multipart_data_and_content_type)
    monkeypatch.setattr('httpie.client.prepare_request_body', mock_prepare_request_body)

    kwargs = make_request_kwargs(args, base_headers)

    assert kwargs['method'] == 'get'
    assert kwargs['url'] == 'http://example.com'
    assert kwargs['headers']['User-Agent'] == 'test-agent'
    assert kwargs['data'] == ''

def test_make_request_kwargs_with_base_headers(monkeypatch):
    class MockArgs:
        method = 'GET'
        url = 'http://example.com'
        headers = {'Custom-Header': 'value'}
        data = None
        json = False
        form = False
        files = None
        offline = False
        chunked = False
        auth = None
        params = {}
        multipart = False
        multipart_data = None
        boundary = None

    args = MockArgs()
    base_headers = {'Base-Header': 'base-value'}

    def mock_make_default_headers(args):
        return {'User-Agent': 'test-agent'}

    def mock_finalize_headers(headers):
        return headers

    def mock_get_multipart_data_and_content_type(data, boundary, content_type):
        return data, 'multipart/form-data'

    def mock_prepare_request_body(body, body_read_callback, chunked, offline, content_length_header_value):
        return body

    monkeypatch.setattr('httpie.client.make_default_headers', mock_make_default_headers)
    monkeypatch.setattr('httpie.client.finalize_headers', mock_finalize_headers)
    monkeypatch.setattr('httpie.client.get_multipart_data_and_content_type', mock_get_multipart_data_and_content_type)
    monkeypatch.setattr('httpie.client.prepare_request_body', mock_prepare_request_body)

    kwargs = make_request_kwargs(args, base_headers)

    assert kwargs['method'] == 'get'
    assert kwargs['url'] == 'http://example.com'
    assert kwargs['headers']['User-Agent'] == 'test-agent'
    assert kwargs['headers']['Base-Header'] == 'base-value'
    assert kwargs['headers']['Custom-Header'] == 'value'
