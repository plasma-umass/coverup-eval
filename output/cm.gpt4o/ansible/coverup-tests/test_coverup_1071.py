# file lib/ansible/plugins/loader.py:149-171
# lines [150, 151, 155, 156, 157, 159, 160, 161, 163, 165, 166, 167, 168, 169, 170, 171]
# branches ['150->151', '150->155', '159->160', '159->161', '166->167', '166->168', '168->169', '168->170']

import pytest
from unittest import mock

# Assuming the PluginLoadContext class is part of the ansible.plugins.loader module
from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def plugin_load_context():
    context = PluginLoadContext()
    context.deprecation_warnings = []
    return context

def test_record_deprecation(plugin_load_context, mocker):
    # Mock the display.deprecated method
    mock_display_deprecated = mocker.patch('ansible.plugins.loader.display.deprecated')

    # Test case where deprecation is None
    result = plugin_load_context.record_deprecation('test_plugin', None, 'test_collection')
    assert result == plugin_load_context
    assert not plugin_load_context.deprecation_warnings

    # Test case where deprecation has warning_text and removal_date
    deprecation_info = {
        'warning_text': 'This is a warning',
        'removal_date': '2023-12-31'
    }
    result = plugin_load_context.record_deprecation('test_plugin', deprecation_info, 'test_collection')
    assert result == plugin_load_context
    assert plugin_load_context.deprecated is True
    assert plugin_load_context.removal_date == '2023-12-31'
    assert 'test_plugin has been deprecated. This is a warning' in plugin_load_context.deprecation_warnings
    mock_display_deprecated.assert_called_with(
        'test_plugin has been deprecated. This is a warning',
        date='2023-12-31',
        version=None,
        collection_name='test_collection'
    )

    # Test case where deprecation has warning_text and removal_version
    deprecation_info = {
        'warning_text': 'This is another warning',
        'removal_version': '2.0.0'
    }
    result = plugin_load_context.record_deprecation('test_plugin', deprecation_info, 'test_collection')
    assert result == plugin_load_context
    assert plugin_load_context.deprecated is True
    assert plugin_load_context.removal_version == '2.0.0'
    assert 'test_plugin has been deprecated. This is another warning' in plugin_load_context.deprecation_warnings
    mock_display_deprecated.assert_called_with(
        'test_plugin has been deprecated. This is another warning',
        date=None,
        version='2.0.0',
        collection_name='test_collection'
    )

    # Test case where deprecation has no warning_text
    deprecation_info = {
        'removal_date': '2023-12-31'
    }
    result = plugin_load_context.record_deprecation('test_plugin', deprecation_info, 'test_collection')
    assert result == plugin_load_context
    assert plugin_load_context.deprecated is True
    assert plugin_load_context.removal_date == '2023-12-31'
    assert 'test_plugin has been deprecated.' in plugin_load_context.deprecation_warnings
    mock_display_deprecated.assert_called_with(
        'test_plugin has been deprecated.',
        date='2023-12-31',
        version=None,
        collection_name='test_collection'
    )
