# file py_backwards/transformers/base.py:112-125
# lines [118, 120, 121, 122, 124, 125]
# branches []

import ast
import pytest
from py_backwards.transformers.base import BaseImportRewrite, BaseNodeTransformer

class DummyTree:
    pass

def test_replace_import_from_names(mocker):
    # Mock the _get_replaced_import_from_part method to return a dummy value
    mocker.patch.object(BaseImportRewrite, '_get_replaced_import_from_part', return_value=ast.ImportFrom(module='dummy', names=[], level=0))
    
    # Mock the import_rewrite.get_body method to return a dummy value
    mocker.patch('py_backwards.transformers.base.import_rewrite.get_body', return_value=[ast.Try(body=[], handlers=[], orelse=[], finalbody=[])])
    
    # Create a dummy ImportFrom node
    node = ast.ImportFrom(module='dummy', names=[ast.alias(name='dummy', asname=None)], level=0)
    
    # Create a dummy names_to_replace dictionary
    names_to_replace = {'dummy': ('old_dummy', 'new_dummy')}
    
    # Instantiate the transformer with a dummy tree
    transformer = BaseImportRewrite(DummyTree())
    
    # Call the method
    result = transformer._replace_import_from_names(node, names_to_replace)
    
    # Assertions to verify the postconditions
    assert isinstance(result, ast.Try)
    assert transformer._tree_changed is True

    # Clean up
    mocker.stopall()
