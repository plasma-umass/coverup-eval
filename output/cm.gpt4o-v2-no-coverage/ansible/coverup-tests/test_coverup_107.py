# file: lib/ansible/playbook/playbook_include.py:157-184
# asked: {"lines": [157, 162, 163, 164, 165, 169, 170, 171, 173, 174, 175, 176, 179, 180, 181, 182, 183, 184], "branches": [[162, 163], [162, 164], [164, 165], [164, 169], [170, 171], [170, 173], [174, 0], [174, 175], [180, 181], [180, 182], [182, 183], [182, 184]]}
# gained: {"lines": [157, 162, 163, 164, 165, 169, 170, 171, 173, 174, 175, 176, 179, 180, 181, 182, 183, 184], "branches": [[162, 163], [162, 164], [164, 165], [164, 169], [170, 171], [170, 173], [174, 0], [174, 175], [180, 181], [180, 182], [182, 183], [182, 184]]}

import pytest
from ansible.errors import AnsibleParserError
from ansible.playbook.playbook_include import PlaybookInclude

class MockDisplay:
    def deprecated(self, msg, version):
        pass

@pytest.fixture
def mock_display(monkeypatch):
    display = MockDisplay()
    monkeypatch.setattr("ansible.playbook.playbook_include.display", display)
    return display

def test_preprocess_import_missing_parameter():
    pb_include = PlaybookInclude()
    ds = {}
    new_ds = {}
    with pytest.raises(AnsibleParserError, match="playbook import parameter is missing"):
        pb_include._preprocess_import(ds, new_ds, 'import_playbook', None)

def test_preprocess_import_invalid_type():
    pb_include = PlaybookInclude()
    ds = {}
    new_ds = {}
    with pytest.raises(AnsibleParserError, match="playbook import parameter must be a string indicating a file path"):
        pb_include._preprocess_import(ds, new_ds, 'import_playbook', 123)

def test_preprocess_import_empty_string():
    pb_include = PlaybookInclude()
    ds = {}
    new_ds = {}
    with pytest.raises(AnsibleParserError, match="import_playbook statements must specify the file name to import"):
        pb_include._preprocess_import(ds, new_ds, 'import_playbook', "")

def test_preprocess_import_valid_string(mock_display):
    pb_include = PlaybookInclude()
    ds = {}
    new_ds = {}
    pb_include._preprocess_import(ds, new_ds, 'import_playbook', "playbook.yml")
    assert new_ds['import_playbook'] == "playbook.yml"

def test_preprocess_import_with_params(mock_display):
    pb_include = PlaybookInclude()
    ds = {}
    new_ds = {}
    pb_include._preprocess_import(ds, new_ds, 'import_playbook', "playbook.yml param1=value1 param2=value2")
    assert new_ds['import_playbook'] == "playbook.yml"
    assert new_ds['vars'] == {'param1': 'value1', 'param2': 'value2'}

def test_preprocess_import_with_tags(mock_display):
    pb_include = PlaybookInclude()
    ds = {}
    new_ds = {}
    pb_include._preprocess_import(ds, new_ds, 'import_playbook', "playbook.yml tags=tag1 param1=value1")
    assert new_ds['import_playbook'] == "playbook.yml"
    assert new_ds['tags'] == 'tag1'
    assert new_ds['vars'] == {'param1': 'value1'}

def test_preprocess_import_with_vars_conflict():
    pb_include = PlaybookInclude()
    ds = {}
    new_ds = {'vars': {'existing_var': 'value'}}
    with pytest.raises(AnsibleParserError, match="import_playbook parameters cannot be mixed with 'vars' entries for import statements"):
        pb_include._preprocess_import(ds, new_ds, 'import_playbook', "playbook.yml param1=value1")
