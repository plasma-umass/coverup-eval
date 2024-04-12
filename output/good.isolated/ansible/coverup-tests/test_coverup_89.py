# file lib/ansible/playbook/playbook_include.py:157-184
# lines [157, 162, 163, 164, 165, 169, 170, 171, 173, 174, 175, 176, 179, 180, 181, 182, 183, 184]
# branches ['162->163', '162->164', '164->165', '164->169', '170->171', '170->173', '174->exit', '174->175', '180->181', '180->182', '182->183', '182->184']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.playbook_include import PlaybookInclude
from ansible.module_utils.six import string_types
from ansible.utils.display import Display
from ansible.parsing.splitter import split_args
from ansible.parsing.mod_args import parse_kv

# Mock the display object to capture deprecation warnings
@pytest.fixture
def mock_display(mocker):
    display = Display()
    mocker.patch('ansible.playbook.playbook_include.display', new=display)
    return display

# Test function to cover the missing branches
def test_preprocess_import_deprecation_warning_and_vars_error(mock_display, mocker):
    playbook_include = PlaybookInclude()

    # Test data simulating a playbook import with additional parameters
    ds = {'import_playbook': 'playbook.yml extra_var=value'}
    new_ds = {'vars': {'some_var': 'some_value'}}
    k = 'import_playbook'
    v = 'playbook.yml extra_var=value'

    # Mock the deprecated method to capture its call
    mock_deprecated = mocker.patch.object(mock_display, 'deprecated')

    # Expecting a deprecation warning for additional parameters
    with pytest.raises(AnsibleParserError) as excinfo:
        playbook_include._preprocess_import(ds, new_ds, k, v)
    assert "import_playbook parameters cannot be mixed with 'vars' entries for import statements" in str(excinfo.value)

    # Check that the deprecation warning was displayed
    mock_deprecated.assert_called_once_with(
        "Additional parameters in import_playbook statements are deprecated. "
        "Use 'vars' instead. See 'import_playbook' documentation for examples.",
        version='2.14'
    )

    # Check that the 'import_playbook' key was set correctly
    assert new_ds['import_playbook'] == 'playbook.yml'

    # Check that the 'vars' key was not set due to the error
    assert 'vars' in new_ds
