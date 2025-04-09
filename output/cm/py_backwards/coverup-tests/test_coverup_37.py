# file py_backwards/transformers/base.py:54-66
# lines [56, 58, 59, 61, 62, 63, 65, 66]
# branches []

import ast
import pytest
from py_backwards.transformers.base import BaseImportRewrite
from unittest.mock import MagicMock

class DummyImportRewrite:
    @staticmethod
    def get_body(previous, current):
        return [ast.Try(
            body=[current],
            handlers=[ast.ExceptHandler(
                type=ast.Name(id='ImportError', ctx=ast.Load()),
                name=None,
                body=[previous]
            )],
            orelse=[],
            finalbody=[]
        )]

@pytest.fixture
def base_import_rewrite():
    return BaseImportRewrite(tree=MagicMock())

def test_replace_import(base_import_rewrite, mocker):
    mocker.patch('py_backwards.transformers.base.import_rewrite', new=DummyImportRewrite)
    node = ast.Import(names=[ast.alias(name='old_module', asname=None)])
    from_ = 'old_module'
    to = 'new_module'
    
    result = base_import_rewrite._replace_import(node, from_, to)
    
    assert base_import_rewrite._tree_changed is True
    assert isinstance(result, ast.Try)
    assert result.body[0].names[0].name == 'new_module'
    assert result.handlers[0].type.id == 'ImportError'
