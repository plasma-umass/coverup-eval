# file: lib/ansible/plugins/loader.py:149-171
# asked: {"lines": [149, 150, 151, 155, 156, 157, 159, 160, 161, 163, 165, 166, 167, 168, 169, 170, 171], "branches": [[150, 151], [150, 155], [159, 160], [159, 161], [166, 167], [166, 168], [168, 169], [168, 170]]}
# gained: {"lines": [149, 150, 151, 155, 156, 157, 159, 160, 161, 163, 165, 166, 167, 168, 169, 170, 171], "branches": [[150, 151], [150, 155], [159, 160], [159, 161], [166, 167], [166, 168], [168, 169], [168, 170]]}

import pytest
from unittest.mock import MagicMock

# Assuming the PluginLoadContext class is defined in ansible.plugins.loader
from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def mock_display_deprecated(monkeypatch):
    mock_display = MagicMock()
    monkeypatch.setattr('ansible.plugins.loader.display.deprecated', mock_display)
    return mock_display

def test_record_deprecation_no_deprecation():
    context = PluginLoadContext()
    result = context.record_deprecation('test_plugin', None, 'test_collection')
    assert result is context
    assert not context.deprecated
    assert context.removal_date is None
    assert context.removal_version is None
    assert context.deprecation_warnings == []

def test_record_deprecation_with_warning_text(mock_display_deprecated):
    context = PluginLoadContext()
    deprecation_info = {
        'warning_text': 'This is a warning',
        'removal_date': '2023-12-31',
        'removal_version': '2.0.0'
    }
    result = context.record_deprecation('test_plugin', deprecation_info, 'test_collection')
    assert result is context
    assert context.deprecated
    assert context.removal_date == '2023-12-31'
    assert context.removal_version is None  # removal_date takes precedence
    assert context.deprecation_warnings == ['test_plugin has been deprecated. This is a warning']
    mock_display_deprecated.assert_called_once_with(
        'test_plugin has been deprecated. This is a warning',
        date='2023-12-31',
        version=None,
        collection_name='test_collection'
    )

def test_record_deprecation_without_warning_text(mock_display_deprecated):
    context = PluginLoadContext()
    deprecation_info = {
        'removal_date': '2023-12-31',
        'removal_version': '2.0.0'
    }
    result = context.record_deprecation('test_plugin', deprecation_info, 'test_collection')
    assert result is context
    assert context.deprecated
    assert context.removal_date == '2023-12-31'
    assert context.removal_version is None  # removal_date takes precedence
    assert context.deprecation_warnings == ['test_plugin has been deprecated.']
    mock_display_deprecated.assert_called_once_with(
        'test_plugin has been deprecated.',
        date='2023-12-31',
        version=None,
        collection_name='test_collection'
    )

def test_record_deprecation_with_removal_version_only(mock_display_deprecated):
    context = PluginLoadContext()
    deprecation_info = {
        'removal_version': '2.0.0'
    }
    result = context.record_deprecation('test_plugin', deprecation_info, 'test_collection')
    assert result is context
    assert context.deprecated
    assert context.removal_date is None
    assert context.removal_version == '2.0.0'
    assert context.deprecation_warnings == ['test_plugin has been deprecated.']
    mock_display_deprecated.assert_called_once_with(
        'test_plugin has been deprecated.',
        date=None,
        version='2.0.0',
        collection_name='test_collection'
    )
