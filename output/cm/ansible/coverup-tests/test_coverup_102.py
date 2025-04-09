# file lib/ansible/plugins/lookup/file.py:60-87
# lines [60, 62, 64, 65, 67, 68, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 83, 84, 85, 87]
# branches ['67->68', '67->87', '74->75', '74->83', '77->78', '77->79', '79->80', '79->81']

import pytest
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.loader import lookup_loader
from ansible.utils.display import Display
from ansible.parsing.dataloader import DataLoader
from ansible.plugins.lookup import file as file_lookup

# Mock the global display object to capture its output
display = Display()
display.display = lambda *args, **kwargs: None
display.debug = lambda *args, **kwargs: None
display.vvvv = lambda *args, **kwargs: None
file_lookup.display = display

# Create a test function to improve coverage
def test_lookup_file_plugin(mocker, tmp_path):
    # Setup the mock for the find_file_in_search_path method
    mock_find_file = mocker.patch.object(file_lookup.LookupModule, 'find_file_in_search_path')
    mock_find_file.return_value = str(tmp_path / "testfile.txt")

    # Setup the mock for the _loader._get_file_contents method
    mock_get_file_contents = mocker.patch.object(DataLoader, '_get_file_contents')
    mock_get_file_contents.return_value = (b"content", False)

    # Setup the mock for the get_option method
    mock_get_option = mocker.patch.object(file_lookup.LookupModule, 'get_option')
    mock_get_option.side_effect = lambda option: True if option in ['lstrip', 'rstrip'] else None

    # Create a temporary file to be used by the lookup plugin
    test_file = tmp_path / "testfile.txt"
    test_file.write_text("  content  ")

    # Instantiate the lookup plugin
    file_lookup_plugin = lookup_loader.get('file', loader=DataLoader())

    # Run the plugin with the test term
    result = file_lookup_plugin.run([str(test_file)], variables={})

    # Assertions to verify postconditions
    assert result == ["content"], "The file content should be stripped and returned"
    assert mock_find_file.called, "The find_file_in_search_path method should be called"
    assert mock_get_file_contents.called, "The _get_file_contents method should be called"
    assert mock_get_option.called, "The get_option method should be called"

    # Cleanup is handled by pytest's tmp_path fixture automatically
