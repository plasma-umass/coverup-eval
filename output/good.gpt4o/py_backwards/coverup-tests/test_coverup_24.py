# file py_backwards/transformers/six_moves.py:209-213
# lines [209, 210, 211, 212, 213]
# branches []

import pytest
from py_backwards.transformers.six_moves import SixMovesTransformer
from py_backwards.transformers.base import BaseImportRewrite

def test_six_moves_transformer_rewrites():
    # Ensure the class inherits from BaseImportRewrite
    assert issubclass(SixMovesTransformer, BaseImportRewrite)
    
    # Ensure the target attribute is correct
    assert SixMovesTransformer.target == (2, 7)
    
    # Ensure the rewrites attribute is populated
    assert isinstance(SixMovesTransformer.rewrites, list)
    assert len(SixMovesTransformer.rewrites) > 0
    assert all(isinstance(item, tuple) and len(item) == 2 for item in SixMovesTransformer.rewrites)
    
    # Ensure the dependencies attribute is correct
    assert SixMovesTransformer.dependencies == ['six']
