# file: httpie/client.py:243-297
# asked: {"lines": [243, 245, 246, 252, 254, 255, 256, 257, 258, 262, 265, 266, 267, 268, 269, 272, 273, 275, 276, 277, 278, 279, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 293, 294, 297], "branches": [[256, 257], [256, 265], [257, 258], [257, 262], [266, 267], [266, 268], [269, 272], [269, 273], [275, 276], [275, 282]]}
# gained: {"lines": [243, 245, 246, 252, 254, 255, 256, 257, 258, 262, 265, 266, 267, 268, 269, 272, 273, 275, 276, 277, 278, 279, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 293, 294, 297], "branches": [[256, 257], [257, 258], [257, 262], [266, 267], [266, 268], [269, 272], [269, 273], [275, 276], [275, 282]]}

import pytest
import argparse
import json
from httpie.client import make_request_kwargs

@pytest.fixture
def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--files', default=None)
    parser.add_argument('--data', default=None)
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--form', action='store_true')
    parser.add_argument('--headers', type=dict, default={})
    parser.add_argument('--offline', action='store_true')
    parser.add_argument('--chunked', action='store_true')
    parser.add_argument('--method', default='GET')
    parser.add_argument('--url', default='http://example.com')
    parser.add_argument('--auth', default=None)
    parser.add_argument('--params', type=dict, default={})
    parser.add_argument('--multipart', action='store_true')
    parser.add_argument('--multipart_data', default=None)
    parser.add_argument('--boundary', default=None)
    return parser.parse_args([])

def test_make_request_kwargs_json_data(args, monkeypatch):
    args.data = {'key': 'value'}
    args.json = True

    def mock_make_default_headers(args):
        return {'User-Agent': 'test-agent'}

    def mock_finalize_headers(headers):
        return headers

    monkeypatch.setattr('httpie.client.make_default_headers', mock_make_default_headers)
    monkeypatch.setattr('httpie.client.finalize_headers', mock_finalize_headers)

    kwargs = make_request_kwargs(args)
    assert kwargs['data'] == json.dumps({'key': 'value'})
    assert kwargs['headers']['User-Agent'] == 'test-agent'

def test_make_request_kwargs_empty_json_data(args, monkeypatch):
    args.data = {}
    args.json = True

    def mock_make_default_headers(args):
        return {'User-Agent': 'test-agent'}

    def mock_finalize_headers(headers):
        return headers

    monkeypatch.setattr('httpie.client.make_default_headers', mock_make_default_headers)
    monkeypatch.setattr('httpie.client.finalize_headers', mock_finalize_headers)

    kwargs = make_request_kwargs(args)
    assert kwargs['data'] == ''
    assert kwargs['headers']['User-Agent'] == 'test-agent'

def test_make_request_kwargs_base_headers(args, monkeypatch):
    args.data = {'key': 'value'}
    args.json = True
    base_headers = {'Base-Header': 'base-value'}

    def mock_make_default_headers(args):
        return {'User-Agent': 'test-agent'}

    def mock_finalize_headers(headers):
        return headers

    monkeypatch.setattr('httpie.client.make_default_headers', mock_make_default_headers)
    monkeypatch.setattr('httpie.client.finalize_headers', mock_finalize_headers)

    kwargs = make_request_kwargs(args, base_headers=base_headers)
    assert kwargs['headers']['Base-Header'] == 'base-value'
    assert kwargs['headers']['User-Agent'] == 'test-agent'

def test_make_request_kwargs_offline_chunked(args, monkeypatch):
    args.data = {'key': 'value'}
    args.json = True
    args.offline = True
    args.chunked = True

    def mock_make_default_headers(args):
        return {'User-Agent': 'test-agent'}

    def mock_finalize_headers(headers):
        return headers

    monkeypatch.setattr('httpie.client.make_default_headers', mock_make_default_headers)
    monkeypatch.setattr('httpie.client.finalize_headers', mock_finalize_headers)

    kwargs = make_request_kwargs(args)
    assert kwargs['headers']['Transfer-Encoding'] == 'chunked'
    assert kwargs['headers']['User-Agent'] == 'test-agent'

def test_make_request_kwargs_multipart(args, monkeypatch):
    args.data = {'key': 'value'}
    args.multipart = True
    args.multipart_data = {'file': ('filename', 'filecontent')}
    args.boundary = 'boundary'

    def mock_make_default_headers(args):
        return {'User-Agent': 'test-agent'}

    def mock_finalize_headers(headers):
        return headers

    def mock_get_multipart_data_and_content_type(data, boundary, content_type):
        return 'multipart-data', 'multipart/form-data; boundary=boundary'

    monkeypatch.setattr('httpie.client.make_default_headers', mock_make_default_headers)
    monkeypatch.setattr('httpie.client.finalize_headers', mock_finalize_headers)
    monkeypatch.setattr('httpie.client.get_multipart_data_and_content_type', mock_get_multipart_data_and_content_type)

    kwargs = make_request_kwargs(args)
    assert kwargs['data'] == 'multipart-data'
    assert kwargs['headers']['Content-Type'] == 'multipart/form-data; boundary=boundary'
    assert kwargs['headers']['User-Agent'] == 'test-agent'
