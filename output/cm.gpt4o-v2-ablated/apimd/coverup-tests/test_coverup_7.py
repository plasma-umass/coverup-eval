# file: apimd/parser.py:46-48
# asked: {"lines": [46, 48], "branches": []}
# gained: {"lines": [46, 48], "branches": []}

import pytest
from typing import Optional, Sequence
from apimd.parser import _defaults
from unittest.mock import patch

def test_defaults_all_none():
    args = [None, None, None]
    result = list(_defaults(args))
    assert result == [" ", " ", " "]

def test_defaults_mixed():
    args = [None, 1, None, 2]
    with patch('apimd.parser.unparse', side_effect=lambda x: str(x)), \
         patch('apimd.parser.code', side_effect=lambda x: f"code({x})"):
        result = list(_defaults(args))
    assert result == [" ", "code(1)", " ", "code(2)"]

def test_defaults_all_values():
    args = [1, 2, 3]
    with patch('apimd.parser.unparse', side_effect=lambda x: str(x)), \
         patch('apimd.parser.code', side_effect=lambda x: f"code({x})"):
        result = list(_defaults(args))
    assert result == ["code(1)", "code(2)", "code(3)"]
