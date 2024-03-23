# file tornado/util.py:338-352
# lines [338, 339, 342, 346, 347, 348, 349, 352]
# branches ['346->347', '346->348', '348->349', '348->352']

import pytest
from tornado.util import Configurable

class DefaultConfigurable(Configurable):
    pass

class TestConfigurable:
    def test_configured_class(self, mocker):
        # Mock the configurable_base method to return the DefaultConfigurable class
        mocker.patch.object(Configurable, 'configurable_base', return_value=DefaultConfigurable)
        # Mock the configurable_default method to return the DefaultConfigurable class
        mocker.patch.object(Configurable, 'configurable_default', return_value=DefaultConfigurable)
        
        # Call the method under test
        configured_cls = Configurable.configured_class()
        
        # Assert that the configured class is indeed DefaultConfigurable
        assert configured_cls is DefaultConfigurable

    def test_configured_class_with_no_impl(self, mocker):
        # Mock the configurable_base method to return a new class with no __impl_class
        mocker.patch.object(Configurable, 'configurable_base', return_value=type('NewBase', (Configurable,), {}))
        # Mock the configurable_default method to return None
        mocker.patch.object(Configurable, 'configurable_default', return_value=None)
        
        # Assert that ValueError is raised when __impl_class is None
        with pytest.raises(ValueError, match="configured class not found"):
            Configurable.configured_class()
