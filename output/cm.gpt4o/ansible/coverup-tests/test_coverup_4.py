# file lib/ansible/cli/doc.py:1174-1302
# lines [1174, 1175, 1177, 1179, 1180, 1181, 1182, 1183, 1185, 1186, 1187, 1189, 1191, 1192, 1194, 1196, 1197, 1199, 1200, 1201, 1202, 1204, 1205, 1206, 1207, 1208, 1209, 1212, 1213, 1214, 1216, 1217, 1219, 1220, 1222, 1223, 1224, 1225, 1227, 1228, 1229, 1230, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1259, 1260, 1261, 1262, 1263, 1264, 1266, 1267, 1268, 1270, 1271, 1272, 1275, 1276, 1277, 1278, 1279, 1280, 1281, 1284, 1285, 1286, 1288, 1289, 1290, 1291, 1292, 1294, 1295, 1296, 1298, 1299, 1300, 1302]
# branches ['1186->1187', '1186->1189', '1191->1192', '1191->1194', '1199->1200', '1199->1204', '1204->1205', '1204->1219', '1206->1207', '1206->1216', '1207->1208', '1207->1212', '1212->1213', '1212->1214', '1219->1220', '1219->1222', '1222->1223', '1222->1227', '1227->1228', '1227->1232', '1232->1233', '1232->1241', '1234->1235', '1234->1237', '1241->1242', '1241->1270', '1243->1244', '1243->1266', '1244->1245', '1244->1251', '1251->1252', '1251->1258', '1258->1243', '1258->1259', '1270->1271', '1270->1275', '1275->1276', '1275->1288', '1276->1277', '1276->1278', '1278->1279', '1278->1280', '1280->1281', '1280->1284', '1288->1289', '1288->1298', '1291->1292', '1291->1294', '1298->1299', '1298->1302']

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI
from ansible.utils.display import Display
import textwrap

@pytest.fixture
def mock_display():
    with patch('ansible.cli.doc.display', autospec=True) as mock_display:
        mock_display.columns = 120
        yield mock_display

@pytest.fixture
def mock_context():
    with patch('ansible.cli.doc.context', autospec=True) as mock_context:
        mock_context.CLIARGS = {'type': 'module'}
        yield mock_context

@pytest.fixture
def mock_get_versioned_doclink():
    with patch('ansible.cli.doc.get_versioned_doclink', autospec=True) as mock_get_versioned_doclink:
        mock_get_versioned_doclink.return_value = 'http://example.com'
        yield mock_get_versioned_doclink

def test_get_man_text(mock_display, mock_context, mock_get_versioned_doclink):
    doc = {
        'name': 'test_module',
        'filename': 'test_module.py',
        'description': 'This is a test module.',
        'version_added': '2.0',
        'deprecated': {
            'why': 'No longer needed',
            'removed_in': '2.10',
            'alternative': 'new_module'
        },
        'has_action': True,
        'options': {
            'param1': {
                'description': ['First parameter'],
                'required': True
            }
        },
        'attributes': {
            'attr1': 'value1'
        },
        'notes': ['Note 1', 'Note 2'],
        'seealso': [
            {
                'module': 'another_module',
                'description': 'Related module'
            }
        ],
        'requirements': ['requirement1', 'requirement2'],
        'plainexamples': 'Example usage',
        'returndocs': {
            'return1': {
                'description': 'Return value 1'
            }
        }
    }

    result = DocCLI.get_man_text(doc, collection_name='test_collection', plugin_type='test_plugin')

    assert "> TEST_COLLECTION.TEST_MODULE    (test_module.py)\n" in result
    assert "This is a test module." in result
    assert "ADDED IN: version 2.0\n" in result
    assert "DEPRECATED: \n" in result
    assert "Reason: No longer needed\n\tWill be removed in: Ansible 2.10\n\tAlternatives: new_module" in result
    assert "This module has a corresponding action plugin." in result
    assert "OPTIONS (= is mandatory):\n" in result
    assert "ATTRIBUTES:\n" in result
    assert "NOTES:" in result
    assert "SEE ALSO:" in result
    assert "REQUIREMENTS:" in result
    assert "EXAMPLES:" in result
    assert "RETURN VALUES:" in result
