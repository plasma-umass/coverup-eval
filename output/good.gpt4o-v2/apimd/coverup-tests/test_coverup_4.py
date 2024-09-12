# file: apimd/parser.py:74-87
# asked: {"lines": [74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87], "branches": [[76, 0], [76, 77], [77, 78], [77, 80], [80, 81], [80, 87], [82, 83], [82, 84]]}
# gained: {"lines": [74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87], "branches": [[76, 0], [76, 77], [77, 78], [77, 80], [80, 81], [80, 87], [82, 83], [82, 84]]}

import pytest
from ast import If, Try, Pass, ExceptHandler
from apimd.parser import walk_body

def test_walk_body_if():
    if_node = If(test=Pass(), body=[Pass()], orelse=[Pass()])
    body = [if_node]
    result = list(walk_body(body))
    assert result == [if_node.body[0], if_node.orelse[0]]

def test_walk_body_try():
    try_node = Try(body=[Pass()], handlers=[ExceptHandler(body=[Pass()])], orelse=[Pass()], finalbody=[Pass()])
    body = [try_node]
    result = list(walk_body(body))
    assert result == [try_node.body[0], try_node.handlers[0].body[0], try_node.orelse[0], try_node.finalbody[0]]

def test_walk_body_else():
    pass_node = Pass()
    body = [pass_node]
    result = list(walk_body(body))
    assert result == [pass_node]
