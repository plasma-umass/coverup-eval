# file lib/ansible/plugins/loader.py:149-171
# lines [150, 151, 155, 156, 157, 159, 160, 161, 163, 165, 166, 167, 168, 169, 170, 171]
# branches ['150->151', '150->155', '159->160', '159->161', '166->167', '166->168', '168->169', '168->170']

import pytest
from ansible.plugins.loader import PluginLoadContext

@pytest.fixture
def mock_display(mocker):
    return mocker.patch('ansible.plugins.loader.display')

def test_plugin_load_context_record_deprecation(mock_display):
    context = PluginLoadContext()
    context.deprecation_warnings = []

    # Test with empty deprecation
    result = context.record_deprecation('test_plugin', {}, 'test_collection')
    assert result == context
    assert not context.deprecated
    assert len(context.deprecation_warnings) == 0

    # Test with deprecation containing warning_text only
    deprecation = {'warning_text': 'This is deprecated.'}
    result = context.record_deprecation('test_plugin', deprecation, 'test_collection')
    assert result == context
    assert context.deprecated
    assert context.deprecation_warnings == ['test_plugin has been deprecated. This is deprecated.']
    mock_display.deprecated.assert_called_with(
        'test_plugin has been deprecated. This is deprecated.',
        date=None,
        version=None,
        collection_name='test_collection'
    )

    # Test with deprecation containing removal_date only
    deprecation = {'removal_date': '2023-12-31'}
    context.record_deprecation('test_plugin', deprecation, 'test_collection')
    assert context.removal_date == '2023-12-31'
    assert context.removal_version is None

    # Reset context for next test
    context = PluginLoadContext()
    context.deprecation_warnings = []

    # Test with deprecation containing removal_version only
    deprecation = {'removal_version': '2.10'}
    context.record_deprecation('test_plugin', deprecation, 'test_collection')
    assert context.removal_version == '2.10'
    assert context.removal_date is None

    # Reset context for next test
    context = PluginLoadContext()
    context.deprecation_warnings = []

    # Test with deprecation containing both removal_date and removal_version
    deprecation = {'removal_date': '2023-12-31', 'removal_version': '2.10'}
    context.record_deprecation('test_plugin', deprecation, 'test_collection')
    assert context.removal_date == '2023-12-31'
    assert context.removal_version is None

    # Cleanup
    mock_display.reset_mock()
