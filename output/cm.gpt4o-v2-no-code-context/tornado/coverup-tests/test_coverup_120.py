# file: tornado/netutil.py:331-333
# asked: {"lines": [331, 332, 333], "branches": []}
# gained: {"lines": [331, 332, 333], "branches": []}

import pytest
from tornado.netutil import Resolver, Configurable

def test_resolver_configurable_base():
    class TestResolver(Resolver):
        pass

    assert TestResolver.configurable_base() is Resolver

@pytest.fixture(autouse=True)
def cleanup_resolver(monkeypatch):
    original_resolver = Resolver.configurable_base
    yield
    monkeypatch.setattr(Resolver, 'configurable_base', original_resolver)
