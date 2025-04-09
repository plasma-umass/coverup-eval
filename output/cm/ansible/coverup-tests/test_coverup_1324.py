# file lib/ansible/plugins/lookup/file.py:60-87
# lines [83, 84, 85]
# branches ['74->83', '77->79', '79->81']

import pytest
from ansible.errors import AnsibleError, AnsibleParserError
from ansible.plugins.loader import lookup_loader
from ansible.utils.display import Display

# Mock the global display object to prevent output during tests
display = Display()
display.debug = lambda x: None
display.vvvv = lambda x: None

@pytest.fixture
def file_lookup(mocker):
    mocker.patch('ansible.plugins.lookup.file.Display', return_value=display)
    file_lookup = lookup_loader.get('file')
    return file_lookup

def test_lookup_file_not_found(file_lookup, mocker, tmp_path):
    # Mock the find_file_in_search_path method to return None
    mocker.patch.object(file_lookup, 'find_file_in_search_path', return_value=None)
    # Mock the _loader to prevent side effects
    mocker.patch.object(file_lookup, '_loader')
    # Set the options for lstrip and rstrip
    file_lookup.set_options(direct={'lstrip': False, 'rstrip': False})

    # Create a temporary file to use as a term
    term = str(tmp_path / "nonexistent.txt")

    # Expect AnsibleError because the file does not exist
    with pytest.raises(AnsibleError) as excinfo:
        file_lookup.run([term])

    assert "could not locate file in lookup: %s" % term in str(excinfo.value)
