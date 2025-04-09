# file: lib/ansible/playbook/playbook_include.py:157-184
# asked: {"lines": [162, 163, 164, 165, 169, 170, 171, 173, 174, 175, 176, 179, 180, 181, 182, 183, 184], "branches": [[162, 163], [162, 164], [164, 165], [164, 169], [170, 171], [170, 173], [174, 0], [174, 175], [180, 181], [180, 182], [182, 183], [182, 184]]}
# gained: {"lines": [162, 163, 164, 165, 169, 170, 171, 173, 174, 175, 176, 179, 180, 181, 182, 183, 184], "branches": [[162, 163], [162, 164], [164, 165], [164, 169], [170, 171], [170, 173], [174, 0], [174, 175], [180, 181], [180, 182], [182, 183], [182, 184]]}

import pytest
from ansible.playbook.playbook_include import PlaybookInclude
from ansible.errors import AnsibleParserError
from ansible.utils.display import Display
from ansible.utils.vars import parse_kv
from ansible.module_utils.six import string_types

@pytest.fixture
def playbook_include():
    return PlaybookInclude()

def test_preprocess_import_none_value(playbook_include):
    ds = {}
    new_ds = {}
    with pytest.raises(AnsibleParserError, match="playbook import parameter is missing"):
        playbook_include._preprocess_import(ds, new_ds, 'import_playbook', None)

def test_preprocess_import_non_string_value(playbook_include):
    ds = {}
    new_ds = {}
    with pytest.raises(AnsibleParserError, match="playbook import parameter must be a string indicating a file path"):
        playbook_include._preprocess_import(ds, new_ds, 'import_playbook', 123)

def test_preprocess_import_empty_string(playbook_include):
    ds = {}
    new_ds = {}
    with pytest.raises(AnsibleParserError, match="import_playbook statements must specify the file name to import"):
        playbook_include._preprocess_import(ds, new_ds, 'import_playbook', '')

def test_preprocess_import_valid_string_no_params(playbook_include, mocker):
    ds = {}
    new_ds = {}
    mocker.patch('ansible.playbook.playbook_include.split_args', return_value=['playbook.yml'])
    playbook_include._preprocess_import(ds, new_ds, 'import_playbook', 'playbook.yml')
    assert new_ds['import_playbook'] == 'playbook.yml'

def test_preprocess_import_valid_string_with_params(playbook_include, mocker):
    ds = {}
    new_ds = {}
    mocker.patch('ansible.playbook.playbook_include.split_args', return_value=['playbook.yml', 'param1=value1', 'param2=value2'])
    mocker.patch('ansible.playbook.playbook_include.Display.deprecated')
    mocker.patch('ansible.playbook.playbook_include.parse_kv', return_value={'param1': 'value1', 'param2': 'value2'})
    playbook_include._preprocess_import(ds, new_ds, 'import_playbook', 'playbook.yml param1=value1 param2=value2')
    assert new_ds['import_playbook'] == 'playbook.yml'
    assert new_ds['vars'] == {'param1': 'value1', 'param2': 'value2'}
    Display.deprecated.assert_called_once_with("Additional parameters in import_playbook statements are deprecated. Use 'vars' instead. See 'import_playbook' documentation for examples.", version='2.14')

def test_preprocess_import_with_tags(playbook_include, mocker):
    ds = {}
    new_ds = {}
    mocker.patch('ansible.playbook.playbook_include.split_args', return_value=['playbook.yml', 'tags=tag1,tag2'])
    mocker.patch('ansible.playbook.playbook_include.Display.deprecated')
    mocker.patch('ansible.playbook.playbook_include.parse_kv', return_value={'tags': 'tag1,tag2'})
    playbook_include._preprocess_import(ds, new_ds, 'import_playbook', 'playbook.yml tags=tag1,tag2')
    assert new_ds['import_playbook'] == 'playbook.yml'
    assert new_ds['tags'] == 'tag1,tag2'
    Display.deprecated.assert_called_once_with("Additional parameters in import_playbook statements are deprecated. Use 'vars' instead. See 'import_playbook' documentation for examples.", version='2.14')

def test_preprocess_import_with_vars_conflict(playbook_include, mocker):
    ds = {}
    new_ds = {'vars': {}}
    mocker.patch('ansible.playbook.playbook_include.split_args', return_value=['playbook.yml', 'param1=value1'])
    mocker.patch('ansible.playbook.playbook_include.Display.deprecated')
    mocker.patch('ansible.playbook.playbook_include.parse_kv', return_value={'param1': 'value1'})
    with pytest.raises(AnsibleParserError, match="import_playbook parameters cannot be mixed with 'vars' entries for import statements"):
        playbook_include._preprocess_import(ds, new_ds, 'import_playbook', 'playbook.yml param1=value1')
