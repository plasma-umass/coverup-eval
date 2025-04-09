# file: lib/ansible/plugins/loader.py:878-992
# asked: {"lines": [919, 938, 941, 954, 959, 960, 961, 967, 968, 969, 974, 976, 977, 978, 979, 980, 981, 988, 989], "branches": [[918, 919], [936, 938], [940, 941], [951, 954], [971, 974], [980, 981], [980, 983]]}
# gained: {"lines": [919, 941, 967, 968, 969], "branches": [[918, 919], [940, 941]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.errors import AnsibleError
from ansible.plugins.loader import PluginLoader

@pytest.fixture
def plugin_loader():
    return PluginLoader(class_name='TestPlugin', package='ansible.plugins.test', config=None, subdir='test_plugins')

def test_all_path_only(plugin_loader, monkeypatch):
    monkeypatch.setattr(plugin_loader, '_get_paths', lambda: ['/fake/path'])
    monkeypatch.setattr('glob.glob', lambda x: ['/fake/path/plugin1.py', '/fake/path/plugin2.py'])
    monkeypatch.setattr('os.path.basename', lambda x: x.split('/')[-1])
    monkeypatch.setattr('os.path.splitext', lambda x: (x.split('.')[0], '.py'))
    monkeypatch.setattr('ansible.plugins.loader._PLUGIN_FILTERS', {'ansible.plugins.test': []})

    paths = list(plugin_loader.all(path_only=True))
    assert paths == ['/fake/path/plugin1.py', '/fake/path/plugin2.py']

def test_all_class_only(plugin_loader, monkeypatch):
    monkeypatch.setattr(plugin_loader, '_get_paths', lambda: ['/fake/path'])
    monkeypatch.setattr('glob.glob', lambda x: ['/fake/path/plugin1.py'])
    monkeypatch.setattr('os.path.basename', lambda x: x.split('/')[-1])
    monkeypatch.setattr('os.path.splitext', lambda x: (x.split('.')[0], '.py'))
    monkeypatch.setattr('ansible.plugins.loader._PLUGIN_FILTERS', {'ansible.plugins.test': []})
    monkeypatch.setattr(plugin_loader, '_load_module_source', lambda name, path: MagicMock())
    monkeypatch.setattr(plugin_loader, '_load_config_defs', lambda name, module, path: None)
    monkeypatch.setattr(plugin_loader, '_update_object', lambda obj, name, path: None)
    monkeypatch.setattr(plugin_loader, '_display_plugin_load', lambda *args, **kwargs: None)
    mock_module = MagicMock()
    mock_module.TestPlugin = MagicMock()
    plugin_loader._module_cache['/fake/path/plugin1.py'] = mock_module

    classes = list(plugin_loader.all(class_only=True))
    assert len(classes) == 1
    assert isinstance(classes[0], MagicMock)

def test_all_dedupe(plugin_loader, monkeypatch):
    monkeypatch.setattr(plugin_loader, '_get_paths', lambda: ['/fake/path'])
    monkeypatch.setattr('glob.glob', lambda x: ['/fake/path/plugin1.py', '/fake/path/plugin1.py'])
    monkeypatch.setattr('os.path.basename', lambda x: x.split('/')[-1])
    monkeypatch.setattr('os.path.splitext', lambda x: (x.split('.')[0], '.py'))
    monkeypatch.setattr('ansible.plugins.loader._PLUGIN_FILTERS', {'ansible.plugins.test': []})
    monkeypatch.setattr(plugin_loader, '_load_module_source', lambda name, path: MagicMock())
    monkeypatch.setattr(plugin_loader, '_load_config_defs', lambda name, module, path: None)
    monkeypatch.setattr(plugin_loader, '_update_object', lambda obj, name, path: None)
    monkeypatch.setattr(plugin_loader, '_display_plugin_load', lambda *args, **kwargs: None)
    mock_module = MagicMock()
    mock_module.TestPlugin = MagicMock()
    plugin_loader._module_cache['/fake/path/plugin1.py'] = mock_module

    plugins = list(plugin_loader.all())
    assert len(plugins) == 1

def test_all_no_dedupe(plugin_loader, monkeypatch):
    monkeypatch.setattr(plugin_loader, '_get_paths', lambda: ['/fake/path'])
    monkeypatch.setattr('glob.glob', lambda x: ['/fake/path/plugin1.py', '/fake/path/plugin1.py'])
    monkeypatch.setattr('os.path.basename', lambda x: x.split('/')[-1])
    monkeypatch.setattr('os.path.splitext', lambda x: (x.split('.')[0], '.py'))
    monkeypatch.setattr('ansible.plugins.loader._PLUGIN_FILTERS', {'ansible.plugins.test': []})
    monkeypatch.setattr(plugin_loader, '_load_module_source', lambda name, path: MagicMock())
    monkeypatch.setattr(plugin_loader, '_load_config_defs', lambda name, module, path: None)
    monkeypatch.setattr(plugin_loader, '_update_object', lambda obj, name, path: None)
    monkeypatch.setattr(plugin_loader, '_display_plugin_load', lambda *args, **kwargs: None)
    mock_module = MagicMock()
    mock_module.TestPlugin = MagicMock()
    plugin_loader._module_cache['/fake/path/plugin1.py'] = mock_module

    plugins = list(plugin_loader.all(_dedupe=False))
    assert len(plugins) == 2

def test_all_invalid_plugin(plugin_loader, monkeypatch):
    monkeypatch.setattr(plugin_loader, '_get_paths', lambda: ['/fake/path'])
    monkeypatch.setattr('glob.glob', lambda x: ['/fake/path/plugin1.py'])
    monkeypatch.setattr('os.path.basename', lambda x: x.split('/')[-1])
    monkeypatch.setattr('os.path.splitext', lambda x: (x.split('.')[0], '.py'))
    monkeypatch.setattr('ansible.plugins.loader._PLUGIN_FILTERS', {'ansible.plugins.test': []})
    monkeypatch.setattr(plugin_loader, '_load_module_source', lambda name, path: MagicMock())
    monkeypatch.setattr(plugin_loader, '_load_config_defs', lambda name, module, path: None)
    monkeypatch.setattr(plugin_loader, '_update_object', lambda obj, name, path: None)
    monkeypatch.setattr(plugin_loader, '_display_plugin_load', lambda *args, **kwargs: None)
    mock_module = MagicMock()
    del mock_module.TestPlugin
    plugin_loader._module_cache['/fake/path/plugin1.py'] = mock_module

    plugins = list(plugin_loader.all())
    assert len(plugins) == 0

def test_all_path_and_class_only(plugin_loader):
    with pytest.raises(AnsibleError, match='Do not set both path_only and class_only when calling PluginLoader.all()'):
        list(plugin_loader.all(path_only=True, class_only=True))
