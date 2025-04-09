# file lib/ansible/plugins/lookup/csvfile.py:136-180
# lines [136, 138, 140, 143, 145, 146, 148, 149, 151, 154, 155, 156, 157, 158, 159, 161, 162, 164, 165, 168, 169, 171, 172, 173, 174, 175, 176, 178, 180]
# branches ['145->146', '145->180', '148->149', '148->151', '155->156', '155->168', '156->157', '156->158', '158->159', '158->161', '168->169', '168->171', '173->145', '173->174', '174->175', '174->178', '175->145', '175->176']

import pytest
from ansible.errors import AnsibleError, AnsibleAssertionError
from ansible.plugins.lookup.csvfile import LookupModule
from ansible.parsing.splitter import parse_kv
from collections.abc import MutableSequence

@pytest.fixture
def lookup_module(mocker):
    mocker.patch('ansible.plugins.lookup.csvfile.LookupModule._load_name', 'csvfile', create=True)
    mocker.patch('ansible.plugins.lookup.csvfile.LookupModule.find_file_in_search_path', return_value='dummy_path')
    mocker.patch('ansible.plugins.lookup.csvfile.LookupModule.read_csv', return_value='value')
    mocker.patch('ansible.plugins.lookup.csvfile.LookupModule._deprecate_inline_kv')
    lookup = LookupModule()
    mocker.patch.object(lookup, '_templar', create=True)
    return lookup

def test_lookup_csvfile_invalid_option(lookup_module, mocker):
    # Mock the get_options method to return a dictionary with options
    mocker.patch.object(lookup_module, 'get_options', return_value={'file': 'dummy.csv', 'delimiter': ',', 'encoding': 'utf-8', 'default': None, 'col': 1})

    # Define a term with an invalid option
    term = "search_key invalid_option=value"

    # Expect AnsibleError because 'invalid_option' is not a valid option and it will be caught and re-raised as AnsibleError
    with pytest.raises(AnsibleError):
        lookup_module.run([term], variables=None)

def test_lookup_csvfile_missing_search_key(lookup_module, mocker):
    # Mock the get_options method to return a dictionary with options
    mocker.patch.object(lookup_module, 'get_options', return_value={'file': 'dummy.csv', 'delimiter': ',', 'encoding': 'utf-8', 'default': None, 'col': 1})

    # Define a term without a search key
    term = "invalid_option=value"

    # Expect AnsibleError because '_raw_params' (search key) is missing
    with pytest.raises(AnsibleError):
        lookup_module.run([term], variables=None)

def test_lookup_csvfile_with_tab_delimiter(lookup_module, mocker):
    # Mock the get_options method to return a dictionary with options including 'TAB' as delimiter
    mocker.patch.object(lookup_module, 'get_options', return_value={'file': 'dummy.csv', 'delimiter': 'TAB', 'encoding': 'utf-8', 'default': None, 'col': 1})

    # Define a term with a valid search key
    term = "search_key"

    # Run the lookup plugin
    result = lookup_module.run([term], variables=None)

    # Assert that the delimiter was converted to "\t"
    assert lookup_module.get_options()['delimiter'] == "\t", "Delimiter 'TAB' should be converted to '\\t'"

    # Assert that the result is as expected
    assert result == ['value'], "Expected result is a list with a single 'value'"
