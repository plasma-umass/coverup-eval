# file tornado/netutil.py:307-330
# lines [307, 308]
# branches []

import pytest
from tornado.netutil import Resolver, Configurable

def test_resolver_configure(mocker):
    # Mock the configure method to ensure it is called correctly
    mock_configure = mocker.patch.object(Configurable, 'configure')

    # Call the configure method on Resolver
    Resolver.configure('tornado.netutil.ThreadedResolver')

    # Assert that the configure method was called with the correct argument
    mock_configure.assert_called_once_with('tornado.netutil.ThreadedResolver')

    # Clean up by resetting the configuration to its default state
    Resolver.configure(None)
