# file lib/ansible/plugins/loader.py:878-992
# lines [919, 938, 941, 946, 947, 954, 959, 960, 961, 967, 968, 969, 974, 976, 977, 978, 979, 980, 981, 988, 989]
# branches ['918->919', '936->938', '940->941', '945->946', '951->954', '971->974', '980->981', '980->983', '985->991']

import os
import pytest
from ansible.errors import AnsibleError
from ansible.plugins.loader import PluginLoader
from ansible.utils.display import Display

# Mock the display object to capture warnings
@pytest.fixture
def mock_display(mocker):
    display = Display()
    mocker.patch.object(display, 'warning')
    return display

# Create a test function to cover the missing lines
def test_plugin_loader_all_exceptions(tmp_path, mocker, mock_display):
    # Create a dummy plugin file that will raise an exception when loaded
    plugin_dir = tmp_path / "plugins"
    plugin_dir.mkdir()
    plugin_file = plugin_dir / "dummy.py"
    plugin_file.write_text("raise Exception('test exception')")

    # Mock the _get_paths method to return the path to the dummy plugin
    mocker.patch.object(PluginLoader, '_get_paths', return_value=[str(plugin_dir)])

    # Mock the _load_module_source method to raise an exception
    mocker.patch.object(PluginLoader, '_load_module_source', side_effect=Exception('test load exception'))

    # Mock the _load_config_defs method to do nothing
    mocker.patch.object(PluginLoader, '_load_config_defs')

    # Mock the _update_object method to do nothing
    mocker.patch.object(PluginLoader, '_update_object')

    # Create a PluginLoader instance with dummy values
    loader = PluginLoader(
        class_name='DummyClass',
        package='ansible.plugins.dummy',
        config={},
        subdir=''
    )

    # Set the global _PLUGIN_FILTERS to include the dummy plugin
    mocker.patch.dict('ansible.plugins.loader._PLUGIN_FILTERS', {'ansible.plugins.dummy': set()})

    # Test path_only and class_only set at the same time
    with pytest.raises(AnsibleError):
        next(loader.all(path_only=True, class_only=True))

    # Test dedupe functionality
    list(loader.all(_dedupe=False))

    # Test path_only functionality
    paths = list(loader.all(path_only=True))
    assert str(plugin_file) in paths

    # Test class_only functionality
    mocker.patch.object(PluginLoader, '_load_module_source', return_value=mocker.MagicMock())
    classes = list(loader.all(class_only=True))
    assert len(classes) > 0

    # Test exception handling in plugin instantiation
    mocker.patch.object(PluginLoader, '_load_module_source', return_value=mocker.MagicMock(DummyClass=mocker.MagicMock(side_effect=TypeError('test type error'))))
    list(loader.all())

    # Check that warnings were displayed
    assert mock_display.warning.call_count > 0
