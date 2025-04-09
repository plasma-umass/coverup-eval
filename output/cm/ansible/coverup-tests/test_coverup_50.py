# file lib/ansible/plugins/lookup/fileglob.py:56-83
# lines [56, 58, 60, 61, 62, 63, 64, 65, 68, 69, 71, 72, 73, 74, 76, 77, 78, 79, 80, 81, 82, 83]
# branches ['61->62', '61->83', '64->65', '64->68', '68->69', '68->71', '72->73', '72->76', '76->61', '76->77', '77->76', '77->78', '80->76', '80->81']

import os
import pytest
from ansible.plugins.lookup import fileglob
from ansible.errors import AnsibleError

def test_fileglob_lookup_with_directory_term(mocker, tmp_path):
    # Setup the environment
    directory = tmp_path / "test_dir"
    directory.mkdir()
    file = directory / "test_file.txt"
    file.touch()

    # Mock the necessary functions
    mocker.patch.object(fileglob.LookupModule, 'find_file_in_search_path', return_value=str(directory))
    mocker.patch.object(fileglob.LookupModule, 'get_basedir', return_value=str(tmp_path))
    mocker.patch('ansible.plugins.lookup.fileglob.glob.glob', return_value=[str(file)])
    mocker.patch('ansible.plugins.lookup.fileglob.os.path.isfile', return_value=True)
    mocker.patch('ansible.plugins.lookup.fileglob.to_bytes', side_effect=lambda x, **kwargs: x)
    mocker.patch('ansible.plugins.lookup.fileglob.to_text', side_effect=lambda x, **kwargs: x)

    # Create the lookup plugin instance
    lookup = fileglob.LookupModule()

    # Run the lookup plugin with a directory term
    variables = {'ansible_search_path': [str(tmp_path)]}
    result = lookup.run([str(file)], variables)

    # Verify the result
    assert result == [str(file)]

    # Cleanup
    file.unlink()
    directory.rmdir()
