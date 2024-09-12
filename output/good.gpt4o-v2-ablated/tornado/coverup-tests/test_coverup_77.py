# file: tornado/netutil.py:331-333
# asked: {"lines": [331, 332, 333], "branches": []}
# gained: {"lines": [331, 332, 333], "branches": []}

import pytest
from tornado.netutil import Resolver

class TestResolver:
    def test_configurable_base(self):
        base_class = Resolver.configurable_base()
        assert base_class is Resolver
