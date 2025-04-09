# file: apimd/parser.py:74-87
# asked: {"lines": [74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87], "branches": [[76, 0], [76, 77], [77, 78], [77, 80], [80, 81], [80, 87], [82, 83], [82, 84]]}
# gained: {"lines": [74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87], "branches": [[76, 0], [76, 77], [77, 78], [77, 80], [80, 81], [80, 87], [82, 83], [82, 84]]}

import pytest
from typing import List
from apimd.parser import walk_body
from ast import If, Try, Pass, stmt

def test_walk_body_if_statement():
    if_node = If(test=Pass(), body=[Pass()], orelse=[Pass()])
    body = [if_node]
    result = list(walk_body(body))
    assert len(result) == 2
    assert isinstance(result[0], Pass)
    assert isinstance(result[1], Pass)

def test_walk_body_try_statement():
    try_node = Try(body=[Pass()], handlers=[], orelse=[Pass()], finalbody=[Pass()])
    body = [try_node]
    result = list(walk_body(body))
    assert len(result) == 3
    assert isinstance(result[0], Pass)
    assert isinstance(result[1], Pass)
    assert isinstance(result[2], Pass)

def test_walk_body_try_with_handler():
    try_node = Try(body=[Pass()], handlers=[If(test=Pass(), body=[Pass()], orelse=[])], orelse=[], finalbody=[])
    body = [try_node]
    result = list(walk_body(body))
    assert len(result) == 2
    assert isinstance(result[0], Pass)
    assert isinstance(result[1], Pass)

def test_walk_body_mixed_statements():
    if_node = If(test=Pass(), body=[Pass()], orelse=[Pass()])
    try_node = Try(body=[Pass()], handlers=[If(test=Pass(), body=[Pass()], orelse=[])], orelse=[Pass()], finalbody=[Pass()])
    body = [if_node, try_node]
    result = list(walk_body(body))
    assert len(result) == 6
    assert all(isinstance(node, Pass) for node in result)

def test_walk_body_simple_statement():
    simple_node = Pass()
    body = [simple_node]
    result = list(walk_body(body))
    assert result == [simple_node]
