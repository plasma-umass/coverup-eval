# file httpie/client.py:223-240
# lines [223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 240]
# branches ['225->226', '225->229', '227->228', '227->229']

import argparse
import pytest
from unittest import mock
from httpie.client import make_send_kwargs_mergeable_from_env

def test_make_send_kwargs_mergeable_from_env(mocker):
    # Mock the argparse.Namespace object
    args = mocker.Mock(spec=argparse.Namespace)
    
    # Set up the mock arguments
    args.cert = 'path/to/cert'
    args.cert_key = 'path/to/cert_key'
    args.proxy = [argparse.Namespace(key='http', value='http://proxy.example.com')]
    args.verify = 'yes'
    
    # Call the function with the mocked arguments
    result = make_send_kwargs_mergeable_from_env(args)
    
    # Assertions to verify the postconditions
    assert result['proxies'] == {'http': 'http://proxy.example.com'}
    assert result['stream'] is True
    assert result['verify'] is True
    assert result['cert'] == ('path/to/cert', 'path/to/cert_key')

    # Clean up
    mocker.stopall()

@pytest.fixture(autouse=True)
def run_around_tests():
    # Code to run before each test
    yield
    # Code to run after each test
    mock.patch.stopall()
