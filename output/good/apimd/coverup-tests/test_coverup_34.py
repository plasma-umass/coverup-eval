# file apimd/parser.py:208-217
# lines [212, 213, 214, 215, 217]
# branches ['210->212']

import pytest
from apimd.parser import Resolver
from ast import parse, Expr, Constant, NodeTransformer

class MockResolver(Resolver):
    def __init__(self):
        super().__init__(root=None, alias=None)

def test_resolver_visit_constant_syntax_error(mocker):
    resolver = MockResolver()
    mocker.patch('apimd.parser.parse', side_effect=SyntaxError)

    # Create a Constant node with a string value that would cause a SyntaxError when parsed
    constant_node = Constant(value='invalid syntax')

    # Visit the node, which should trigger the SyntaxError branch
    result_node = resolver.visit_Constant(constant_node)

    # Assert that the result is the same node as the input, since it should return the node on SyntaxError
    assert result_node is constant_node
