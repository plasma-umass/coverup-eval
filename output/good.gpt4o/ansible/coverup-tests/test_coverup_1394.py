# file lib/ansible/cli/doc.py:1174-1302
# lines [1213, 1216, 1280, 1281, 1284, 1294]
# branches ['1186->1189', '1199->1204', '1204->1219', '1206->1216', '1212->1213', '1219->1222', '1222->1227', '1227->1232', '1232->1241', '1241->1270', '1258->1243', '1270->1275', '1278->1280', '1280->1281', '1280->1284', '1288->1298', '1291->1294', '1298->1302']

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

def test_get_man_text_full_coverage(mock_display_columns, mock_context_cliargs):
    doc = {
        'name': 'test_module',
        'filename': 'test_module.py',
        'description': 'This is a test module.',
        'version_added': '2.0',
        'version_added_collection': 'test_collection',
        'deprecated': {
            'why': 'test reason',
            'version': '2.0',
            'alternative': 'test alternative'
        },
        'has_action': True,
        'options': {
            'option1': {
                'description': 'Option 1 description',
                'required': True
            }
        },
        'attributes': {
            'attr1': 'Attribute 1 description'
        },
        'notes': ['Note 1', 'Note 2'],
        'seealso': [
            {
                'module': 'other_module',
                'description': 'Other module description'
            },
            {
                'name': 'External link',
                'link': 'http://example.com',
                'description': 'External link description'
            },
            {
                'ref': 'some_ref',
                'description': 'Reference description'
            }
        ],
        'requirements': ['Requirement 1', 'Requirement 2'],
        'plainexamples': 'Example usage of the module.',
        'returndocs': {
            'return1': {
                'description': 'Return value 1 description',
                'returned': 'success',
                'type': 'str'
            }
        }
    }

    result = DocCLI.get_man_text(doc, collection_name='test_collection', plugin_type='module')
    
    assert "> TEST_COLLECTION.TEST_MODULE    (test_module.py)\n" in result
    assert "This is a test module." in result
    assert "ADDED IN: version 2.0 of test_collection" in result
    assert "DEPRECATED: \n" in result
    assert "Reason: test reason" in result
    assert "Will be removed in: Ansible 2.0" in result
    assert "Alternatives: test alternative" in result
    assert "  * note: This module has a corresponding action plugin." in result
    assert "OPTIONS (= is mandatory):" in result
    assert "option1\n        Option 1 description" in result
    assert "ATTRIBUTES:" in result
    assert "attr1: Attribute 1 description" in result
    assert "NOTES:" in result
    assert "* Note 1" in result
    assert "* Note 2" in result
    assert "SEE ALSO:" in result
    assert "Module other_module" in result
    assert "Other module description" in result
    assert "External link" in result
    assert "External link description" in result
    assert "http://example.com" in result
    assert "Ansible documentation [some_ref]" in result
    assert "Reference description" in result
    assert "REQUIREMENTS:" in result
    assert "Requirement 1, Requirement 2" in result
    assert "EXAMPLES:" in result
    assert "Example usage of the module." in result
    assert "RETURN VALUES:" in result
    assert "return1\n        Return value 1 description" in result
