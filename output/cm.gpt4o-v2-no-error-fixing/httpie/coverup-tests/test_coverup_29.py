# file: httpie/client.py:215-220
# asked: {"lines": [215, 216, 217, 218, 220], "branches": []}
# gained: {"lines": [215, 216, 217, 218, 220], "branches": []}

import pytest
import argparse
from httpie.client import make_send_kwargs

def test_make_send_kwargs_with_timeout():
    args = argparse.Namespace(timeout=30)
    kwargs = make_send_kwargs(args)
    assert kwargs == {'timeout': 30, 'allow_redirects': False}

def test_make_send_kwargs_without_timeout():
    args = argparse.Namespace(timeout=None)
    kwargs = make_send_kwargs(args)
    assert kwargs == {'timeout': None, 'allow_redirects': False}
