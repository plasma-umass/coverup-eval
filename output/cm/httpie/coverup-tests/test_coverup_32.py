# file httpie/client.py:215-220
# lines [215, 216, 217, 218, 220]
# branches []

import argparse
import pytest
from httpie.client import make_send_kwargs

# Test function to cover the make_send_kwargs function
def test_make_send_kwargs():
    # Create a mock argparse.Namespace with different scenarios
    args_with_timeout = argparse.Namespace(timeout=30)
    args_without_timeout = argparse.Namespace(timeout=None)

    # Call the function with timeout set
    kwargs_with_timeout = make_send_kwargs(args_with_timeout)
    assert kwargs_with_timeout['timeout'] == 30
    assert kwargs_with_timeout['allow_redirects'] == False

    # Call the function without timeout set
    kwargs_without_timeout = make_send_kwargs(args_without_timeout)
    assert kwargs_without_timeout['timeout'] is None
    assert kwargs_without_timeout['allow_redirects'] == False
