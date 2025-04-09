# file: apimd/parser.py:381-416
# asked: {"lines": [381, 385, 386, 387, 388, 389, 390, 391, 392, 393, 395, 396, 397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 408, 409, 410, 411, 412, 413, 414, 415, 416], "branches": [[390, 391], [390, 392], [392, 393], [392, 395], [397, 398], [397, 399], [401, 402], [401, 403], [403, 404], [403, 408], [410, 411], [410, 412], [412, 413], [412, 414], [414, 0], [414, 415], [415, 414], [415, 416]]}
# gained: {"lines": [381, 385, 386, 387, 388, 389, 390, 391, 392, 393, 395, 396, 397, 399, 400, 401, 403, 404, 405, 406, 408, 409, 410, 412, 413, 414, 415], "branches": [[390, 391], [390, 392], [392, 393], [392, 395], [397, 399], [401, 403], [403, 404], [403, 408], [410, 412], [412, 413], [412, 414], [414, 0], [414, 415], [415, 414]]}

import pytest
from unittest.mock import MagicMock
from ast import FunctionDef, AsyncFunctionDef, ClassDef, arguments, arg, Name, Expr, Str, Assign, AnnAssign, Delete

@pytest.fixture
def parser():
    from apimd.parser import Parser
    parser = Parser()
    parser.b_level = 1
    parser.level = {}
    parser.root = {}
    parser.doc = {}
    parser.docstring = {}
    parser.link = False
    return parser

def test_api_function_def(parser, mocker):
    node = FunctionDef(
        name='test_func',
        args=arguments(
            posonlyargs=[],
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
    mocker.patch('apimd.parser._m', return_value='test_func')
    mocker.patch('apimd.parser.esc_underscore', return_value='test_func')
    mocker.patch('apimd.parser.get_docstring', return_value=None)
    mocker.patch('apimd.parser.walk_body', return_value=[])
    parser.level['root'] = 1
    parser.api('root', node)
    assert 'test_func' in parser.doc

def test_api_async_function_def(parser, mocker):
    node = AsyncFunctionDef(
        name='test_async_func',
        args=arguments(
            posonlyargs=[],
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
    mocker.patch('apimd.parser._m', return_value='test_async_func')
    mocker.patch('apimd.parser.esc_underscore', return_value='test_async_func')
    mocker.patch('apimd.parser.get_docstring', return_value=None)
    mocker.patch('apimd.parser.walk_body', return_value=[])
    parser.level['root'] = 1
    parser.api('root', node)
    assert 'test_async_func' in parser.doc

def test_api_class_def(parser, mocker):
    node = ClassDef(
        name='TestClass',
        bases=[],
        keywords=[],
        body=[],
        decorator_list=[]
    )
    mocker.patch('apimd.parser._m', return_value='TestClass')
    mocker.patch('apimd.parser.esc_underscore', return_value='TestClass')
    mocker.patch('apimd.parser.get_docstring', return_value=None)
    mocker.patch('apimd.parser.walk_body', return_value=[])
    parser.level['root'] = 1
    parser.api('root', node)
    assert 'TestClass' in parser.doc

def test_class_api(parser, mocker):
    node = ClassDef(
        name='TestClass',
        bases=[],
        keywords=[],
        body=[
            AnnAssign(target=Name(id='attr1', ctx=None), annotation=Name(id='int', ctx=None), value=None, simple=1),
            Assign(targets=[Name(id='attr2', ctx=None)], value=Str(s='value'), type_comment=None),
            Delete(targets=[Name(id='attr2', ctx=None)])
        ],
        decorator_list=[]
    )
    mocker.patch('apimd.parser._m', return_value='TestClass')
    mocker.patch('apimd.parser.esc_underscore', return_value='TestClass')
    mocker.patch('apimd.parser.get_docstring', return_value=None)
    mocker.patch('apimd.parser.walk_body', return_value=node.body)
    parser.level['root'] = 1
    parser.api('root', node)
    assert 'TestClass' in parser.doc

def test_func_api(parser, mocker):
    node = FunctionDef(
        name='test_func',
        args=arguments(
            posonlyargs=[],
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
    mocker.patch('apimd.parser._m', return_value='test_func')
    mocker.patch('apimd.parser.esc_underscore', return_value='test_func')
    mocker.patch('apimd.parser.get_docstring', return_value=None)
    mocker.patch('apimd.parser.walk_body', return_value=[])
    parser.level['root'] = 1
    parser.api('root', node)
    assert 'test_func' in parser.doc
