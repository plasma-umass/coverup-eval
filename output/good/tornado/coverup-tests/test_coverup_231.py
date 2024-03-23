# file tornado/util.py:321-336
# lines [332, 334]
# branches ['331->332', '333->334']

import pytest
from tornado.util import Configurable

class MyConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return cls

def test_configure_with_invalid_subclass(mocker):
    mocker.patch('tornado.util.import_object', return_value=object)  # Patch import_object to return a non-subclass object
    with pytest.raises(ValueError) as exc_info:
        MyConfigurable.configure('not.a.real.Module')
    expected_error_message = "Invalid subclass of %s" % repr(MyConfigurable)
    assert str(exc_info.value) == expected_error_message
