# file: tornado/util.py:160-167
# asked: {"lines": [160, 161, 163, 166, 167], "branches": [[163, 166], [163, 167]]}
# gained: {"lines": [160, 161, 163, 166, 167], "branches": [[163, 166], [163, 167]]}

import pytest
from types import CodeType
from tornado.util import exec_in

def test_exec_in_string_code():
    glob = {}
    loc = {}
    code = "x = 1"
    exec_in(code, glob, loc)
    assert loc['x'] == 1

def test_exec_in_code_object():
    glob = {}
    loc = {}
    code = compile("y = 2", "<string>", "exec")
    exec_in(code, glob, loc)
    assert loc['y'] == 2

def test_exec_in_with_none_loc():
    glob = {}
    code = "z = 3"
    exec_in(code, glob)
    assert glob['z'] == 3

def test_exec_in_with_future_import(monkeypatch):
    glob = {}
    loc = {}
    code = "from __future__ import division\nresult = 1 / 2"
    exec_in(code, glob, loc)
    assert loc['result'] == 0.5

def test_exec_in_with_existing_future_import(monkeypatch):
    glob = {}
    loc = {}
    code = "result = 1 / 2"
    future_code = "from __future__ import division"
    exec_in(future_code, glob, loc)
    exec_in(code, glob, loc)
    assert loc['result'] == 0.5
