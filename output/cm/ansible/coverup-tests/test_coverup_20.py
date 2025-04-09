# file lib/ansible/cli/doc.py:1113-1172
# lines [1113, 1124, 1125, 1126, 1127, 1129, 1131, 1132, 1134, 1135, 1137, 1139, 1140, 1141, 1143, 1145, 1146, 1147, 1148, 1149, 1150, 1151, 1153, 1154, 1155, 1156, 1159, 1160, 1161, 1162, 1163, 1164, 1165, 1166, 1169, 1170, 1172]
# branches ['1131->1132', '1131->1172', '1134->1135', '1134->1137', '1139->1140', '1139->1148', '1140->1141', '1140->1143', '1148->1149', '1148->1153', '1153->1154', '1153->1159', '1159->1131', '1159->1160', '1160->1161', '1160->1162', '1162->1163', '1162->1165', '1165->1166', '1165->1169']

import pytest
from ansible.cli.doc import DocCLI
from ansible.utils.display import Display
from unittest.mock import MagicMock

# Mock the global display object
@pytest.fixture
def mock_display(mocker):
    mock_display = mocker.patch('ansible.cli.doc.display', autospec=True)
    mock_display.columns = 80
    return mock_display

# Test function to cover missing branches in get_role_man_text
def test_get_role_man_text(mock_display):
    role = 'testrole'
    role_json = {
        'path': '/path/to/role',
        'entry_points': {
            'main': {
                'short_description': 'Main entry point',
                'description': ['This is a', 'description of the main entry point.'],
                'options': {'option1': {'description': 'Option 1 description', 'required': True}},
                'attributes': {'attribute1': 'Attribute 1 value'},
                'author': ['Author One', 'Author Two']
            },
            'secondary': {
                'description': 'A single line description for secondary entry point.',
                'author': 'Single Author'
            }
        }
    }

    args = MagicMock()
    doc_cli = DocCLI(args)
    result_text = doc_cli.get_role_man_text(role, role_json)

    # Assertions to verify the postconditions
    assert "> TESTROLE    (/path/to/role)\n" in ''.join(result_text)
    assert "ENTRY POINT: main - Main entry point\n" in ''.join(result_text)
    assert "ENTRY POINT: secondary\n" in ''.join(result_text)
    assert "This is a description of the main entry point." in ''.join(result_text)
    assert "OPTIONS (= is mandatory):\n" in ''.join(result_text)
    assert "ATTRIBUTES:\n" in ''.join(result_text)
    assert "AUTHOR: Author One, Author Two" in ''.join(result_text)
    assert "AUTHOR: Single Author" in ''.join(result_text)
