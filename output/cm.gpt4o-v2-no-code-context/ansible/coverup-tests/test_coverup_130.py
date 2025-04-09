# file: lib/ansible/plugins/loader.py:149-171
# asked: {"lines": [149, 150, 151, 155, 156, 157, 159, 160, 161, 163, 165, 166, 167, 168, 169, 170, 171], "branches": [[150, 151], [150, 155], [159, 160], [159, 161], [166, 167], [166, 168], [168, 169], [168, 170]]}
# gained: {"lines": [149], "branches": []}

import pytest
from unittest.mock import MagicMock

@pytest.fixture
def plugin_load_context():
    class PluginLoadContext:
        def __init__(self):
            self.deprecated = False
            self.removal_date = None
            self.removal_version = None
            self.deprecation_warnings = []

        def record_deprecation(self, name, deprecation, collection_name):
            if not deprecation:
                return self

            warning_text = deprecation.get('warning_text', None) or ''
            removal_date = deprecation.get('removal_date', None)
            removal_version = deprecation.get('removal_version', None)
            if removal_date is not None:
                removal_version = None
            warning_text = '{0} has been deprecated.{1}{2}'.format(name, ' ' if warning_text else '', warning_text)

            self.display.deprecated(warning_text, date=removal_date, version=removal_version, collection_name=collection_name)

            self.deprecated = True
            if removal_date:
                self.removal_date = removal_date
            if removal_version:
                self.removal_version = removal_version
            self.deprecation_warnings.append(warning_text)
            return self

    return PluginLoadContext()

@pytest.fixture
def mock_display(mocker):
    mock_display = mocker.patch('ansible.plugins.loader.display')
    return mock_display

@pytest.fixture(autouse=True)
def setup_display(plugin_load_context, mock_display):
    plugin_load_context.display = mock_display

def test_record_deprecation_no_deprecation(plugin_load_context):
    context = plugin_load_context.record_deprecation('test_plugin', None, 'test_collection')
    assert context.deprecated is False
    assert context.removal_date is None
    assert context.removal_version is None
    assert context.deprecation_warnings == []

def test_record_deprecation_with_warning_text(plugin_load_context, mock_display):
    deprecation_info = {
        'warning_text': 'This is a warning',
        'removal_date': None,
        'removal_version': '2.0'
    }
    context = plugin_load_context.record_deprecation('test_plugin', deprecation_info, 'test_collection')
    assert context.deprecated is True
    assert context.removal_date is None
    assert context.removal_version == '2.0'
    assert context.deprecation_warnings == ['test_plugin has been deprecated. This is a warning']
    mock_display.deprecated.assert_called_once_with('test_plugin has been deprecated. This is a warning', date=None, version='2.0', collection_name='test_collection')

def test_record_deprecation_with_removal_date(plugin_load_context, mock_display):
    deprecation_info = {
        'warning_text': 'This is a warning',
        'removal_date': '2023-12-31',
        'removal_version': '2.0'
    }
    context = plugin_load_context.record_deprecation('test_plugin', deprecation_info, 'test_collection')
    assert context.deprecated is True
    assert context.removal_date == '2023-12-31'
    assert context.removal_version is None
    assert context.deprecation_warnings == ['test_plugin has been deprecated. This is a warning']
    mock_display.deprecated.assert_called_once_with('test_plugin has been deprecated. This is a warning', date='2023-12-31', version=None, collection_name='test_collection')

def test_record_deprecation_with_no_warning_text(plugin_load_context, mock_display):
    deprecation_info = {
        'warning_text': None,
        'removal_date': None,
        'removal_version': '2.0'
    }
    context = plugin_load_context.record_deprecation('test_plugin', deprecation_info, 'test_collection')
    assert context.deprecated is True
    assert context.removal_date is None
    assert context.removal_version == '2.0'
    assert context.deprecation_warnings == ['test_plugin has been deprecated.']
    mock_display.deprecated.assert_called_once_with('test_plugin has been deprecated.', date=None, version='2.0', collection_name='test_collection')
