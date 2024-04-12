# file tornado/util.py:131-157
# lines [131, 149, 150, 152, 153, 154, 155, 156, 157]
# branches ['149->150', '149->152']

import pytest
from tornado.util import import_object

def test_import_object():
    # Test importing a module
    import math
    assert import_object('math') is math

    # Test importing a symbol from a module
    from math import cos
    assert import_object('math.cos') is cos

    # Test importing a submodule
    import os.path
    assert import_object('os.path') is os.path

    # Test importing a symbol from a submodule
    from os.path import abspath
    assert import_object('os.path.abspath') is abspath

    # Test importing a missing module
    with pytest.raises(ImportError):
        import_object('tornado.missing_module')

    # Test importing a missing symbol from an existing module
    with pytest.raises(ImportError):
        import_object('math.missing_symbol')

# Clean up is not necessary as the import_object function does not modify any state
