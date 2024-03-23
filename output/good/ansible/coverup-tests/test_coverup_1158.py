# file lib/ansible/cli/doc.py:473-504
# lines [478, 479, 480, 481, 482, 484, 485, 487, 488, 489, 490, 492, 493, 495, 496, 497, 498, 499, 500, 501, 504]
# branches ['480->481', '480->484', '481->480', '481->482', '487->488', '487->489', '489->490', '489->492', '495->496', '495->504', '496->495', '496->497', '497->498', '497->499']

import pytest
from ansible.cli.doc import DocCLI
from ansible.utils.display import Display
from ansible.module_utils.six import iteritems

# Mock the Display class to control the output behavior
@pytest.fixture
def mock_display(mocker):
    display_mock = mocker.patch.object(Display, '__new__', return_value=mocker.Mock(spec=Display))
    display_mock.columns = 80
    return display_mock()

# Test function to cover lines 478-504
def test_display_available_roles(mock_display, mocker):
    pager_mock = mocker.patch('ansible.cli.doc.DocCLI.pager')
    list_json = {
        'role1': {
            'entry_points': {
                'ep1': 'Short description for ep1',
                'ep2': 'Short description for ep2'
            }
        },
        'role2': {
            'entry_points': {
                'ep3': 'Short description for ep3',
                'ep4': 'Short description that is way too long to fit in the line limit and will be truncated'
            }
        }
    }

    # Provide a non-empty list for args to avoid ValueError
    doc_cli = DocCLI(['--help'])
    doc_cli._display_available_roles(list_json)

    # Assertions to verify the pager was called with the correct text
    expected_text = [
        'role1 ep1 Short description for ep1',
        'role1 ep2 Short description for ep2',
        'role2 ep3 Short description for ep3',
        # Ensure the description is truncated correctly according to the linelimit
        'role2 ep4 Short description that is way too long to fit in the line limit an...'
    ]
    pager_mock.assert_called_once_with("\n".join(expected_text))

    # Clean up after the test
    mocker.stopall()
