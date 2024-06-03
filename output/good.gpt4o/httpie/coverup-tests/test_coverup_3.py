# file httpie/client.py:197-212
# lines [197, 198, 199, 202, 203, 204, 205, 206, 208, 211, 212]
# branches ['203->204', '203->208', '205->206', '205->212', '208->211', '208->212']

import pytest
import argparse
from httpie.client import make_default_headers, RequestHeadersDict, DEFAULT_UA, JSON_ACCEPT, JSON_CONTENT_TYPE, FORM_CONTENT_TYPE

def test_make_default_headers_json():
    args = argparse.Namespace(data=True, form=False, json=True, files=False)
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE

def test_make_default_headers_auto_json():
    args = argparse.Namespace(data=True, form=False, json=False, files=False)
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE

def test_make_default_headers_form():
    args = argparse.Namespace(data=False, form=True, json=False, files=False)
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert headers['Content-Type'] == FORM_CONTENT_TYPE

def test_make_default_headers_files():
    args = argparse.Namespace(data=False, form=True, json=False, files=True)
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert 'Content-Type' not in headers

def test_make_default_headers_no_special_handling():
    args = argparse.Namespace(data=False, form=False, json=False, files=False)
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA
    assert 'Accept' not in headers
    assert 'Content-Type' not in headers
