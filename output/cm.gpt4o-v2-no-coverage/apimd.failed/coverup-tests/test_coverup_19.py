# file: apimd/parser.py:74-87
# asked: {"lines": [74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87], "branches": [[76, 0], [76, 77], [77, 78], [77, 80], [80, 81], [80, 87], [82, 83], [82, 84]]}
# gained: {"lines": [74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87], "branches": [[76, 0], [76, 77], [77, 78], [77, 80], [80, 81], [80, 87], [82, 83], [82, 84]]}

import pytest
from ast import If, Try, Expr, Pass
from apimd.parser import walk_body

def test_walk_body_if():
    # Create a mock If node
    if_node = If(test=Expr(value=Pass()), body=[Expr(value=Pass())], orelse=[Expr(value=Pass())])
    body = [if_node]
    
    result = list(walk_body(body))
    
    assert len(result) == 2
    assert isinstance(result[0], Expr)
    assert isinstance(result[1], Expr)

def test_walk_body_try():
    # Create a mock Try node
    try_node = Try(
        body=[Expr(value=Pass())],
        handlers=[If(test=Expr(value=Pass()), body=[Expr(value=Pass())], orelse=[])],
        orelse=[Expr(value=Pass())],
        finalbody=[Expr(value=Pass())]
    )
    body = [try_node]
    
    result = list(walk_body(body))
    
    assert len(result) == 4
    assert isinstance(result[0], Expr)
    assert isinstance(result[1], Expr)
    assert isinstance(result[2], Expr)
    assert isinstance(result[3], Expr)

def test_walk_body_mixed():
    # Create a mix of If and Try nodes
    if_node = If(test=Expr(value=Pass()), body=[Expr(value=Pass())], orelse=[Expr(value=Pass())])
    try_node = Try(
        body=[Expr(value=Pass())],
        handlers=[If(test=Expr(value=Pass()), body=[Expr(value=Pass())], orelse=[])],
        orelse=[Expr(value=Pass())],
        finalbody=[Expr(value=Pass())]
    )
    body = [if_node, try_node]
    
    result = list(walk_body(body))
    
    assert len(result) == 6
    assert isinstance(result[0], Expr)
    assert isinstance(result[1], Expr)
    assert isinstance(result[2], Expr)
    assert isinstance(result[3], Expr)
    assert isinstance(result[4], Expr)
    assert isinstance(result[5], Expr)

def test_walk_body_simple():
    # Create a simple body with no If or Try nodes
    body = [Expr(value=Pass()), Expr(value=Pass())]
    
    result = list(walk_body(body))
    
    assert len(result) == 2
    assert isinstance(result[0], Expr)
    assert isinstance(result[1], Expr)
