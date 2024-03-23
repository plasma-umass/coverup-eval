# file apimd/parser.py:494-511
# lines [500, 501, 502, 503, 504, 505]
# branches ['499->500', '500->501', '500->505', '502->503', '502->505']

import pytest
from apimd.parser import Parser
from typing import Sequence, Iterator
from dataclasses import dataclass
from unittest.mock import MagicMock

@dataclass
class MockArg:
    arg: str
    annotation: str = None

@pytest.fixture
def parser(mocker):
    parser = Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})
    parser.resolve = mocker.MagicMock(return_value='ResolvedType')
    return parser

def test_func_ann_with_self_and_cls_method(parser):
    root = 'root'
    args = [MockArg(arg='self', annotation='SomeAnnotation'), MockArg(arg='arg1', annotation='Arg1Annotation')]
    has_self = True
    cls_method = True

    result = list(parser.func_ann(root, args, has_self=has_self, cls_method=cls_method))

    assert parser.resolve.call_args_list[0][0][1] == 'SomeAnnotation'
    assert parser.resolve.call_args_list[1][0][1] == 'Arg1Annotation'
    assert result == ['type[Self]', 'ResolvedType']

def test_func_ann_with_self_without_cls_method(parser):
    root = 'root'
    args = [MockArg(arg='self', annotation='SomeAnnotation'), MockArg(arg='arg1', annotation='Arg1Annotation')]
    has_self = True
    cls_method = False

    result = list(parser.func_ann(root, args, has_self=has_self, cls_method=cls_method))

    assert parser.resolve.call_args_list[0][0][1] == 'SomeAnnotation'
    assert parser.resolve.call_args_list[1][0][1] == 'Arg1Annotation'
    assert result == ['Self', 'ResolvedType']
