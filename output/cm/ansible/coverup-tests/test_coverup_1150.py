# file lib/ansible/cli/doc.py:1350-1385
# lines [1351, 1352, 1353, 1355, 1357, 1358, 1359, 1361, 1362, 1364, 1365, 1366, 1368, 1369, 1371, 1373, 1374, 1376, 1378, 1380, 1381, 1382, 1383, 1385]
# branches ['1355->1357', '1355->1378', '1359->1361', '1359->1364', '1365->1366', '1365->1368', '1368->1369', '1368->1371', '1373->1374', '1373->1376', '1380->1381', '1380->1383']

import pytest

@pytest.fixture
def mock_doc():
    return {
        'plugin': 'my_lookup_plugin',
        'options': {
            'param1': {
                'type': 'string',
                'description': 'First parameter',
                'required': True
            },
            'param2': {
                'type': 'int',
                'description': 'Second parameter',
                'default': 10
            },
            '_terms': {
                'description': 'Terms',
                'required': False
            }
        }
    }

def test_do_lookup_snippet(mock_doc):
    from ansible.cli.doc import _do_lookup_snippet

    expected_comment = [
        '# _terms(string): Terms',
        '# param1(string): First parameter',
        '# param2(int): Second parameter',
        ''
    ]
    expected_snippet = "lookup('my_lookup_plugin', < _terms >, param1='<REQUIRED>', param2=10)"

    result = _do_lookup_snippet(mock_doc)

    assert result[:-1] == expected_comment
    assert result[-1] == expected_snippet
