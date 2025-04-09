# file: lib/ansible/plugins/lookup/template.py:97-164
# asked: {"lines": [113, 158], "branches": [[112, 113], [128, 137], [155, 158]]}
# gained: {"lines": [], "branches": [[128, 137]]}

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
    templar.set_temporary_context = MagicMock()
    return templar

@pytest.fixture
def mock_loader():
    loader = MagicMock()
    loader._get_file_contents.return_value = (b"template_content", "show_data")
    return loader

@pytest.fixture
def mock_display():
    with patch("ansible.plugins.lookup.template.display") as display:
        yield display

@pytest.fixture
def mock_find_file_in_search_path():
    with patch.object(LookupModule, 'find_file_in_search_path', return_value="path/to/template") as mock_method:
        yield mock_method

@pytest.fixture
def mock_generate_ansible_template_vars():
    with patch("ansible.plugins.lookup.template.generate_ansible_template_vars", return_value={"template_var": "value"}):
        yield

def test_run_template_found(lookup_module, mock_templar, mock_loader, mock_display, mock_find_file_in_search_path, mock_generate_ansible_template_vars):
    lookup_module._templar = mock_templar
    lookup_module._loader = mock_loader
    lookup_module.set_options = MagicMock()
    lookup_module.get_option = MagicMock(side_effect=lambda x: {
        'convert_data': True,
        'template_vars': {},
        'jinja2_native': False,
        'variable_start_string': '{{',
        'variable_end_string': '}}',
        'comment_start_string': '{#',
        'comment_end_string': '#}'
    }[x])

    terms = ["template1"]
    variables = {"var1": "value1"}

    result = lookup_module.run(terms, variables)

    assert result == ["rendered_template"]
    mock_display.debug.assert_called_with("File lookup term: template1")
    mock_display.vvvv.assert_called_with("File lookup using path/to/template as file")
    mock_loader._get_file_contents.assert_called_with("path/to/template")
    mock_templar.template.assert_called_with("template_content", preserve_trailing_newlines=True, convert_data=True, escape_backslashes=False)

def test_run_template_not_found(lookup_module, mock_templar, mock_loader, mock_display, mock_find_file_in_search_path):
    lookup_module._templar = mock_templar
    lookup_module._loader = mock_loader
    lookup_module.set_options = MagicMock()
    lookup_module.get_option = MagicMock(side_effect=lambda x: {
        'convert_data': True,
        'template_vars': {},
        'jinja2_native': False,
        'variable_start_string': '{{',
        'variable_end_string': '}}',
        'comment_start_string': '{#',
        'comment_end_string': '#}'
    }[x])

    mock_find_file_in_search_path.return_value = None

    terms = ["template1"]
    variables = {"var1": "value1"}

    with pytest.raises(AnsibleError, match="the template file template1 could not be found for the lookup"):
        lookup_module.run(terms, variables)
