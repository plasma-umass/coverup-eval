# file: py_backwards/transformers/six_moves.py:209-213
# asked: {"lines": [209, 210, 211, 212, 213], "branches": []}
# gained: {"lines": [209, 210, 211, 212, 213], "branches": []}

import pytest
from py_backwards.transformers.six_moves import SixMovesTransformer
from py_backwards.transformers.six_moves import _get_rewrites

def test_six_moves_transformer_target():
    assert SixMovesTransformer.target == (2, 7)

def test_six_moves_transformer_rewrites():
    rewrites = list(_get_rewrites())
    assert SixMovesTransformer.rewrites == rewrites

def test_six_moves_transformer_dependencies():
    assert SixMovesTransformer.dependencies == ['six']
