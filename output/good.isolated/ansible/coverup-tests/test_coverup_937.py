# file lib/ansible/plugins/loader.py:238-239
# lines [238, 239]
# branches []

import pytest
from ansible.plugins.loader import PluginLoader
from ansible.utils.collection_loader import AnsibleCollectionRef
from unittest.mock import MagicMock

# Assuming that the PluginLoader class has an __init__ method that accepts `class_name`, `package`, and `config` as parameters.
# If not, the test will need to be adjusted to match the actual signature of PluginLoader.

@pytest.fixture
def plugin_loader_cleanup(mocker):
    # Mocking AnsibleCollectionRef to avoid side effects
    mocker.patch.object(AnsibleCollectionRef, 'legacy_plugin_dir_to_plugin_type')

    # Cleanup code if necessary, e.g., resetting class variables or state
    yield
    # No cleanup actions needed for this example

def test_plugin_loader_repr(plugin_loader_cleanup):
    # Setup
    test_subdir = 'test_subdir'
    expected_plugin_type = 'test_plugin_type'
    AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type.return_value = expected_plugin_type

    # Mocking the __init__ method to avoid needing to pass the required arguments
    PluginLoader.__init__ = MagicMock(return_value=None)
    loader = PluginLoader()
    loader.subdir = test_subdir  # Manually setting the subdir attribute

    # Exercise
    repr_string = repr(loader)

    # Verify
    assert repr_string == 'PluginLoader(type={})'.format(expected_plugin_type)
    AnsibleCollectionRef.legacy_plugin_dir_to_plugin_type.assert_called_once_with(test_subdir)

    # Cleanup is handled by the plugin_loader_cleanup fixture
