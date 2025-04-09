# file: lib/ansible/cli/doc.py:1174-1302
# asked: {"lines": [1177, 1179, 1180, 1181, 1182, 1183, 1185, 1186, 1187, 1189, 1191, 1192, 1194, 1196, 1197, 1199, 1200, 1201, 1202, 1204, 1205, 1206, 1207, 1208, 1209, 1212, 1213, 1214, 1216, 1217, 1219, 1220, 1222, 1223, 1224, 1225, 1227, 1228, 1229, 1230, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1258, 1259, 1260, 1261, 1262, 1263, 1264, 1266, 1267, 1268, 1270, 1271, 1272, 1275, 1276, 1277, 1278, 1279, 1280, 1281, 1284, 1285, 1286, 1288, 1289, 1290, 1291, 1292, 1294, 1295, 1296, 1298, 1299, 1300, 1302], "branches": [[1186, 1187], [1186, 1189], [1191, 1192], [1191, 1194], [1199, 1200], [1199, 1204], [1204, 1205], [1204, 1219], [1206, 1207], [1206, 1216], [1207, 1208], [1207, 1212], [1212, 1213], [1212, 1214], [1219, 1220], [1219, 1222], [1222, 1223], [1222, 1227], [1227, 1228], [1227, 1232], [1232, 1233], [1232, 1241], [1234, 1235], [1234, 1237], [1241, 1242], [1241, 1270], [1243, 1244], [1243, 1266], [1244, 1245], [1244, 1251], [1251, 1252], [1251, 1258], [1258, 1243], [1258, 1259], [1270, 1271], [1270, 1275], [1275, 1276], [1275, 1288], [1276, 1277], [1276, 1278], [1278, 1279], [1278, 1280], [1280, 1281], [1280, 1284], [1288, 1289], [1288, 1298], [1291, 1292], [1291, 1294], [1298, 1299], [1298, 1302]]}
# gained: {"lines": [1177, 1179, 1180, 1181, 1182, 1183, 1185, 1186, 1187, 1189, 1191, 1194, 1196, 1197, 1199, 1200, 1201, 1202, 1204, 1205, 1206, 1207, 1212, 1214, 1217, 1219, 1220, 1222, 1223, 1224, 1225, 1227, 1228, 1229, 1230, 1232, 1233, 1234, 1235, 1236, 1237, 1238, 1239, 1241, 1242, 1243, 1244, 1245, 1246, 1247, 1248, 1249, 1250, 1251, 1252, 1253, 1254, 1255, 1256, 1257, 1266, 1267, 1268, 1270, 1271, 1272, 1275, 1276, 1277, 1288, 1289, 1290, 1291, 1292, 1295, 1296, 1298, 1299, 1300, 1302], "branches": [[1186, 1187], [1191, 1194], [1199, 1200], [1204, 1205], [1206, 1207], [1207, 1212], [1212, 1214], [1219, 1220], [1222, 1223], [1227, 1228], [1232, 1233], [1234, 1235], [1234, 1237], [1241, 1242], [1243, 1244], [1243, 1266], [1244, 1245], [1244, 1251], [1251, 1252], [1270, 1271], [1275, 1276], [1275, 1288], [1276, 1277], [1288, 1289], [1291, 1292], [1298, 1299]]}

import pytest
from unittest.mock import patch, MagicMock
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_display_columns(monkeypatch):
    mock_display = MagicMock()
    mock_display.columns = 100
    monkeypatch.setattr('ansible.cli.doc.display', mock_display)
    return mock_display

@pytest.fixture
def mock_context_cliargs(monkeypatch):
    mock_context = MagicMock()
    mock_context.CLIARGS = {'type': 'module'}
    monkeypatch.setattr('ansible.cli.doc.context', mock_context)
    return mock_context

def test_get_man_text_full_coverage(mock_display_columns, mock_context_cliargs):
    doc = {
        'filename': 'test_file.py',
        'description': 'This is a test description.',
        'version_added': '2.0',
        'deprecated': {
            'why': 'Deprecated reason',
            'removed_in': '2.10',
            'alternative': 'Use something else'
        },
        'has_action': True,
        'options': {
            'option1': {
                'description': 'Option 1 description',
                'required': True
            }
        },
        'attributes': {
            'attr1': 'Attribute 1'
        },
        'notes': ['Note 1', 'Note 2'],
        'seealso': [
            {
                'module': 'test_module',
                'description': 'Test module description'
            },
            {
                'name': 'Test Name',
                'link': 'http://example.com',
                'description': 'Test link description'
            }
        ],
        'requirements': ['Requirement 1', 'Requirement 2'],
        'plainexamples': 'Example 1\nExample 2',
        'returndocs': {
            'return1': {
                'description': 'Return 1 description'
            }
        }
    }

    with patch('ansible.cli.doc.DocCLI.tty_ify', side_effect=lambda x: x), \
         patch('ansible.cli.doc.DocCLI._format_version_added', return_value='2.0'), \
         patch('ansible.cli.doc.DocCLI._dump_yaml', side_effect=lambda x, y: str(x)), \
         patch('ansible.cli.doc.DocCLI.add_fields', side_effect=lambda *args, **kwargs: args[0].append('field added')), \
         patch('ansible.utils.plugin_docs.get_versioned_doclink', return_value='http://doclink'):
        
        result = DocCLI.get_man_text(doc, 'test_collection', 'test_plugin_type')
        
        assert '> TEST_COLLECTION.TEST_PLUGIN_TYPE    (test_file.py)\n' in result
        assert 'This is a test description.' in result
        assert 'ADDED IN: 2.0\n' in result
        assert 'DEPRECATED: \n' in result
        assert 'Reason: Deprecated reason\n' in result
        assert 'Will be removed in: Ansible 2.10\n' in result
        assert 'Alternatives: Use something else' in result
        assert '  * note: This module has a corresponding action plugin.\n' in result
        assert 'OPTIONS (= is mandatory):\n' in result
        assert 'field added' in result
        assert 'ATTRIBUTES:\n' in result
        assert "{'attr1': 'Attribute 1'}" in result
        assert 'NOTES:' in result
        assert '* Note 1' in result
        assert '* Note 2' in result
        assert 'SEE ALSO:' in result
        assert '* Module test_module' in result
        assert 'Test module description' in result
        assert '* Test Name' in result
        assert 'Test link description' in result
        assert 'http://example.com' in result
        assert 'REQUIREMENTS:' in result
        assert 'Requirement 1, Requirement 2' in result
        assert 'EXAMPLES:' in result
        assert 'Example 1\nExample 2' in result
        assert 'RETURN VALUES:' in result
        assert 'field added' in result
