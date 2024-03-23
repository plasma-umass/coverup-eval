# file py_backwards/transformers/import_pathlib.py:4-8
# lines [4, 5, 6, 7, 8]
# branches []

import pytest
from py_backwards.transformers.import_pathlib import ImportPathlibTransformer
from typed_ast import ast3

def test_import_pathlib_transformer(mocker):
    # Mock the sys.version_info to simulate the environment
    mocker.patch('sys.version_info', (3, 3))

    # Create a dummy ast tree
    tree = ast3.parse('')

    transformer = ImportPathlibTransformer(tree=tree)

    # Check if the transformer's target is correctly set
    assert transformer.target == (3, 3)

    # Check if the rewrites are correctly set
    assert transformer.rewrites == [('pathlib', 'pathlib2')]

    # Check if the dependencies are correctly set
    assert transformer.dependencies == ['pathlib2']
