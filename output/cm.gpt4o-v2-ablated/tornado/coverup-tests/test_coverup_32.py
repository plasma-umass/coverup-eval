# file: tornado/util.py:131-157
# asked: {"lines": [131, 149, 150, 152, 153, 154, 155, 156, 157], "branches": [[149, 150], [149, 152]]}
# gained: {"lines": [131, 149, 150, 152, 153, 154, 155, 156, 157], "branches": [[149, 150], [149, 152]]}

import pytest
from tornado.util import import_object

def test_import_module():
    import tornado.escape
    assert import_object('tornado.escape') is tornado.escape

def test_import_submodule():
    import tornado.escape
    assert import_object('tornado.escape.utf8') is tornado.escape.utf8

def test_import_top_level_module():
    import tornado
    assert import_object('tornado') is tornado

def test_import_nonexistent_module():
    with pytest.raises(ImportError, match="No module named missing_module"):
        import_object('tornado.missing_module')

def test_import_nonexistent_submodule():
    with pytest.raises(ImportError, match="No module named nonexistent"):
        import_object('tornado.escape.nonexistent')
