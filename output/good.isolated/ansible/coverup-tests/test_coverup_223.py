# file lib/ansible/plugins/lookup/unvault.py:41-63
# lines [41, 43, 45, 47, 49, 50, 53, 54, 55, 56, 57, 58, 59, 61, 63]
# branches ['49->50', '49->63', '55->56', '55->61']

import pytest
from ansible.errors import AnsibleParserError
from ansible.parsing.dataloader import DataLoader
from ansible.plugins.loader import lookup_loader
from ansible.utils.display import Display
from ansible.utils.unsafe_proxy import AnsibleUnsafeText

# Mock the display to avoid actual print
@pytest.fixture
def mock_display(mocker):
    mock_display = mocker.patch('ansible.plugins.lookup.unvault.Display', autospec=True)
    mock_display.debug = mocker.MagicMock()
    mock_display.vvvv = mocker.MagicMock()
    return mock_display

# Create a test for the LookupModule run method
def test_unvault_lookup_plugin(tmp_path, mocker, mock_display):
    # Create a temporary file to simulate the file to be unvaulted
    test_file = tmp_path / "test_file.txt"
    test_file.write_text(u"dummy content")

    # Mock the DataLoader and its methods
    mock_loader = mocker.MagicMock(DataLoader)
    mock_loader.get_real_file.return_value = str(test_file)

    # Mock the find_file_in_search_path method to return the test file path
    mocker.patch('ansible.plugins.lookup.unvault.LookupModule.find_file_in_search_path', return_value=str(test_file))

    # Instantiate the LookupModule
    unvault_lookup = lookup_loader.get('unvault')
    unvault_lookup._loader = mock_loader

    # Run the lookup plugin with the test term
    terms = ['test_file.txt']
    variables = {'ansible_search_path': [str(tmp_path)]}
    result = unvault_lookup.run(terms, variables)

    # Verify the result
    assert result == ["dummy content"], "The content read from the file should match 'dummy content'"

    # Verify that the DataLoader's get_real_file method was called
    mock_loader.get_real_file.assert_called_once_with(str(test_file), decrypt=True)

    # Test with a non-existent file to trigger the AnsibleParserError
    mocker.patch('ansible.plugins.lookup.unvault.LookupModule.find_file_in_search_path', return_value=None)
    with pytest.raises(AnsibleParserError):
        unvault_lookup.run(['non_existent_file.txt'], variables)

# No need to clean up after the test as there is no flush_loader method
