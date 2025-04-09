# file: apimd/parser.py:494-511
# asked: {"lines": [494, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 511], "branches": [[498, 0], [498, 499], [499, 500], [499, 506], [500, 501], [500, 505], [502, 503], [502, 505], [506, 507], [506, 508], [508, 509], [508, 511]]}
# gained: {"lines": [494, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506, 507, 508, 509, 511], "branches": [[498, 0], [498, 499], [499, 500], [499, 506], [500, 501], [502, 503], [502, 505], [506, 507], [506, 508], [508, 509], [508, 511]]}

import pytest
from unittest.mock import MagicMock
from apimd.parser import Parser, arg

@pytest.fixture
def parser():
    return Parser(link=True, b_level=1, toc=False, level={}, doc={}, docstring={}, imp={}, root={}, alias={}, const={})

def test_func_ann_with_self_and_cls_method(parser, mocker):
    mocker.patch.object(parser, 'resolve', return_value='resolved_annotation')
    root = 'root'
    args = [arg(arg='self', annotation='annotation')]
    has_self = True
    cls_method = True

    result = list(parser.func_ann(root, args, has_self=has_self, cls_method=cls_method))
    
    assert result == ['type[Self]']
    parser.resolve.assert_called_once_with(root, 'annotation')

def test_func_ann_with_self_without_cls_method(parser, mocker):
    mocker.patch.object(parser, 'resolve', return_value='resolved_annotation')
    root = 'root'
    args = [arg(arg='self', annotation='annotation')]
    has_self = True
    cls_method = False

    result = list(parser.func_ann(root, args, has_self=has_self, cls_method=cls_method))
    
    assert result == ['Self']
    parser.resolve.assert_called_once_with(root, 'annotation')

def test_func_ann_with_star_arg(parser):
    root = 'root'
    args = [arg(arg='*', annotation=None)]
    has_self = False
    cls_method = False

    result = list(parser.func_ann(root, args, has_self=has_self, cls_method=cls_method))
    
    assert result == ['']

def test_func_ann_with_annotation(parser, mocker):
    mocker.patch.object(parser, 'resolve', return_value='resolved_annotation')
    root = 'root'
    args = [arg(arg='arg', annotation='annotation')]
    has_self = False
    cls_method = False

    result = list(parser.func_ann(root, args, has_self=has_self, cls_method=cls_method))
    
    assert result == ['resolved_annotation']
    parser.resolve.assert_called_once_with(root, 'annotation', '')

def test_func_ann_without_annotation(parser):
    root = 'root'
    args = [arg(arg='arg', annotation=None)]
    has_self = False
    cls_method = False

    result = list(parser.func_ann(root, args, has_self=has_self, cls_method=cls_method))
    
    assert result == ['Any']
