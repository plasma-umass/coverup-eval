# file apimd/parser.py:494-511
# lines []
# branches ['500->505', '502->505']

import pytest
from unittest.mock import MagicMock
from apimd.parser import Parser
from typing import Iterator, Sequence
from dataclasses import dataclass

@dataclass
class Arg:
    annotation: str = None
    arg: str = None

@pytest.fixture
def parser():
    return Parser()

def test_func_ann_branches(parser, mocker):
    # Mock the resolve method to return a specific value
    mocker.patch.object(parser, 'resolve', return_value='resolved_annotation')

    # Test case to cover branch 500->505, 502->505
    args = [Arg(annotation='some_annotation')]
    result = list(parser.func_ann(root='root', args=args, has_self=True, cls_method=True))
    assert result == ['type[Self]']

    # Test case to cover branch 500->505 without cls_method
    result = list(parser.func_ann(root='root', args=args, has_self=True, cls_method=False))
    assert result == ['Self']

    # Test case to cover branch 502->505 with cls_method
    args = [Arg(annotation='type[some_annotation]')]
    result = list(parser.func_ann(root='root', args=args, has_self=True, cls_method=True))
    assert result == ['type[Self]']

    # Test case to cover branch 502->505 without cls_method
    result = list(parser.func_ann(root='root', args=args, has_self=True, cls_method=False))
    assert result == ['Self']
