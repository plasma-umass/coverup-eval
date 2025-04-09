# file httpie/client.py:197-212
# lines [198, 199, 202, 203, 204, 205, 206, 208, 211, 212]
# branches ['203->204', '203->208', '205->206', '205->212', '208->211', '208->212']

import argparse
import pytest
from httpie.client import make_default_headers

JSON_ACCEPT = 'application/json, */*;q=0.5'
JSON_CONTENT_TYPE = 'application/json'
FORM_CONTENT_TYPE = 'application/x-www-form-urlencoded; charset=utf-8'
DEFAULT_UA = 'HTTPie/2.4.0'

@pytest.fixture
def args_namespace():
    return argparse.Namespace(
        data=None,
        form=False,
        json=False,
        files=False
    )

def test_make_default_headers_with_json(args_namespace):
    args_namespace.json = True
    headers = make_default_headers(args_namespace)
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE
    assert headers['User-Agent'] == DEFAULT_UA

def test_make_default_headers_with_auto_json(args_namespace):
    args_namespace.data = '{"name": "value"}'
    headers = make_default_headers(args_namespace)
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE
    assert headers['User-Agent'] == DEFAULT_UA

def test_make_default_headers_with_form(args_namespace):
    args_namespace.form = True
    headers = make_default_headers(args_namespace)
    assert headers['Content-Type'] == FORM_CONTENT_TYPE
    assert headers['User-Agent'] == DEFAULT_UA
    assert 'Accept' not in headers

def test_make_default_headers_without_special_content_type(args_namespace):
    headers = make_default_headers(args_namespace)
    assert 'Content-Type' not in headers
    assert headers['User-Agent'] == DEFAULT_UA
    assert 'Accept' not in headers
