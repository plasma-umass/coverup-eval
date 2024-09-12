# file: lib/ansible/plugins/lookup/template.py:97-164
# asked: {"lines": [97, 99, 101, 104, 105, 106, 107, 108, 109, 110, 112, 113, 115, 117, 118, 120, 121, 122, 123, 124, 127, 128, 132, 133, 134, 135, 136, 137, 143, 144, 145, 147, 148, 149, 150, 151, 152, 153, 155, 158, 160, 162, 164], "branches": [[112, 113], [112, 115], [117, 118], [117, 164], [122, 123], [122, 162], [128, 132], [128, 137], [133, 134], [133, 136], [155, 158], [155, 160]]}
# gained: {"lines": [97, 99, 101, 104, 105, 106, 107, 108, 109, 110, 112, 115, 117, 118, 120, 121, 122, 123, 124, 127, 128, 132, 133, 134, 135, 136, 137, 143, 144, 145, 147, 148, 149, 150, 151, 152, 153, 155, 160, 162, 164], "branches": [[112, 115], [117, 118], [117, 164], [122, 123], [122, 162], [128, 132], [133, 134], [133, 136], [155, 160]]}

import pytest
from unittest.mock import MagicMock, patch
from ansible.errors import AnsibleError
from ansible.plugins.lookup.template import LookupModule
from ansible.template import Templar

@pytest.fixture
def lookup_module():
    loader = MagicMock()
    templar = MagicMock(spec=Templar)
    return LookupModule(loader=loader, templar=templar)

@patch('ansible.template.generate_ansible_template_vars')
@patch('os.path.getmtime', return_value=0)
@patch('os.stat')
@patch('pwd.getpwuid')
def test_run_template_found(mock_getpwuid, mock_stat, mock_getmtime, mock_generate_vars, lookup_module, monkeypatch):
    terms = ['test_template.j2']
    variables = {
        'ansible_search_path': ['/mock/path']
    }
    kwargs = {
        'convert_data': True,
        'template_vars': {'var1': 'value1'},
        'jinja2_native': False,
        'variable_start_string': '{{',
        'variable_end_string': '}}',
        'comment_start_string': '{#',
        'comment_end_string': '#}'
    }

    mock_stat.return_value.st_uid = 1000
    mock_getpwuid.return_value.pw_name = 'user'
    mock_generate_vars.return_value = {
        'template_host': 'localhost',
        'template_path': 'test_template.j2',
        'template_mtime': '2023-01-01 00:00:00',
        'template_uid': 'user',
        'template_run_date': '2023-01-01 00:00:00',
        'template_destpath': None,
        'template_fullpath': '/mock/path/test_template.j2',
        'ansible_managed': 'Ansible managed'
    }

    lookup_module.set_options = MagicMock()
    lookup_module.get_option = MagicMock(side_effect=lambda x: kwargs[x])
    lookup_module.find_file_in_search_path = MagicMock(return_value='/mock/path/test_template.j2')
    lookup_module._loader._get_file_contents = MagicMock(return_value=(b"template content", None))
    lookup_module._templar.template = MagicMock(return_value="rendered content")

    result = lookup_module.run(terms, variables, **kwargs)

    lookup_module.set_options.assert_called_once_with(var_options=variables, direct=kwargs)
    lookup_module.get_option.assert_any_call('convert_data')
    lookup_module.get_option.assert_any_call('template_vars')
    lookup_module.get_option.assert_any_call('jinja2_native')
    lookup_module.get_option.assert_any_call('variable_start_string')
    lookup_module.get_option.assert_any_call('variable_end_string')
    lookup_module.get_option.assert_any_call('comment_start_string')
    lookup_module.get_option.assert_any_call('comment_end_string')
    lookup_module.find_file_in_search_path.assert_called_once_with(variables, 'templates', 'test_template.j2')
    lookup_module._loader._get_file_contents.assert_called_once_with('/mock/path/test_template.j2')
    lookup_module._templar.template.assert_called_once_with("template content", preserve_trailing_newlines=True, convert_data=True, escape_backslashes=False)

    assert result == ["rendered content"]

def test_run_template_not_found(lookup_module, monkeypatch):
    terms = ['missing_template.j2']
    variables = {}
    kwargs = {}

    lookup_module.set_options = MagicMock()
    lookup_module.get_option = MagicMock()
    lookup_module.find_file_in_search_path = MagicMock(return_value=None)

    with pytest.raises(AnsibleError, match="the template file missing_template.j2 could not be found for the lookup"):
        lookup_module.run(terms, variables, **kwargs)

    lookup_module.set_options.assert_called_once_with(var_options=variables, direct=kwargs)
    lookup_module.find_file_in_search_path.assert_called_once_with(variables, 'templates', 'missing_template.j2')
