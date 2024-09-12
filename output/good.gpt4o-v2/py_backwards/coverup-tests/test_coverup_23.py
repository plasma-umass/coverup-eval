# file: py_backwards/transformers/six_moves.py:209-213
# asked: {"lines": [209, 210, 211, 212, 213], "branches": []}
# gained: {"lines": [209, 210, 211, 212, 213], "branches": []}

import pytest
from py_backwards.transformers.six_moves import SixMovesTransformer

def test_six_moves_transformer_target():
    assert SixMovesTransformer.target == (2, 7)

def test_six_moves_transformer_rewrites():
    rewrites = list(SixMovesTransformer.rewrites)
    assert len(rewrites) > 0  # Ensure that rewrites are populated
    for rewrite in rewrites:
        assert isinstance(rewrite, tuple)
        assert len(rewrite) == 2
        assert rewrite[0].startswith('six.moves') or rewrite[1].startswith('six.moves')

def test_six_moves_transformer_dependencies():
    assert SixMovesTransformer.dependencies == ['six']
