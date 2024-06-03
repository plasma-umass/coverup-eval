# file httpie/client.py:243-297
# lines [252, 254, 255, 256, 257, 258, 262, 265, 266, 267, 268, 269, 272, 273, 275, 276, 277, 278, 279, 282, 283, 284, 285, 286, 287, 288, 289, 290, 291, 293, 294, 297]
# branches ['256->257', '256->265', '257->258', '257->262', '266->267', '266->268', '269->272', '269->273', '275->276', '275->282']

import pytest
import argparse
import json
from httpie.client import make_request_kwargs

@pytest.fixture
def mock_args(mocker):
    args = argparse.Namespace()
    args.files = None
    args.data = {"key": "value"}
    args.json = True
    args.form = False
    args.headers = {"Custom-Header": "value"}
    args.offline = False
    args.chunked = False
    args.method = "POST"
    args.url = "http://example.com"
    args.auth = None
    args.params = {"param1": "value1"}
    args.multipart = False
    args.multipart_data = None
    args.boundary = None
    return args

def test_make_request_kwargs_json_data(mock_args, mocker):
    mocker.patch('httpie.client.make_default_headers', return_value={})
    mocker.patch('httpie.client.finalize_headers', return_value={})
    mocker.patch('httpie.client.prepare_request_body', return_value='{"key": "value"}')

    kwargs = make_request_kwargs(mock_args)

    assert kwargs['method'] == 'post'
    assert kwargs['url'] == 'http://example.com'
    assert kwargs['headers'] == {}
    assert kwargs['data'] == '{"key": "value"}'
    assert kwargs['auth'] is None
    assert list(kwargs['params']) == [('param1', 'value1')]

def test_make_request_kwargs_empty_json_data(mock_args, mocker):
    mock_args.data = {}
    mocker.patch('httpie.client.make_default_headers', return_value={})
    mocker.patch('httpie.client.finalize_headers', return_value={})
    mocker.patch('httpie.client.prepare_request_body', return_value='')

    kwargs = make_request_kwargs(mock_args)

    assert kwargs['method'] == 'post'
    assert kwargs['url'] == 'http://example.com'
    assert kwargs['headers'] == {}
    assert kwargs['data'] == ''
    assert kwargs['auth'] is None
    assert list(kwargs['params']) == [('param1', 'value1')]

def test_make_request_kwargs_multipart(mock_args, mocker):
    mock_args.multipart = True
    mock_args.multipart_data = {"file": "content"}
    mocker.patch('httpie.client.make_default_headers', return_value={})
    mocker.patch('httpie.client.finalize_headers', return_value={})
    mocker.patch('httpie.client.get_multipart_data_and_content_type', return_value=('multipart_data', 'multipart/form-data'))
    mocker.patch('httpie.client.prepare_request_body', return_value='multipart_data')

    kwargs = make_request_kwargs(mock_args)

    assert kwargs['method'] == 'post'
    assert kwargs['url'] == 'http://example.com'
    assert kwargs['headers'] == {'Content-Type': 'multipart/form-data'}
    assert kwargs['data'] == 'multipart_data'
    assert kwargs['auth'] is None
    assert list(kwargs['params']) == [('param1', 'value1')]
