# file: apimd/parser.py:74-87
# asked: {"lines": [74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87], "branches": [[76, 0], [76, 77], [77, 78], [77, 80], [80, 81], [80, 87], [82, 83], [82, 84]]}
# gained: {"lines": [74, 76, 77, 78, 79, 80, 81, 82, 84, 85, 87], "branches": [[76, 0], [76, 77], [77, 78], [77, 80], [80, 81], [80, 87], [82, 84]]}

import pytest
from ast import If, Try, FunctionDef, Pass
from apimd.parser import walk_body

def test_walk_body_if():
    # Create an AST for if statement
    if_node = If(test=None, body=[Pass()], orelse=[Pass()])
    body = [if_node]
    
    result = list(walk_body(body))
    
    assert len(result) == 2
    assert isinstance(result[0], Pass)
    assert isinstance(result[1], Pass)

def test_walk_body_try():
    # Create an AST for try statement
    try_node = Try(body=[Pass()], handlers=[], orelse=[Pass()], finalbody=[Pass()])
    body = [try_node]
    
    result = list(walk_body(body))
    
    assert len(result) == 3
    assert isinstance(result[0], Pass)
    assert isinstance(result[1], Pass)
    assert isinstance(result[2], Pass)

def test_walk_body_mixed():
    # Create a mixed AST with if and try statements
    if_node = If(test=None, body=[Pass()], orelse=[Pass()])
    try_node = Try(body=[Pass()], handlers=[], orelse=[Pass()], finalbody=[Pass()])
    body = [if_node, try_node]
    
    result = list(walk_body(body))
    
    assert len(result) == 5
    assert isinstance(result[0], Pass)
    assert isinstance(result[1], Pass)
    assert isinstance(result[2], Pass)
    assert isinstance(result[3], Pass)
    assert isinstance(result[4], Pass)

def test_walk_body_simple():
    # Create a simple AST with only one statement
    body = [Pass()]
    
    result = list(walk_body(body))
    
    assert len(result) == 1
    assert isinstance(result[0], Pass)
