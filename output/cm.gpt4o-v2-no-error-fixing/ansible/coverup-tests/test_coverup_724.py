# file: lib/ansible/playbook/playbook_include.py:157-184
# asked: {"lines": [162, 163, 164, 165, 169, 170, 171, 173, 174, 175, 176, 179, 180, 181, 182, 183, 184], "branches": [[162, 163], [162, 164], [164, 165], [164, 169], [170, 171], [170, 173], [174, 0], [174, 175], [180, 181], [180, 182], [182, 183], [182, 184]]}
# gained: {"lines": [162, 163, 164, 165, 169, 170, 171, 173, 174, 175, 176, 179, 180, 181, 182, 183, 184], "branches": [[162, 163], [162, 164], [164, 165], [164, 169], [170, 171], [170, 173], [174, 175], [180, 181], [180, 182], [182, 183], [182, 184]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.playbook_include import PlaybookInclude

def test_preprocess_import_none_value():
    playbook_include = PlaybookInclude()
    ds = {}
    new_ds = {}
    with pytest.raises(AnsibleParserError, match="playbook import parameter is missing"):
        playbook_include._preprocess_import(ds, new_ds, 'import_playbook', None)

def test_preprocess_import_non_string_value():
    playbook_include = PlaybookInclude()
    ds = {}
    new_ds = {}
    with pytest.raises(AnsibleParserError, match="playbook import parameter must be a string indicating a file path, got <class 'int'> instead"):
        playbook_include._preprocess_import(ds, new_ds, 'import_playbook', 123)

def test_preprocess_import_empty_string():
    playbook_include = PlaybookInclude()
    ds = {}
    new_ds = {}
    with pytest.raises(AnsibleParserError, match="import_playbook statements must specify the file name to import"):
        playbook_include._preprocess_import(ds, new_ds, 'import_playbook', "")

def test_preprocess_import_with_tags():
    playbook_include = PlaybookInclude()
    ds = {}
    new_ds = {}
    playbook_include._preprocess_import(ds, new_ds, 'import_playbook', "test_playbook.yml tags=tag1,tag2")
    assert new_ds['import_playbook'] == "test_playbook.yml"
    assert new_ds['tags'] == "tag1,tag2"

def test_preprocess_import_with_vars():
    playbook_include = PlaybookInclude()
    ds = {}
    new_ds = {'vars': {}}
    with pytest.raises(AnsibleParserError, match="import_playbook parameters cannot be mixed with 'vars' entries for import statements"):
        playbook_include._preprocess_import(ds, new_ds, 'import_playbook', "test_playbook.yml var1=value1")
