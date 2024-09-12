# file: lib/ansible/plugins/loader.py:149-171
# asked: {"lines": [150, 151, 155, 156, 157, 159, 160, 161, 163, 165, 166, 167, 168, 169, 170, 171], "branches": [[150, 151], [150, 155], [159, 160], [159, 161], [166, 167], [166, 168], [168, 169], [168, 170]]}
# gained: {"lines": [150, 151, 155, 156, 157, 159, 160, 161, 163, 165, 166, 167, 168, 169, 170, 171], "branches": [[150, 151], [150, 155], [159, 160], [159, 161], [166, 167], [166, 168], [168, 169], [168, 170]]}

import pytest
from unittest.mock import MagicMock

# Assuming the PluginLoadContext class is defined in ansible.plugins.loader
from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def plugin_load_context():
    return PluginLoadContext()

def test_record_deprecation_no_deprecation(plugin_load_context):
    result = plugin_load_context.record_deprecation('test_plugin', None, 'test_collection')
    assert result is plugin_load_context
    assert not plugin_load_context.deprecated
    assert plugin_load_context.removal_date is None
    assert plugin_load_context.removal_version is None
    assert len(plugin_load_context.deprecation_warnings) == 0

def test_record_deprecation_with_deprecation_date(monkeypatch, plugin_load_context):
    mock_display = MagicMock()
    monkeypatch.setattr('ansible.plugins.loader.display', mock_display)
    
    deprecation_info = {
        'warning_text': 'This is a warning',
        'removal_date': '2023-12-31'
    }
    result = plugin_load_context.record_deprecation('test_plugin', deprecation_info, 'test_collection')
    
    assert result is plugin_load_context
    assert plugin_load_context.deprecated
    assert plugin_load_context.removal_date == '2023-12-31'
    assert plugin_load_context.removal_version is None
    assert len(plugin_load_context.deprecation_warnings) == 1
    assert 'test_plugin has been deprecated. This is a warning' in plugin_load_context.deprecation_warnings
    mock_display.deprecated.assert_called_once_with(
        'test_plugin has been deprecated. This is a warning',
        date='2023-12-31',
        version=None,
        collection_name='test_collection'
    )

def test_record_deprecation_with_deprecation_version(monkeypatch, plugin_load_context):
    mock_display = MagicMock()
    monkeypatch.setattr('ansible.plugins.loader.display', mock_display)
    
    deprecation_info = {
        'warning_text': 'This is a warning',
        'removal_version': '2.0.0'
    }
    result = plugin_load_context.record_deprecation('test_plugin', deprecation_info, 'test_collection')
    
    assert result is plugin_load_context
    assert plugin_load_context.deprecated
    assert plugin_load_context.removal_date is None
    assert plugin_load_context.removal_version == '2.0.0'
    assert len(plugin_load_context.deprecation_warnings) == 1
    assert 'test_plugin has been deprecated. This is a warning' in plugin_load_context.deprecation_warnings
    mock_display.deprecated.assert_called_once_with(
        'test_plugin has been deprecated. This is a warning',
        date=None,
        version='2.0.0',
        collection_name='test_collection'
    )

def test_record_deprecation_with_empty_warning_text(monkeypatch, plugin_load_context):
    mock_display = MagicMock()
    monkeypatch.setattr('ansible.plugins.loader.display', mock_display)
    
    deprecation_info = {
        'warning_text': None,
        'removal_date': '2023-12-31'
    }
    result = plugin_load_context.record_deprecation('test_plugin', deprecation_info, 'test_collection')
    
    assert result is plugin_load_context
    assert plugin_load_context.deprecated
    assert plugin_load_context.removal_date == '2023-12-31'
    assert plugin_load_context.removal_version is None
    assert len(plugin_load_context.deprecation_warnings) == 1
    assert 'test_plugin has been deprecated.' in plugin_load_context.deprecation_warnings
    mock_display.deprecated.assert_called_once_with(
        'test_plugin has been deprecated.',
        date='2023-12-31',
        version=None,
        collection_name='test_collection'
    )
