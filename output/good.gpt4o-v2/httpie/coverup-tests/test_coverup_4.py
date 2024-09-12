# file: httpie/client.py:223-240
# asked: {"lines": [223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 240], "branches": [[225, 226], [225, 229], [227, 228], [227, 229]]}
# gained: {"lines": [223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 240], "branches": [[225, 226], [225, 229], [227, 228], [227, 229]]}

import pytest
import argparse
from httpie.client import make_send_kwargs_mergeable_from_env

def test_make_send_kwargs_mergeable_from_env_no_cert():
    args = argparse.Namespace(cert=None, cert_key=None, proxy=[], verify='yes')
    result = make_send_kwargs_mergeable_from_env(args)
    assert result['cert'] is None
    assert result['verify'] is True

def test_make_send_kwargs_mergeable_from_env_cert_only():
    args = argparse.Namespace(cert='path/to/cert', cert_key=None, proxy=[], verify='no')
    result = make_send_kwargs_mergeable_from_env(args)
    assert result['cert'] == 'path/to/cert'
    assert result['verify'] is False

def test_make_send_kwargs_mergeable_from_env_cert_and_key():
    args = argparse.Namespace(cert='path/to/cert', cert_key='path/to/key', proxy=[], verify='true')
    result = make_send_kwargs_mergeable_from_env(args)
    assert result['cert'] == ('path/to/cert', 'path/to/key')
    assert result['verify'] is True

def test_make_send_kwargs_mergeable_from_env_proxies():
    proxy = argparse.Namespace(key='http', value='http://proxy.example.com')
    args = argparse.Namespace(cert=None, cert_key=None, proxy=[proxy], verify='false')
    result = make_send_kwargs_mergeable_from_env(args)
    assert result['proxies'] == {'http': 'http://proxy.example.com'}
    assert result['verify'] is False

def test_make_send_kwargs_mergeable_from_env_verify_default():
    args = argparse.Namespace(cert=None, cert_key=None, proxy=[], verify='custom')
    result = make_send_kwargs_mergeable_from_env(args)
    assert result['verify'] == 'custom'
