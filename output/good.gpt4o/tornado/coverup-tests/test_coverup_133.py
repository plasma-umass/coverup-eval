# file tornado/netutil.py:335-337
# lines [335, 336, 337]
# branches []

import pytest
from tornado.netutil import Resolver, DefaultExecutorResolver

def test_resolver_configurable_default():
    class TestResolver(Resolver):
        @classmethod
        def configurable_default(cls):
            return super().configurable_default()

    resolver_instance = TestResolver()
    default_class = resolver_instance.configurable_default()
    assert default_class == DefaultExecutorResolver
