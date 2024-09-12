# file: apimd/parser.py:201-206
# asked: {"lines": [201, 203, 204, 205, 206], "branches": []}
# gained: {"lines": [201, 203, 204, 205, 206], "branches": []}

import pytest
from apimd.parser import Resolver

def test_resolver_initialization():
    root = "root_module"
    alias = {"alias1": "module1", "alias2": "module2"}
    self_ty = "self_type"

    resolver = Resolver(root, alias, self_ty)

    assert resolver.root == root
    assert resolver.alias == alias
    assert resolver.self_ty == self_ty

def test_resolver_initialization_default_self_ty():
    root = "root_module"
    alias = {"alias1": "module1", "alias2": "module2"}

    resolver = Resolver(root, alias)

    assert resolver.root == root
    assert resolver.alias == alias
    assert resolver.self_ty == ""
