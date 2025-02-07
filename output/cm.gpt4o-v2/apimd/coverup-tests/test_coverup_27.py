# file: apimd/parser.py:236-257
# asked: {"lines": [236, 238, 239, 240, 241, 242, 243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 257], "branches": [[238, 239], [238, 240], [242, 243], [242, 249], [243, 244], [243, 245], [246, 247], [246, 248], [249, 250], [249, 251], [251, 252], [251, 257]]}
# gained: {"lines": [236, 238, 240, 241, 242, 243, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 257], "branches": [[238, 240], [242, 243], [242, 249], [243, 245], [246, 247], [246, 248], [249, 250], [249, 251], [251, 252], [251, 257]]}

import pytest
from ast import Subscript, Name, Load, Tuple, Constant, BinOp, BitOr
from apimd.parser import Resolver
from apimd.pep585 import PEP585

@pytest.fixture
def resolver():
    class MockResolver(Resolver):
        def __init__(self):
            self.alias = {}
            self.root = None
    return MockResolver()

def test_visit_subscript_typing_union(resolver):
    node = Subscript(
        value=Name(id='Union', ctx=Load()),
        slice=Tuple(elts=[Constant(value=1), Constant(value=2)], ctx=Load()),
        ctx=Load()
    )
    resolver.alias = {'Union': 'typing.Union'}
    result = resolver.visit_Subscript(node)
    assert isinstance(result, BinOp)
    assert isinstance(result.left, Constant)
    assert isinstance(result.op, BitOr)
    assert isinstance(result.right, Constant)

def test_visit_subscript_typing_optional(resolver):
    node = Subscript(
        value=Name(id='Optional', ctx=Load()),
        slice=Constant(value=1),
        ctx=Load()
    )
    resolver.alias = {'Optional': 'typing.Optional'}
    result = resolver.visit_Subscript(node)
    assert isinstance(result, BinOp)
    assert isinstance(result.left, Constant)
    assert isinstance(result.op, BitOr)
    assert result.right.value is None

def test_visit_subscript_pep585(resolver, mocker):
    node = Subscript(
        value=Name(id='List', ctx=Load()),
        slice=Constant(value=1),
        ctx=Load()
    )
    node.lineno = 1
    node.col_offset = 0
    resolver.alias = {'List': 'typing.List'}
    mock_logger = mocker.patch('apimd.parser.logger.warning')
    result = resolver.visit_Subscript(node)
    assert isinstance(result, Subscript)
    assert result.value.id == 'list'
    mock_logger.assert_called_once_with(f'{node.lineno}:{node.col_offset}: find deprecated name typing.List, recommended to use list')

def test_visit_subscript_other(resolver):
    node = Subscript(
        value=Name(id='Other', ctx=Load()),
        slice=Constant(value=1),
        ctx=Load()
    )
    resolver.alias = {'Other': 'typing.Other'}
    result = resolver.visit_Subscript(node)
    assert result == node
