# file: tornado/util.py:131-157
# asked: {"lines": [131, 149, 150, 152, 153, 154, 155, 156, 157], "branches": [[149, 150], [149, 152]]}
# gained: {"lines": [131, 149, 150, 152, 153, 154, 155, 156, 157], "branches": [[149, 150], [149, 152]]}

import pytest
from tornado.util import import_object

def test_import_object_module():
    import tornado.escape
    assert import_object('tornado.escape') is tornado.escape

def test_import_object_submodule():
    import tornado.escape
    assert import_object('tornado.escape.utf8') is tornado.escape.utf8

def test_import_object_top_level():
    import tornado
    assert import_object('tornado') is tornado

def test_import_object_missing_module():
    with pytest.raises(ImportError, match="No module named missing_module"):
        import_object('tornado.missing_module')

def test_import_object_missing_attribute():
    with pytest.raises(ImportError, match="No module named non_existent"):
        import_object('tornado.escape.non_existent')
