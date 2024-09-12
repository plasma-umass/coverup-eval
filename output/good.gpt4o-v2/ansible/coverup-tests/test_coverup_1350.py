# file: lib/ansible/playbook/playbook_include.py:157-184
# asked: {"lines": [162, 163, 164, 165, 169, 170, 171, 173, 174, 175, 176, 179, 180, 181, 182, 183, 184], "branches": [[162, 163], [162, 164], [164, 165], [164, 169], [170, 171], [170, 173], [174, 0], [174, 175], [180, 181], [180, 182], [182, 183], [182, 184]]}
# gained: {"lines": [162, 163, 164, 165, 169, 170, 171, 173, 174, 175, 176, 179, 180, 181, 182, 183, 184], "branches": [[162, 163], [162, 164], [164, 165], [164, 169], [170, 171], [170, 173], [174, 0], [174, 175], [180, 181], [180, 182], [182, 183], [182, 184]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.module_utils.six import string_types
from ansible.parsing.splitter import split_args, parse_kv
from ansible.playbook.playbook_include import PlaybookInclude

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
        playbook_include._preprocess_import(ds, new_ds, 'import_playbook', "")

def test_preprocess_import_valid_string_no_params(playbook_include, mocker):
    ds = {}
    new_ds = {}
    mocker.patch('ansible.utils.display.Display.deprecated')
    playbook_include._preprocess_import(ds, new_ds, 'import_playbook', "test_playbook.yml")
    assert new_ds['import_playbook'] == "test_playbook.yml"

def test_preprocess_import_valid_string_with_params(playbook_include, mocker):
    ds = {}
    new_ds = {}
    mocker.patch('ansible.utils.display.Display.deprecated')
    playbook_include._preprocess_import(ds, new_ds, 'import_playbook', "test_playbook.yml param1=value1 param2=value2")
    assert new_ds['import_playbook'] == "test_playbook.yml"
    assert new_ds['vars'] == {'param1': 'value1', 'param2': 'value2'}

def test_preprocess_import_with_tags(playbook_include, mocker):
    ds = {}
    new_ds = {}
    mocker.patch('ansible.utils.display.Display.deprecated')
    playbook_include._preprocess_import(ds, new_ds, 'import_playbook', "test_playbook.yml tags=tag1 param1=value1")
    assert new_ds['import_playbook'] == "test_playbook.yml"
    assert new_ds['tags'] == 'tag1'
    assert new_ds['vars'] == {'param1': 'value1'}

def test_preprocess_import_with_vars_conflict(playbook_include, mocker):
    ds = {}
    new_ds = {'vars': {}}
    mocker.patch('ansible.utils.display.Display.deprecated')
    with pytest.raises(AnsibleParserError, match="import_playbook parameters cannot be mixed with 'vars' entries for import statements"):
        playbook_include._preprocess_import(ds, new_ds, 'import_playbook', "test_playbook.yml param1=value1")
