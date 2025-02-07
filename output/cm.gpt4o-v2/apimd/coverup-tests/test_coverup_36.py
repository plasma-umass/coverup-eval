# file: apimd/parser.py:381-416
# asked: {"lines": [385, 386, 387, 388, 389, 390, 391, 392, 393, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415, 416], "branches": [[390, 391], [390, 392], [392, 393], [392, 395], [397, 398], [397, 399], [401, 402], [401, 403], [403, 404], [403, 408], [410, 411], [410, 412], [412, 413], [412, 414], [414, 0], [414, 415], [415, 414], [415, 416]]}
# gained: {"lines": [385, 386, 387, 388, 389, 390, 391, 392, 393, 395, 396, 397, 398, 399, 400, 401, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415, 416], "branches": [[390, 391], [390, 392], [392, 393], [392, 395], [397, 398], [401, 403], [403, 404], [403, 408], [410, 411], [410, 412], [412, 413], [412, 414], [414, 0], [414, 415], [415, 416]]}

import pytest
from unittest.mock import MagicMock
from ast import FunctionDef, AsyncFunctionDef, ClassDef, arguments, arg, Name, Expr, Str
from apimd.parser import Parser, _m, esc_underscore, table, code, doctest, walk_body

@pytest.fixture
def parser():
    return Parser(b_level=1, level={}, root={}, doc={}, docstring={}, link=True)

def test_api_function_def(parser, mocker):
    node = FunctionDef(
        name='test_func',
        args=arguments(
            args=[arg(arg='x', annotation=None)],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        ),
        body=[],
        decorator_list=[]
    )
    mocker.patch.object(parser, 'resolve', return_value='resolved_decorator')
    mocker.patch.object(parser, 'func_api')
    parser.level['root'] = 1
    parser.api('root', node)
    assert 'root.test_func' in parser.doc
    assert parser.func_api.called

def test_api_async_function_def(parser, mocker):
    node = AsyncFunctionDef(
        name='test_async_func',
        args=arguments(
            args=[arg(arg='x', annotation=None)],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        ),
        body=[],
        decorator_list=[]
    )
    mocker.patch.object(parser, 'resolve', return_value='resolved_decorator')
    mocker.patch.object(parser, 'func_api')
    parser.level['root'] = 1
    parser.api('root', node)
    assert 'root.test_async_func' in parser.doc
    assert parser.func_api.called

def test_api_class_def(parser, mocker):
    node = ClassDef(
        name='TestClass',
        bases=[],
        keywords=[],
        body=[
            FunctionDef(
                name='method',
                args=arguments(
                    posonlyargs=[],
                    args=[arg(arg='self', annotation=None)],
                    vararg=None,
                    kwonlyargs=[],
                    kw_defaults=[],
                    kwarg=None,
                    defaults=[]
                ),
                body=[],
                decorator_list=[]
            )
        ],
        decorator_list=[]
    )
    mocker.patch.object(parser, 'resolve', return_value='resolved_decorator')
    mocker.patch.object(parser, 'class_api')
    parser.level['root'] = 1
    parser.api('root', node)
    assert 'root.TestClass' in parser.doc
    assert parser.class_api.called
    assert 'root.TestClass.method' in parser.doc

def test_api_with_docstring(parser, mocker):
    node = FunctionDef(
        name='test_func_with_doc',
        args=arguments(
            posonlyargs=[],
            args=[arg(arg='x', annotation=None)],
            vararg=None,
            kwonlyargs=[],
            kw_defaults=[],
            kwarg=None,
            defaults=[]
        ),
        body=[Expr(value=Str(s='This is a docstring'))],
        decorator_list=[]
    )
    mocker.patch.object(parser, 'resolve', return_value='resolved_decorator')
    mocker.patch.object(parser, 'func_api')
    parser.level['root'] = 1
    parser.api('root', node)
    assert 'root.test_func_with_doc' in parser.doc
    assert 'root.test_func_with_doc' in parser.docstring
    assert parser.func_api.called
