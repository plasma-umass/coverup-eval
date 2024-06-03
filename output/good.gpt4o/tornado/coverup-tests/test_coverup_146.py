# file tornado/auth.py:80-87
# lines [80, 81]
# branches []

import pytest
from tornado.auth import OpenIdMixin

def test_openid_mixin():
    class TestOpenIdMixin(OpenIdMixin):
        _OPENID_ENDPOINT = "http://example.com/openid"

    mixin = TestOpenIdMixin()
    assert hasattr(mixin, '_OPENID_ENDPOINT')
    assert mixin._OPENID_ENDPOINT == "http://example.com/openid"
