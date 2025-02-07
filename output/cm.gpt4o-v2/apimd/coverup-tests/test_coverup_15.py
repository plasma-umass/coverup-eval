# file: apimd/parser.py:418-449
# asked: {"lines": [418, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449], "branches": [[424, 425], [424, 428], [431, 432], [431, 433], [433, 434], [433, 435], [439, 440], [439, 442]]}
# gained: {"lines": [418, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 435, 436, 437, 438, 439, 440, 441, 442, 443, 444, 445, 446, 447, 448, 449], "branches": [[424, 425], [431, 432], [439, 440]]}

import pytest
from ast import arguments, arg, expr, Constant
from typing import Optional
from unittest.mock import MagicMock
from apimd.parser import Parser

@pytest.fixture
def parser():
    return Parser()

def test_func_api_full_coverage(parser, mocker):
    # Mocking the self.doc dictionary
    parser.doc = {"test_func": ""}

    # Mocking the func_ann method
    mocker.patch.object(parser, 'func_ann', return_value=iter(["annotation1", "annotation2"]))

    # Creating a sample arguments node
    node = arguments(
        posonlyargs=[arg(arg='posonly1', annotation=None)],
        args=[arg(arg='arg1', annotation=None)],
        vararg=arg(arg='vararg1', annotation=None),
        kwonlyargs=[arg(arg='kwonly1', annotation=None)],
        kw_defaults=[None],
        kwarg=arg(arg='kwarg1', annotation=None),
        defaults=[Constant(value=42)]
    )

    # Calling the func_api method
    parser.func_api(
        root="root",
        name="test_func",
        node=node,
        returns=Constant(value="return_annotation"),
        has_self=True,
        cls_method=False
    )

    # Assertions to verify the expected behavior
    assert "test_func" in parser.doc
    assert parser.doc["test_func"] != ""

    # Clean up
    del parser.doc["test_func"]
