# file httpie/client.py:223-240
# lines [223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 240]
# branches ['225->226', '225->229', '227->228', '227->229']

import argparse
import pytest
from httpie.client import make_send_kwargs_mergeable_from_env

class Proxy:
    def __init__(self, key, value):
        self.key = key
        self.value = value

@pytest.fixture
def args():
    args = argparse.Namespace()
    args.cert = None
    args.cert_key = None
    args.proxy = []
    args.verify = 'yes'
    return args

def test_make_send_kwargs_mergeable_from_env_with_cert_and_key(args):
    args.cert = '/path/to/cert.pem'
    args.cert_key = '/path/to/key.pem'
    args.proxy = [Proxy('http', 'http://localhost:3128')]
    args.verify = 'no'

    expected_kwargs = {
        'proxies': {'http': 'http://localhost:3128'},
        'stream': True,
        'verify': False,
        'cert': ('/path/to/cert.pem', '/path/to/key.pem'),
    }

    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs == expected_kwargs

def test_make_send_kwargs_mergeable_from_env_with_cert_without_key(args):
    args.cert = '/path/to/cert.pem'
    args.proxy = [Proxy('https', 'https://localhost:3128')]
    args.verify = 'true'

    expected_kwargs = {
        'proxies': {'https': 'https://localhost:3128'},
        'stream': True,
        'verify': True,
        'cert': '/path/to/cert.pem',
    }

    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs == expected_kwargs

def test_make_send_kwargs_mergeable_from_env_with_custom_verify(args):
    args.verify = '/path/to/ca_bundle.pem'
    args.proxy = [Proxy('http', 'http://localhost:3128')]

    expected_kwargs = {
        'proxies': {'http': 'http://localhost:3128'},
        'stream': True,
        'verify': '/path/to/ca_bundle.pem',
        'cert': None,
    }

    kwargs = make_send_kwargs_mergeable_from_env(args)
    assert kwargs == expected_kwargs
