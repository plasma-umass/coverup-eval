# file: httpie/core.py:112-125
# asked: {"lines": [112, 116, 117, 118, 119, 121, 122, 123, 125], "branches": []}
# gained: {"lines": [112, 116, 117, 118, 119, 121, 122, 123, 125], "branches": []}

import pytest
import argparse
import requests
from httpie.cli.constants import OUT_REQ_BODY, OUT_REQ_HEAD, OUT_RESP_BODY, OUT_RESP_HEAD
from httpie.core import get_output_options

@pytest.fixture
def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--output-options', nargs='*', default=[])
    return parser.parse_args([])

def test_get_output_options_prepared_request(args, monkeypatch):
    monkeypatch.setattr(args, 'output_options', [OUT_REQ_HEAD, OUT_REQ_BODY])
    message = requests.PreparedRequest()
    head, body = get_output_options(args, message)
    assert head is True
    assert body is True

    monkeypatch.setattr(args, 'output_options', [OUT_REQ_HEAD])
    head, body = get_output_options(args, message)
    assert head is True
    assert body is False

    monkeypatch.setattr(args, 'output_options', [OUT_REQ_BODY])
    head, body = get_output_options(args, message)
    assert head is False
    assert body is True

    monkeypatch.setattr(args, 'output_options', [])
    head, body = get_output_options(args, message)
    assert head is False
    assert body is False

def test_get_output_options_response(args, monkeypatch):
    monkeypatch.setattr(args, 'output_options', [OUT_RESP_HEAD, OUT_RESP_BODY])
    message = requests.Response()
    head, body = get_output_options(args, message)
    assert head is True
    assert body is True

    monkeypatch.setattr(args, 'output_options', [OUT_RESP_HEAD])
    head, body = get_output_options(args, message)
    assert head is True
    assert body is False

    monkeypatch.setattr(args, 'output_options', [OUT_RESP_BODY])
    head, body = get_output_options(args, message)
    assert head is False
    assert body is True

    monkeypatch.setattr(args, 'output_options', [])
    head, body = get_output_options(args, message)
    assert head is False
    assert body is False
