# file py_backwards/transformers/yield_from.py:30-33
# lines [30, 31, 32]
# branches []

import pytest
from py_backwards.transformers.yield_from import YieldFromTransformer
from unittest.mock import MagicMock

def test_yield_from_transformer_target():
    mock_tree = MagicMock()
    transformer = YieldFromTransformer(mock_tree)
    assert transformer.target == (3, 2)
