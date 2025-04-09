# file: httpie/client.py:197-212
# asked: {"lines": [198, 199, 202, 203, 204, 205, 206, 208, 211, 212], "branches": [[203, 204], [203, 208], [205, 206], [205, 212], [208, 211], [208, 212]]}
# gained: {"lines": [198, 199, 202, 203, 204, 205, 206, 208, 211, 212], "branches": [[203, 204], [203, 208], [205, 206], [208, 211], [208, 212]]}

import pytest
import argparse
from httpie.client import make_default_headers
from httpie.cli.dicts import RequestHeadersDict

DEFAULT_UA = 'test-user-agent'
JSON_ACCEPT = 'application/json'
JSON_CONTENT_TYPE = 'application/json'
FORM_CONTENT_TYPE = 'application/x-www-form-urlencoded'

@pytest.fixture
def args():
    return argparse.Namespace(data=None, form=None, json=None, files=None)

def test_default_headers_user_agent(args, monkeypatch):
    monkeypatch.setattr('httpie.client.DEFAULT_UA', DEFAULT_UA)
    headers = make_default_headers(args)
    assert headers['User-Agent'] == DEFAULT_UA

def test_default_headers_json(args, monkeypatch):
    monkeypatch.setattr('httpie.client.DEFAULT_UA', DEFAULT_UA)
    monkeypatch.setattr('httpie.client.JSON_ACCEPT', JSON_ACCEPT)
    monkeypatch.setattr('httpie.client.JSON_CONTENT_TYPE', JSON_CONTENT_TYPE)
    args.json = True
    headers = make_default_headers(args)
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE

def test_default_headers_auto_json(args, monkeypatch):
    monkeypatch.setattr('httpie.client.DEFAULT_UA', DEFAULT_UA)
    monkeypatch.setattr('httpie.client.JSON_ACCEPT', JSON_ACCEPT)
    monkeypatch.setattr('httpie.client.JSON_CONTENT_TYPE', JSON_CONTENT_TYPE)
    args.data = True
    headers = make_default_headers(args)
    assert headers['Accept'] == JSON_ACCEPT
    assert headers['Content-Type'] == JSON_CONTENT_TYPE

def test_default_headers_form(args, monkeypatch):
    monkeypatch.setattr('httpie.client.DEFAULT_UA', DEFAULT_UA)
    monkeypatch.setattr('httpie.client.FORM_CONTENT_TYPE', FORM_CONTENT_TYPE)
    args.form = True
    headers = make_default_headers(args)
    assert headers['Content-Type'] == FORM_CONTENT_TYPE

def test_default_headers_files(args, monkeypatch):
    monkeypatch.setattr('httpie.client.DEFAULT_UA', DEFAULT_UA)
    args.form = True
    args.files = True
    headers = make_default_headers(args)
    assert 'Content-Type' not in headers
