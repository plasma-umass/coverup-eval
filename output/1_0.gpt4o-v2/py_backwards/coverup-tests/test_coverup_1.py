# file: py_backwards/transformers/import_pathlib.py:4-8
# asked: {"lines": [4, 5, 6, 7, 8], "branches": []}
# gained: {"lines": [4, 5, 6, 7, 8], "branches": []}

import ast
import pytest
from py_backwards.transformers.import_pathlib import ImportPathlibTransformer

def test_import_pathlib_transformer_attributes():
    tree = ast.parse("")
    transformer = ImportPathlibTransformer(tree)
    
    assert transformer.target == (3, 3)
    assert transformer.rewrites == [('pathlib', 'pathlib2')]
    assert transformer.dependencies == ['pathlib2']
