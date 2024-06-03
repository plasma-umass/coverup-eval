# file httpie/client.py:223-240
# lines []
# branches ['225->229', '227->229']

import argparse
import pytest
from httpie.client import make_send_kwargs_mergeable_from_env

def test_make_send_kwargs_mergeable_from_env_with_cert_and_cert_key():
    args = argparse.Namespace(
        cert='path/to/cert',
        cert_key='path/to/cert_key',
        proxy=[],
        verify='yes'
    )
    result = make_send_kwargs_mergeable_from_env(args)
    assert result['cert'] == ('path/to/cert', 'path/to/cert_key')
    assert result['verify'] is True

def test_make_send_kwargs_mergeable_from_env_with_cert_only():
    args = argparse.Namespace(
        cert='path/to/cert',
        cert_key=None,
        proxy=[],
        verify='yes'
    )
    result = make_send_kwargs_mergeable_from_env(args)
    assert result['cert'] == 'path/to/cert'
    assert result['verify'] is True

def test_make_send_kwargs_mergeable_from_env_without_cert():
    args = argparse.Namespace(
        cert=None,
        cert_key=None,
        proxy=[],
        verify='yes'
    )
    result = make_send_kwargs_mergeable_from_env(args)
    assert result['cert'] is None
    assert result['verify'] is True
