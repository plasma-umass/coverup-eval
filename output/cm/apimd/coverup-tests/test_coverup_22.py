# file apimd/parser.py:74-87
# lines [74, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 87]
# branches ['76->exit', '76->77', '77->78', '77->80', '80->81', '80->87', '82->83', '82->84']

import pytest
from apimd.parser import walk_body
from ast import If, Try, Pass, ExceptHandler

@pytest.fixture
def cleanup():
    # Fixture to perform cleanup if necessary
    yield
    # Perform cleanup here if needed

def test_walk_body_with_if_and_try(cleanup):
    if_node = If(test=Pass(), body=[Pass()], orelse=[Pass()])
    try_node = Try(
        body=[Pass()],
        handlers=[ExceptHandler(type=None, name=None, body=[Pass()])],
        orelse=[Pass()],
        finalbody=[Pass()]
    )
    body = [if_node, try_node, Pass()]

    result = list(walk_body(body))

    assert len(result) == 7
    assert all(isinstance(node, Pass) for node in result)
