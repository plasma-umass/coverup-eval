# file: apimd/parser.py:74-87
# asked: {"lines": [83], "branches": [[82, 83]]}
# gained: {"lines": [83], "branches": [[82, 83]]}

import pytest
from ast import parse, If, Try, Assign
from apimd.parser import walk_body

def test_walk_body_if():
    code = """
if True:
    x = 1
else:
    y = 2
"""
    tree = parse(code)
    body = list(walk_body(tree.body))
    assert len(body) == 2
    assert isinstance(body[0], Assign)
    assert isinstance(body[1], Assign)

def test_walk_body_try():
    code = """
try:
    x = 1
except Exception:
    y = 2
else:
    z = 3
finally:
    w = 4
"""
    tree = parse(code)
    body = list(walk_body(tree.body))
    assert len(body) == 4
    assert isinstance(body[0], Assign)
    assert isinstance(body[1], Assign)
    assert isinstance(body[2], Assign)
    assert isinstance(body[3], Assign)

def test_walk_body_mixed():
    code = """
if True:
    try:
        x = 1
    except Exception:
        y = 2
    else:
        z = 3
    finally:
        w = 4
else:
    v = 5
"""
    tree = parse(code)
    body = list(walk_body(tree.body))
    assert len(body) == 5
    assert isinstance(body[0], Assign)
    assert isinstance(body[1], Assign)
    assert isinstance(body[2], Assign)
    assert isinstance(body[3], Assign)
    assert isinstance(body[4], Assign)
