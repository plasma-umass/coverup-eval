# file: apimd/parser.py:418-449
# asked: {"lines": [422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449], "branches": [[424, 425], [424, 428], [431, 432], [431, 433], [433, 434], [433, 435], [439, 440], [439, 442]]}
# gained: {"lines": [422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449], "branches": [[424, 425], [431, 432], [439, 440]]}

import pytest
from ast import arg, arguments, Name, Load, Constant
from typing import Optional
from unittest.mock import MagicMock
from apimd.parser import Parser

@pytest.fixture
def parser():
    return Parser()

def test_func_api_full_coverage(parser, mocker):
    # Mocking the func_ann method
    mocker.patch.object(parser, 'func_ann', return_value=iter(['int', 'str', 'float']))

    # Mocking the doc attribute
    parser.doc = {'test_func': ''}

    # Creating a mock arguments object
    node = arguments(
        posonlyargs=[arg(arg='a', annotation=Name(id='int', ctx=Load()))],
        args=[arg(arg='b', annotation=Name(id='str', ctx=Load()))],
        vararg=arg(arg='args', annotation=None),
        kwonlyargs=[arg(arg='kw', annotation=Name(id='float', ctx=Load()))],
        kw_defaults=[Constant(value=None)],
        kwarg=arg(arg='kwargs', annotation=None),
        defaults=[Constant(value=1)]
    )

    # Call the func_api method
    parser.func_api(
        root='root',
        name='test_func',
        node=node,
        returns=Name(id='None', ctx=Load()),
        has_self=False,
        cls_method=False
    )

    # Assertions to verify the expected behavior
    assert 'test_func' in parser.doc
    assert 'a' in parser.doc['test_func']
    assert 'b' in parser.doc['test_func']
    assert '*' in parser.doc['test_func']
    assert 'kw' in parser.doc['test_func']
    assert '**' in parser.doc['test_func']
    assert 'return' in parser.doc['test_func']
