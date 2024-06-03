# file httpie/client.py:215-220
# lines [215, 216, 217, 218, 220]
# branches []

import argparse
import pytest

from httpie.client import make_send_kwargs

def test_make_send_kwargs():
    # Test with timeout set
    args = argparse.Namespace(timeout=10)
    kwargs = make_send_kwargs(args)
    assert kwargs == {'timeout': 10, 'allow_redirects': False}

    # Test with timeout not set
    args = argparse.Namespace(timeout=None)
    kwargs = make_send_kwargs(args)
    assert kwargs == {'timeout': None, 'allow_redirects': False}

    # Test with timeout set to 0 (edge case)
    args = argparse.Namespace(timeout=0)
    kwargs = make_send_kwargs(args)
    assert kwargs == {'timeout': None, 'allow_redirects': False}
