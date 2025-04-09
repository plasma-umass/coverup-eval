# file: apimd/parser.py:236-257
# asked: {"lines": [239, 243, 244, 245, 246, 247, 248, 250, 252, 253, 254, 255], "branches": [[238, 239], [242, 243], [243, 244], [243, 245], [246, 247], [246, 248], [249, 250], [251, 252]]}
# gained: {"lines": [239, 243, 245, 246, 247, 248, 250, 252, 253, 254, 255], "branches": [[238, 239], [242, 243], [243, 245], [246, 247], [246, 248], [249, 250], [251, 252]]}

import pytest
from ast import Subscript, Name, Load, Tuple, Constant, BinOp, BitOr
from apimd.parser import Resolver
from apimd.pep585 import PEP585
from apimd.logger import logger

@pytest.fixture
def resolver():
    return Resolver(root='root', alias={'root.Union': 'typing.Union', 'root.Optional': 'typing.Optional'})

def test_visit_subscript_typing_union(resolver):
    node = Subscript(
        value=Name(id='Union', ctx=Load()),
        slice=Tuple(elts=[Constant(value=1), Constant(value=2)], ctx=Load()),
        ctx=Load()
    )
    result = resolver.visit_Subscript(node)
    assert isinstance(result, BinOp)
    assert isinstance(result.op, BitOr)
    assert isinstance(result.left, Constant)
    assert isinstance(result.right, Constant)

def test_visit_subscript_typing_optional(resolver):
    node = Subscript(
        value=Name(id='Optional', ctx=Load()),
        slice=Constant(value=1),
        ctx=Load()
    )
    result = resolver.visit_Subscript(node)
    assert isinstance(result, BinOp)
    assert isinstance(result.op, BitOr)
    assert isinstance(result.left, Constant)
    assert result.right.value is None

def test_visit_subscript_pep585(resolver, mocker):
    mocker.patch('apimd.logger.logger.warning')
    node = Subscript(
        value=Name(id='List', ctx=Load()),
        slice=Constant(value=1),
        ctx=Load()
    )
    PEP585['List'] = 'list'
    node.lineno = 1
    node.col_offset = 0
    result = resolver.visit_Subscript(node)
    assert isinstance(result, Subscript)
    assert isinstance(result.value, Name)
    assert result.value.id == 'list'
    logger.warning.assert_called_once()

def test_visit_subscript_no_match(resolver):
    node = Subscript(
        value=Name(id='Unknown', ctx=Load()),
        slice=Constant(value=1),
        ctx=Load()
    )
    result = resolver.visit_Subscript(node)
    assert result == node

def test_visit_subscript_not_name(resolver):
    node = Subscript(
        value=Constant(value=1),
        slice=Constant(value=1),
        ctx=Load()
    )
    result = resolver.visit_Subscript(node)
    assert result == node
