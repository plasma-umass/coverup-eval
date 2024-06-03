# file lib/ansible/playbook/playbook_include.py:157-184
# lines []
# branches ['174->exit']

import pytest
from ansible.playbook.playbook_include import PlaybookInclude
from ansible.errors import AnsibleParserError
from ansible.utils.display import Display
from unittest.mock import patch

@pytest.fixture
def playbook_include():
    return PlaybookInclude()

def test_preprocess_import_with_additional_parameters(playbook_include, mocker):
    ds = {}
    new_ds = {}
    k = 'import_playbook'
    v = 'playbook.yml param1=value1 param2=value2'

    mock_display = mocker.patch('ansible.utils.display.Display.deprecated')

    playbook_include._preprocess_import(ds, new_ds, k, v)

    assert new_ds['import_playbook'] == 'playbook.yml'
    assert 'vars' in new_ds
    assert new_ds['vars'] == {'param1': 'value1', 'param2': 'value2'}
    mock_display.assert_called_once_with(
        "Additional parameters in import_playbook statements are deprecated. "
        "Use 'vars' instead. See 'import_playbook' documentation for examples.", version='2.14'
    )

def test_preprocess_import_with_tags(playbook_include, mocker):
    ds = {}
    new_ds = {}
    k = 'import_playbook'
    v = 'playbook.yml param1=value1 tags=tag1,tag2'

    mock_display = mocker.patch('ansible.utils.display.Display.deprecated')

    playbook_include._preprocess_import(ds, new_ds, k, v)

    assert new_ds['import_playbook'] == 'playbook.yml'
    assert 'vars' in new_ds
    assert new_ds['vars'] == {'param1': 'value1'}
    assert new_ds['tags'] == 'tag1,tag2'
    mock_display.assert_called_once_with(
        "Additional parameters in import_playbook statements are deprecated. "
        "Use 'vars' instead. See 'import_playbook' documentation for examples.", version='2.14'
    )

def test_preprocess_import_with_vars_conflict(playbook_include):
    ds = {}
    new_ds = {'vars': {'existing_var': 'value'}}
    k = 'import_playbook'
    v = 'playbook.yml param1=value1'

    with pytest.raises(AnsibleParserError, match="import_playbook parameters cannot be mixed with 'vars' entries for import statements"):
        playbook_include._preprocess_import(ds, new_ds, k, v)

def test_preprocess_import_no_additional_parameters(playbook_include, mocker):
    ds = {}
    new_ds = {}
    k = 'import_playbook'
    v = 'playbook.yml'

    mock_display = mocker.patch('ansible.utils.display.Display.deprecated')

    playbook_include._preprocess_import(ds, new_ds, k, v)

    assert new_ds['import_playbook'] == 'playbook.yml'
    assert 'vars' not in new_ds
    assert 'tags' not in new_ds
    mock_display.assert_not_called()
