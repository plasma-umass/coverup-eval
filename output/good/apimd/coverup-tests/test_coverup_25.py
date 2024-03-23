# file apimd/parser.py:418-449
# lines [418, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449]
# branches ['424->425', '424->428', '431->432', '431->433', '433->434', '433->435', '439->440', '439->442']

import pytest
from apimd.parser import Parser
from typing import Optional
from dataclasses import dataclass
from ast import arg, arguments, expr

@dataclass
class MockExpr(expr):
    pass

@pytest.fixture
def parser():
    p = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
    yield p

def test_func_api_with_posonlyargs_and_kwonlyargs(parser):
    parser.doc['test_func'] = ''
    posonlyargs = [arg(arg='posonly1', annotation=None), arg(arg='posonly2', annotation=None)]
    args = [arg(arg='arg1', annotation=None), arg(arg='arg2', annotation=None)]
    kwonlyargs = [arg(arg='kwonly1', annotation=None), arg(arg='kwonly2', annotation=None)]
    kw_defaults = [MockExpr(), None]
    node = arguments(
        posonlyargs=posonlyargs,
        args=args,
        vararg=None,
        kwonlyargs=kwonlyargs,
        kw_defaults=kw_defaults,
        kwarg=None,
        defaults=[]
    )
    returns = MockExpr()
    parser.func_api(root='root', name='test_func', node=node, returns=returns, has_self=False, cls_method=False)

    assert 'test_func' in parser.doc
    assert len(parser.doc['test_func']) > 0

def test_func_api_with_vararg_and_kwarg(parser):
    parser.doc['test_func_var_kw'] = ''
    args = [arg(arg='arg1', annotation=None)]
    vararg = arg(arg='args', annotation=None)
    kwarg = arg(arg='kwargs', annotation=None)
    node = arguments(
        posonlyargs=[],
        args=args,
        vararg=vararg,
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=kwarg,
        defaults=[]
    )
    returns = MockExpr()
    parser.func_api(root='root', name='test_func_var_kw', node=node, returns=returns, has_self=False, cls_method=False)

    assert 'test_func_var_kw' in parser.doc
    assert len(parser.doc['test_func_var_kw']) > 0

def test_func_api_without_defaults(parser, mocker):
    parser.doc['test_func_no_defaults'] = ''
    mocker.patch('apimd.parser.code', return_value='code')
    mocker.patch('apimd.parser.table', return_value='table')
    mocker.patch('apimd.parser._defaults', return_value='defaults')

    args = [arg(arg='arg1', annotation=None)]
    node = arguments(
        posonlyargs=[],
        args=args,
        vararg=None,
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[]
    )
    returns = MockExpr()
    parser.func_api(root='root', name='test_func_no_defaults', node=node, returns=returns, has_self=False, cls_method=False)

    assert 'test_func_no_defaults' in parser.doc
    assert parser.doc['test_func_no_defaults'] == 'table'
