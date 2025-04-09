# file: lib/ansible/plugins/lookup/template.py:97-164
# asked: {"lines": [97, 99, 101, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 120, 121, 122, 123, 124, 127, 128, 132, 133, 134, 135, 136, 137, 143, 144, 145, 147, 148, 149, 150, 151, 152, 153, 155, 158, 160, 162, 164], "branches": [[112, 113], [112, 115], [117, 118], [117, 164], [122, 123], [122, 162], [128, 132], [128, 137], [133, 134], [133, 136], [155, 158], [155, 160]]}
# gained: {"lines": [97, 99, 101, 104, 105, 106, 107, 108, 109, 110, 112, 115, 117, 118, 120, 121, 122, 123, 124, 127, 128, 132, 133, 134, 135, 136, 137, 143, 144, 145, 147, 148, 149, 150, 151, 152, 153, 155, 160, 162, 164], "branches": [[112, 115], [117, 118], [117, 164], [122, 123], [122, 162], [128, 132], [133, 134], [133, 136], [155, 160]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError
from ansible.plugins.lookup.template import LookupModule

@pytest.fixture
def lookup_module():
    return LookupModule()

@pytest.fixture
def mock_templar():
    templar = MagicMock()
    templar.template.return_value = "rendered_template"
    return templar

@pytest.fixture
def mock_loader():
    loader = MagicMock()
    loader._get_file_contents.return_value = (b"template content", None)
    return loader

@pytest.fixture
def mock_variables():
    return {
        'ansible_search_path': ['/mock/path'],
        'template_vars': {'var1': 'value1'}
    }

@pytest.fixture
def mock_os_stat():
    stat_result = MagicMock()
    stat_result.st_uid = 1000
    stat_result.st_mtime = 1609459200  # Mock timestamp
    return stat_result

def test_run_template_found(lookup_module, mock_templar, mock_loader, mock_variables, mock_os_stat):
    terms = ['template1.j2']
    variables = mock_variables

    lookup_module._templar = mock_templar
    lookup_module._loader = mock_loader
    lookup_module.set_options = MagicMock()
    lookup_module.get_option = MagicMock(side_effect=lambda x: variables.get(x, None))
    lookup_module.find_file_in_search_path = MagicMock(return_value='/mock/path/template1.j2')

    with patch('os.stat', return_value=mock_os_stat), patch('pwd.getpwuid', return_value=MagicMock(pw_name='mockuser')), patch('ansible.template.USE_JINJA2_NATIVE', False):
        result = lookup_module.run(terms, variables)

    assert result == ["rendered_template"]
    mock_templar.template.assert_called_once_with(
        "template content", preserve_trailing_newlines=True, convert_data=None, escape_backslashes=False
    )

def test_run_template_not_found(lookup_module, mock_templar, mock_loader, mock_variables):
    terms = ['template1.j2']
    variables = mock_variables

    lookup_module._templar = mock_templar
    lookup_module._loader = mock_loader
    lookup_module.set_options = MagicMock()
    lookup_module.get_option = MagicMock(side_effect=lambda x: variables.get(x, None))
    lookup_module.find_file_in_search_path = MagicMock(return_value=None)

    with pytest.raises(AnsibleError, match="the template file template1.j2 could not be found for the lookup"):
        lookup_module.run(terms, variables)

def test_run_with_jinja2_native(lookup_module, mock_templar, mock_loader, mock_variables, mock_os_stat):
    terms = ['template1.j2']
    variables = mock_variables

    lookup_module._templar = mock_templar
    lookup_module._loader = mock_loader
    lookup_module.set_options = MagicMock()
    lookup_module.get_option = MagicMock(side_effect=lambda x: variables.get(x, None))
    lookup_module.find_file_in_search_path = MagicMock(return_value='/mock/path/template1.j2')

    with patch('os.stat', return_value=mock_os_stat), patch('pwd.getpwuid', return_value=MagicMock(pw_name='mockuser')), patch('ansible.template.USE_JINJA2_NATIVE', True):
        result = lookup_module.run(terms, variables)

    assert result == ["rendered_template"]
    mock_templar.template.assert_called_once_with(
        "template content", preserve_trailing_newlines=True, convert_data=None, escape_backslashes=False
    )
