# file apimd/parser.py:201-206
# lines [201, 203, 204, 205, 206]
# branches []

import pytest
from apimd.parser import Resolver
from ast import NodeTransformer

# Assuming the Resolver class is part of a larger module that we're testing

def test_resolver_initialization(mocker):
    # Mock the NodeTransformer __init__ to ensure no side effects
    init_mock = mocker.patch.object(NodeTransformer, '__init__', return_value=None)
    
    root = "root_module"
    alias = {"alias_key": "alias_value"}
    self_ty = "self_type"
    
    resolver = Resolver(root, alias, self_ty)
    
    assert resolver.root == root
    assert resolver.alias == alias
    assert resolver.self_ty == self_ty
    
    # Verify that the NodeTransformer __init__ was called
    init_mock.assert_called_once_with()
