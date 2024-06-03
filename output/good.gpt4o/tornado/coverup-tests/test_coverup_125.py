# file tornado/util.py:360-365
# lines [360, 361, 363, 364, 365]
# branches []

import pytest
from unittest.mock import patch

# Assuming the Configurable class is imported from tornado.util
from tornado.util import Configurable

class TestConfigurable:
    @patch.object(Configurable, 'configurable_base')
    def test_restore_configuration(self, mock_configurable_base):
        class MockBase:
            pass

        mock_base_instance = MockBase()
        mock_configurable_base.return_value = mock_base_instance

        saved = (MockBase, {'key': 'value'})
        Configurable._restore_configuration(saved)

        assert hasattr(mock_base_instance, '_Configurable__impl_class')
        assert hasattr(mock_base_instance, '_Configurable__impl_kwargs')
        assert mock_base_instance._Configurable__impl_class == MockBase
        assert mock_base_instance._Configurable__impl_kwargs == {'key': 'value'}
