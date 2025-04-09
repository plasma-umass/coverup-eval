# file: httpie/client.py:197-212
# asked: {"lines": [197, 198, 199, 202, 203, 204, 205, 206, 208, 211, 212], "branches": [[203, 204], [203, 208], [205, 206], [205, 212], [208, 211], [208, 212]]}
# gained: {"lines": [197, 198, 199, 202, 203, 204, 205, 206, 208, 211, 212], "branches": [[203, 204], [203, 208], [205, 206], [208, 211], [208, 212]]}

import pytest
import argparse
from httpie.client import make_default_headers, RequestHeadersDict, DEFAULT_UA, JSON_ACCEPT, JSON_CONTENT_TYPE, FORM_CONTENT_TYPE

def test_make_default_headers_no_args():
    args = argparse.Namespace(data=None, form=False, json=False, files=None)
    headers = make_default_headers(args)
    assert headers == {'User-Agent': DEFAULT_UA}

def test_make_default_headers_json():
    args = argparse.Namespace(data=None, form=False, json=True, files=None)
    headers = make_default_headers(args)
    assert headers == {'User-Agent': DEFAULT_UA, 'Accept': JSON_ACCEPT, 'Content-Type': JSON_CONTENT_TYPE}

def test_make_default_headers_auto_json():
    args = argparse.Namespace(data='some_data', form=False, json=False, files=None)
    headers = make_default_headers(args)
    assert headers == {'User-Agent': DEFAULT_UA, 'Accept': JSON_ACCEPT, 'Content-Type': JSON_CONTENT_TYPE}

def test_make_default_headers_form():
    args = argparse.Namespace(data=None, form=True, json=False, files=None)
    headers = make_default_headers(args)
    assert headers == {'User-Agent': DEFAULT_UA, 'Content-Type': FORM_CONTENT_TYPE}

def test_make_default_headers_form_with_files():
    args = argparse.Namespace(data=None, form=True, json=False, files={'file': 'content'})
    headers = make_default_headers(args)
    assert headers == {'User-Agent': DEFAULT_UA}
