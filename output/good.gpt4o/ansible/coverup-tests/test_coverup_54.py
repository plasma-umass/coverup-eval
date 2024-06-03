# file lib/ansible/cli/doc.py:1350-1385
# lines [1350, 1351, 1352, 1353, 1355, 1357, 1358, 1359, 1361, 1362, 1364, 1365, 1366, 1368, 1369, 1371, 1373, 1374, 1376, 1378, 1380, 1381, 1382, 1383, 1385]
# branches ['1355->1357', '1355->1378', '1359->1361', '1359->1364', '1365->1366', '1365->1368', '1368->1369', '1368->1371', '1373->1374', '1373->1376', '1380->1381', '1380->1383']

import pytest

def test_do_lookup_snippet():
    from ansible.cli.doc import _do_lookup_snippet

    # Test case with required options and different types
    doc = {
        'plugin': 'test_plugin',
        'options': {
            'option1': {'type': 'string', 'description': 'desc1', 'required': True},
            'option2': {'type': 'int', 'description': 'desc2', 'default': 42},
            '_terms': {'type': 'list', 'description': 'desc3'},
            'option3': {'type': 'bool', 'description': 'desc4', 'default': False},
        }
    }

    result = _do_lookup_snippet(doc)
    expected = [
        "# _terms(list): desc3",
        "# option1(string): desc1",
        "# option2(int): desc2",
        "# option3(bool): desc4",
        "",
        "lookup('test_plugin', < _terms >, option1='<REQUIRED>', option2=42, option3=False)"
    ]
    assert result == expected

    # Test case with non-boolean required value
    doc_invalid = {
        'plugin': 'test_plugin',
        'options': {
            'option1': {'type': 'string', 'description': 'desc1', 'required': 'yes'},
        }
    }

    with pytest.raises(ValueError, match="Incorrect value for 'Required', a boolean is needed: yes"):
        _do_lookup_snippet(doc_invalid)

    # Test case with no options
    doc_empty = {
        'plugin': 'test_plugin',
        'options': {}
    }

    result = _do_lookup_snippet(doc_empty)
    expected = ["lookup('test_plugin', )"]
    assert result == expected
