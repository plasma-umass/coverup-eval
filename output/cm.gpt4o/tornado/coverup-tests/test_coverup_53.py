# file tornado/util.py:321-336
# lines [321, 322, 330, 331, 332, 333, 334, 335, 336]
# branches ['331->332', '331->333', '333->334', '333->335']

import pytest
from tornado.util import Configurable
import typing

class TestConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return cls

def test_configurable_configure_with_string(mocker):
    mock_import_object = mocker.patch('tornado.util.import_object', return_value=TestConfigurable)
    TestConfigurable.configure('some.module.TestConfigurable', some_arg='some_value')
    
    base = TestConfigurable.configurable_base()
    assert getattr(base, '_Configurable__impl_class') == TestConfigurable
    assert getattr(base, '_Configurable__impl_kwargs') == {'some_arg': 'some_value'}
    mock_import_object.assert_called_once_with('some.module.TestConfigurable')

def test_configurable_configure_with_class():
    TestConfigurable.configure(TestConfigurable, some_arg='some_value')
    
    base = TestConfigurable.configurable_base()
    assert getattr(base, '_Configurable__impl_class') == TestConfigurable
    assert getattr(base, '_Configurable__impl_kwargs') == {'some_arg': 'some_value'}

def test_configurable_configure_with_invalid_class():
    class InvalidClass:
        pass
    
    with pytest.raises(ValueError, match="Invalid subclass of <class '.*TestConfigurable'>"):
        TestConfigurable.configure(InvalidClass)
