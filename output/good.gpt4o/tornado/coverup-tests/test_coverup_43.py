# file tornado/util.py:131-157
# lines [131, 149, 150, 152, 153, 154, 155, 156, 157]
# branches ['149->150', '149->152']

import pytest
from tornado.util import import_object

def test_import_object():
    # Test importing a module
    import tornado.escape
    assert import_object('tornado.escape') is tornado.escape

    # Test importing an attribute from a module
    assert import_object('tornado.escape.utf8') is tornado.escape.utf8

    # Test importing a top-level module
    import tornado
    assert import_object('tornado') is tornado

    # Test importing a non-existent module
    with pytest.raises(ImportError, match="No module named missing_module"):
        import_object('tornado.missing_module')

    # Test importing a non-existent attribute from an existing module
    with pytest.raises(ImportError, match="No module named non_existent"):
        import_object('tornado.escape.non_existent')
