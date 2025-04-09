# file: apimd/parser.py:201-206
# asked: {"lines": [201, 203, 204, 205, 206], "branches": []}
# gained: {"lines": [201, 203, 204, 205, 206], "branches": []}

import pytest
from apimd.parser import Resolver

def test_resolver_init():
    root = "root_module"
    alias = {"alias_key": "alias_value"}
    self_ty = "self_type"

    resolver = Resolver(root, alias, self_ty)

    assert resolver.root == root
    assert resolver.alias == alias
    assert resolver.self_ty == self_ty

    # Test with default self_ty
    resolver_default = Resolver(root, alias)
    assert resolver_default.self_ty == ""
