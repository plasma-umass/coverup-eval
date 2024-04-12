# file lib/ansible/plugins/loader.py:761-770
# lines [764, 765, 766, 767, 768, 770]
# branches ['767->768', '767->770']

import pytest
from ansible.errors import AnsibleError
from ansible.utils.display import Display
from ansible.plugins.loader import PluginLoader, get_plugin_class

# Mock the Display class to capture debug output
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'debug')

# Test function to cover lines 764-770
def test_has_plugin_exception_handling(mocker, mock_display):
    # Mock the get_plugin_class method to return a dummy class
    mocker.patch('ansible.plugins.loader.get_plugin_class', return_value=type('DummyPluginClass', (object,), {}))

    # Create a mock PluginLoader instance with the necessary attributes
    mock_loader = PluginLoader(
        class_name='DummyPluginClass',
        package='dummy_package',
        config={},
        subdir='dummy_subdir'
    )

    # Mock the find_plugin method to raise a non-AnsibleError exception
    mocker.patch.object(PluginLoader, 'find_plugin', side_effect=Exception('Test exception'))

    # Assert that has_plugin returns False when an exception is raised
    assert not mock_loader.has_plugin('nonexistent_plugin')

    # Assert that the debug method was called with the expected message
    mock_display.assert_called_once_with('has_plugin error: Test exception')

    # Now test that an AnsibleError is raised and not caught
    mocker.patch.object(PluginLoader, 'find_plugin', side_effect=AnsibleError('Ansible exception'))

    with pytest.raises(AnsibleError):
        mock_loader.has_plugin('nonexistent_plugin')
