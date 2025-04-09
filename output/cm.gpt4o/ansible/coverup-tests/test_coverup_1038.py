# file lib/ansible/cli/doc.py:1174-1302
# lines [1192, 1208, 1209, 1213, 1216, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1259, 1260, 1261, 1262, 1263, 1264, 1280, 1281, 1284, 1294]
# branches ['1186->1189', '1191->1192', '1199->1204', '1204->1219', '1206->1216', '1207->1208', '1212->1213', '1219->1222', '1222->1227', '1227->1232', '1232->1241', '1241->1270', '1244->1251', '1251->1252', '1251->1258', '1258->1243', '1258->1259', '1270->1275', '1278->1280', '1280->1281', '1280->1284', '1288->1298', '1291->1294', '1298->1302']

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_display_columns():
    with patch('ansible.cli.doc.display.columns', 120):
        yield

@pytest.fixture
def mock_context_cliargs():
    with patch('ansible.cli.doc.context.CLIARGS', {'type': 'module'}):
        yield

@pytest.fixture
def mock_get_versioned_doclink():
    with patch('ansible.cli.doc.get_versioned_doclink', return_value='http://example.com'):
        yield

def test_get_man_text_full_coverage(mock_display_columns, mock_context_cliargs, mock_get_versioned_doclink):
    doc = {
        'name': 'test_module',
        'filename': 'test_module.py',
        'description': ['This is a test module.'],
        'version_added': '2.9',
        'version_added_collection': 'community.general',
        'deprecated': {
            'why': 'No longer maintained',
            'removed_at_date': '2023-01-01',
            'alternative': 'new_module'
        },
        'has_action': True,
        'options': {
            'param1': {
                'description': ['Parameter 1 description'],
                'required': True
            }
        },
        'attributes': {
            'attr1': 'Attribute 1 description'
        },
        'notes': ['Note 1', 'Note 2'],
        'seealso': [
            {'module': 'other_module', 'description': 'See other module'},
            {'name': 'External Link', 'link': 'http://example.com', 'description': 'External documentation'},
            {'ref': 'some_ref', 'description': 'Reference documentation'}
        ],
        'requirements': ['Requirement 1', 'Requirement 2'],
        'plainexamples': 'Example usage of the module.',
        'returndocs': {
            'return1': {
                'description': 'Return value 1 description',
                'returned': 'always',
                'type': 'str'
            }
        }
    }

    result = DocCLI.get_man_text(doc, collection_name='community.general', plugin_type='module')
    
    assert "> COMMUNITY.GENERAL.TEST_MODULE    (test_module.py)\n" in result
    assert "This is a test module." in result
    assert "ADDED IN: version 2.9 of community.general" in result
    assert "DEPRECATED: \n" in result
    assert "Reason: No longer maintained\n\tWill be removed in a release after 2023-01-01\n\tAlternatives: new_module" in result
    assert "  * note: This module has a corresponding action plugin." in result
    assert "OPTIONS (= is mandatory):" in result
    assert "ATTRIBUTES:" in result
    assert "NOTES:" in result
    assert "SEE ALSO:" in result
    assert "Module other_module" in result
    assert "External Link" in result
    assert "Ansible documentation [some_ref]" in result
    assert "REQUIREMENTS:" in result
    assert "EXAMPLES:" in result
    assert "Example usage of the module." in result
    assert "RETURN VALUES:" in result
