# file: httpie/client.py:223-240
# asked: {"lines": [223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 240], "branches": [[225, 226], [225, 229], [227, 228], [227, 229]]}
# gained: {"lines": [223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 240], "branches": [[225, 226], [225, 229], [227, 228], [227, 229]]}

import argparse
import pytest

from httpie.client import make_send_kwargs_mergeable_from_env

def test_make_send_kwargs_mergeable_from_env_no_cert():
    args = argparse.Namespace(
        cert=None,
        cert_key=None,
        proxy=[],
        verify='yes'
    )
    expected = {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': None,
    }
    result = make_send_kwargs_mergeable_from_env(args)
    assert result == expected

def test_make_send_kwargs_mergeable_from_env_with_cert():
    args = argparse.Namespace(
        cert='path/to/cert',
        cert_key=None,
        proxy=[],
        verify='true'
    )
    expected = {
        'proxies': {},
        'stream': True,
        'verify': True,
        'cert': 'path/to/cert',
    }
    result = make_send_kwargs_mergeable_from_env(args)
    assert result == expected

def test_make_send_kwargs_mergeable_from_env_with_cert_and_key():
    args = argparse.Namespace(
        cert='path/to/cert',
        cert_key='path/to/key',
        proxy=[],
        verify='no'
    )
    expected = {
        'proxies': {},
        'stream': True,
        'verify': False,
        'cert': ('path/to/cert', 'path/to/key'),
    }
    result = make_send_kwargs_mergeable_from_env(args)
    assert result == expected

def test_make_send_kwargs_mergeable_from_env_with_proxy():
    args = argparse.Namespace(
        cert=None,
        cert_key=None,
        proxy=[argparse.Namespace(key='http', value='http://proxy')],
        verify='false'
    )
    expected = {
        'proxies': {'http': 'http://proxy'},
        'stream': True,
        'verify': False,
        'cert': None,
    }
    result = make_send_kwargs_mergeable_from_env(args)
    assert result == expected

def test_make_send_kwargs_mergeable_from_env_with_unknown_verify():
    args = argparse.Namespace(
        cert=None,
        cert_key=None,
        proxy=[],
        verify='custom'
    )
    expected = {
        'proxies': {},
        'stream': True,
        'verify': 'custom',
        'cert': None,
    }
    result = make_send_kwargs_mergeable_from_env(args)
    assert result == expected
