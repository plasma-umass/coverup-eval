# file tornado/auth.py:80-87
# lines [80, 81]
# branches []

import pytest
from tornado.auth import OpenIdMixin

class DummyOpenIdMixin(OpenIdMixin):
    _OPENID_ENDPOINT = "http://example.com/openid"

def test_openid_mixin_endpoint():
    mixin = DummyOpenIdMixin()
    assert hasattr(mixin, "_OPENID_ENDPOINT")
    assert mixin._OPENID_ENDPOINT == "http://example.com/openid"
