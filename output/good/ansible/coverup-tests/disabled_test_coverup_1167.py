# file lib/ansible/playbook/playbook_include.py:157-184
# lines [162, 163, 164, 165, 169, 170, 171, 173, 174, 175, 176, 179, 180, 181, 182, 183, 184]
# branches ['162->163', '162->164', '164->165', '164->169', '170->171', '170->173', '174->exit', '174->175', '180->181', '180->182', '182->183', '182->184']

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.playbook_include import PlaybookInclude
from ansible.module_utils.six import string_types
from ansible.utils.vars import combine_vars
from ansible.template import Templar
from ansible.parsing.splitter import split_args
from ansible.parsing.dataloader import DataLoader
from ansible.parsing.mod_args import parse_kv
from ansible.utils.display import Display

# Mock the display object to prevent actual deprecation warnings during the test
@pytest.fixture
def mock_display(mocker):
    display = Display()
    mocker.patch('ansible.playbook.playbook_include.display', new=display)
    return display

@pytest.fixture
def playbook_include():
    return PlaybookInclude()

def test_preprocess_import_missing_parameter(playbook_include):
    with pytest.raises(AnsibleParserError) as excinfo:
        playbook_include._preprocess_import({}, {}, 'import_playbook', None)
    assert "playbook import parameter is missing" in str(excinfo.value)

def test_preprocess_import_invalid_parameter_type(playbook_include):
    with pytest.raises(AnsibleParserError) as excinfo:
        playbook_include._preprocess_import({}, {}, 'import_playbook', 123)
    assert "playbook import parameter must be a string indicating a file path" in str(excinfo.value)

def test_preprocess_import_empty_filename(playbook_include):
    with pytest.raises(AnsibleParserError) as excinfo:
        playbook_include._preprocess_import({}, {}, 'import_playbook', '')
    assert "import_playbook statements must specify the file name to import" in str(excinfo.value)

def test_preprocess_import_deprecated_parameters(playbook_include, mock_display, mocker):
    new_ds = {}
    mocker.spy(mock_display, 'deprecated')
    playbook_include._preprocess_import({}, new_ds, 'import_playbook', 'playbook.yml extra_var=value')
    assert new_ds['import_playbook'] == 'playbook.yml'
    assert new_ds['vars'] == {'extra_var': 'value'}
    mock_display.deprecated.assert_called_once_with(
        "Additional parameters in import_playbook statements are deprecated. "
        "Use 'vars' instead. See 'import_playbook' documentation for examples.", version='2.14'
    )

def test_preprocess_import_vars_conflict(playbook_include):
    new_ds = {'vars': {'existing_var': 'value'}}
    with pytest.raises(AnsibleParserError) as excinfo:
        playbook_include._preprocess_import({}, new_ds, 'import_playbook', 'playbook.yml extra_var=value')
    assert "import_playbook parameters cannot be mixed with 'vars' entries for import statements" in str(excinfo.value)
