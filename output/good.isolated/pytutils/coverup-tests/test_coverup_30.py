# file pytutils/lazy/lazy_import.py:194-203
# lines [194, 203]
# branches []

import pytest
from pytutils.lazy.lazy_import import disallow_proxying, ScopeReplacer

def test_disallow_proxying(mocker):
    # Mock the ScopeReplacer to verify that _should_proxy is set to False
    mocker.patch.object(ScopeReplacer, '_should_proxy', new_callable=mocker.PropertyMock)
    ScopeReplacer._should_proxy.return_value = True

    # Call the function that should change _should_proxy to False
    disallow_proxying()

    # Assert that _should_proxy is now False
    assert not ScopeReplacer._should_proxy

    # Clean up by setting _should_proxy back to its default value (True)
    ScopeReplacer._should_proxy = True
