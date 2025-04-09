# file: apimd/parser.py:74-87
# asked: {"lines": [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87], "branches": [[76, 0], [76, 77], [77, 78], [77, 80], [80, 81], [80, 87], [82, 83], [82, 84]]}
# gained: {"lines": [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87], "branches": [[76, 0], [76, 77], [77, 78], [77, 80], [80, 81], [80, 87], [82, 83], [82, 84]]}

import pytest
from unittest.mock import MagicMock
from typing import List
from ast import If, Try, stmt

from apimd.parser import walk_body

def test_walk_body_if(monkeypatch):
    if_node = MagicMock(spec=If)
    if_node.body = [MagicMock(spec=stmt)]
    if_node.orelse = [MagicMock(spec=stmt)]
    
    body = [if_node]
    
    result = list(walk_body(body))
    
    assert result == if_node.body + if_node.orelse

def test_walk_body_try(monkeypatch):
    try_node = MagicMock(spec=Try)
    try_node.body = [MagicMock(spec=stmt)]
    handler = MagicMock()
    handler.body = [MagicMock(spec=stmt)]
    try_node.handlers = [handler]
    try_node.orelse = [MagicMock(spec=stmt)]
    try_node.finalbody = [MagicMock(spec=stmt)]
    
    body = [try_node]
    
    result = list(walk_body(body))
    
    assert result == try_node.body + handler.body + try_node.orelse + try_node.finalbody

def test_walk_body_other(monkeypatch):
    other_node = MagicMock(spec=stmt)
    
    body = [other_node]
    
    result = list(walk_body(body))
    
    assert result == [other_node]
