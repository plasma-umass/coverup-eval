# file: py_backwards/transformers/six_moves.py:209-213
# asked: {"lines": [209, 210, 211, 212, 213], "branches": []}
# gained: {"lines": [209, 210, 211, 212, 213], "branches": []}

import pytest
from py_backwards.transformers.six_moves import SixMovesTransformer

def test_six_moves_transformer_target():
    assert SixMovesTransformer.target == (2, 7)

def test_six_moves_transformer_rewrites():
    rewrites = SixMovesTransformer.rewrites
    assert isinstance(rewrites, list)
    assert len(rewrites) > 0
    assert all(isinstance(item, tuple) and len(item) == 2 for item in rewrites)

def test_six_moves_transformer_dependencies():
    assert SixMovesTransformer.dependencies == ['six']
