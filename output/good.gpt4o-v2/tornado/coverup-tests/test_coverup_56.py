# file: tornado/util.py:321-336
# asked: {"lines": [321, 322, 330, 331, 332, 333, 334, 335, 336], "branches": [[331, 332], [331, 333], [333, 334], [333, 335]]}
# gained: {"lines": [321, 322, 330, 331, 332, 333, 334, 335, 336], "branches": [[331, 332], [331, 333], [333, 334], [333, 335]]}

import pytest
from unittest.mock import patch, MagicMock
from tornado.util import Configurable, import_object

class TestConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return cls

@pytest.fixture(autouse=True)
def reset_configurable():
    # Reset the Configurable class to its initial state before each test
    if hasattr(Configurable, '_Configurable__impl_class'):
        delattr(Configurable, '_Configurable__impl_class')
    if hasattr(Configurable, '_Configurable__impl_kwargs'):
        delattr(Configurable, '_Configurable__impl_kwargs')
    yield

def test_configure_with_string():
    with patch('tornado.util.import_object') as mock_import_object:
        mock_import_object.return_value = TestConfigurable
        with patch.object(Configurable, 'configurable_base', return_value=Configurable):
            Configurable.configure('tornado.util.TestConfigurable', test_kwarg='value')
            assert Configurable._Configurable__impl_class == TestConfigurable
            assert Configurable._Configurable__impl_kwargs == {'test_kwarg': 'value'}

def test_configure_with_class():
    with patch.object(Configurable, 'configurable_base', return_value=Configurable):
        Configurable.configure(TestConfigurable, test_kwarg='value')
        assert Configurable._Configurable__impl_class == TestConfigurable
        assert Configurable._Configurable__impl_kwargs == {'test_kwarg': 'value'}

def test_configure_with_invalid_class():
    class InvalidClass:
        pass

    with patch.object(Configurable, 'configurable_base', return_value=Configurable):
        with pytest.raises(ValueError, match="Invalid subclass of <class 'tornado.util.Configurable'>"):
            Configurable.configure(InvalidClass)

def test_configure_with_none():
    with patch.object(Configurable, 'configurable_base', return_value=Configurable):
        Configurable.configure(None, test_kwarg='value')
        assert Configurable._Configurable__impl_class is None
        assert Configurable._Configurable__impl_kwargs == {'test_kwarg': 'value'}
