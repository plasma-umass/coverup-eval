# file lib/ansible/playbook/collectionsearch.py:34-61
# lines [43, 46, 48, 49, 55, 56, 57, 58, 59, 61]
# branches ['48->49', '48->55', '56->57', '56->61', '57->56', '57->58']

import pytest
from ansible.playbook.collectionsearch import CollectionSearch
from ansible.template import is_template
from ansible.utils.display import Display
from jinja2 import Environment

# Mocking the Display class to capture warnings
@pytest.fixture
def mock_display(mocker):
    return mocker.patch.object(Display, 'warning')

# Test function to cover lines 43-61
def test_load_collections_with_templated_name(mock_display, mocker):
    # Create an instance of CollectionSearch
    collection_search = CollectionSearch()

    # Mock the get_validated_value method to return a list with a templated collection name
    collection_search.get_validated_value = lambda *args, **kwargs: ['{{ my_collection }}']

    # Mock the _ensure_default_collection function to do nothing
    mocker.patch('ansible.playbook.collectionsearch._ensure_default_collection', return_value=None)

    # Mock the is_template function to return True for the templated collection name
    mocker.patch('ansible.template.is_template', side_effect=lambda name, env: '{{' in name and '}}' in name)

    # Call the _load_collections method
    result = collection_search._load_collections('collections', None)

    # Assert that the result is the same list that was passed in
    assert result == ['{{ my_collection }}']

    # Assert that the warning was displayed for the templated collection name
    mock_display.assert_called_once_with('"collections" is not templatable, but we found: {{ my_collection }}, '
                                         'it will not be templated and will be used "as is".')

# No teardown function is required as pytest-mock handles cleanup
