# file: tornado/util.py:321-336
# asked: {"lines": [321, 322, 330, 331, 332, 333, 334, 335, 336], "branches": [[331, 332], [331, 333], [333, 334], [333, 335]]}
# gained: {"lines": [321, 322, 330, 331, 332, 333, 334, 335, 336], "branches": [[331, 332], [331, 333], [333, 334], [333, 335]]}

import pytest
from tornado.util import Configurable, import_object

class DummyConfigurable(Configurable):
    @classmethod
    def configurable_base(cls):
        return cls

def test_configure_with_class():
    class ImplClass(DummyConfigurable):
        pass

    DummyConfigurable.configure(ImplClass, foo='bar')
    assert DummyConfigurable.configurable_base().__dict__.get('_Configurable__impl_class') == ImplClass
    assert DummyConfigurable.configurable_base().__dict__.get('_Configurable__impl_kwargs') == {'foo': 'bar'}

def test_configure_with_string(monkeypatch):
    class ImplClass(DummyConfigurable):
        pass

    def mock_import_object(name):
        return ImplClass

    monkeypatch.setattr('tornado.util.import_object', mock_import_object)
    DummyConfigurable.configure('some.module.ImplClass', foo='bar')
    assert DummyConfigurable.configurable_base().__dict__.get('_Configurable__impl_class') == ImplClass
    assert DummyConfigurable.configurable_base().__dict__.get('_Configurable__impl_kwargs') == {'foo': 'bar'}

def test_configure_with_invalid_class():
    class NotAConfigurable:
        pass

    with pytest.raises(ValueError, match="Invalid subclass of"):
        DummyConfigurable.configure(NotAConfigurable)

def test_configure_with_none():
    DummyConfigurable.configure(None, foo='bar')
    assert DummyConfigurable.configurable_base().__dict__.get('_Configurable__impl_class') is None
    assert DummyConfigurable.configurable_base().__dict__.get('_Configurable__impl_kwargs') == {'foo': 'bar'}
