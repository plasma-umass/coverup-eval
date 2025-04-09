# file: lib/ansible/cli/doc.py:1350-1385
# asked: {"lines": [1351, 1352, 1353, 1355, 1357, 1358, 1359, 1361, 1362, 1364, 1365, 1366, 1368, 1369, 1371, 1373, 1374, 1376, 1378, 1380, 1381, 1382, 1383, 1385], "branches": [[1355, 1357], [1355, 1378], [1359, 1361], [1359, 1364], [1365, 1366], [1365, 1368], [1368, 1369], [1368, 1371], [1373, 1374], [1373, 1376], [1380, 1381], [1380, 1383]]}
# gained: {"lines": [1351, 1352, 1353, 1355, 1357, 1358, 1359, 1361, 1362, 1364, 1365, 1366, 1368, 1369, 1371, 1373, 1374, 1376, 1378, 1380, 1381, 1382, 1383, 1385], "branches": [[1355, 1357], [1355, 1378], [1359, 1361], [1359, 1364], [1365, 1366], [1365, 1368], [1368, 1369], [1368, 1371], [1373, 1374], [1373, 1376], [1380, 1381]]}

import pytest

def test_do_lookup_snippet_all_branches():
    from ansible.cli.doc import _do_lookup_snippet

    # Test case 1: Required is not a boolean
    doc = {
        'plugin': 'test_plugin',
        'options': {
            'option1': {
                'type': 'string',
                'description': 'A test option',
                'required': 'yes'  # Incorrect type
            }
        }
    }
    with pytest.raises(ValueError, match="Incorrect value for 'Required', a boolean is needed: yes"):
        _do_lookup_snippet(doc)

    # Test case 2: Required is True
    doc = {
        'plugin': 'test_plugin',
        'options': {
            'option1': {
                'type': 'string',
                'description': 'A test option',
                'required': True
            }
        }
    }
    result = _do_lookup_snippet(doc)
    assert result == [
        "# option1(string): A test option",
        "",
        "lookup('test_plugin', , option1='<REQUIRED>')"
    ]

    # Test case 3: Required is False and default is provided
    doc = {
        'plugin': 'test_plugin',
        'options': {
            'option1': {
                'type': 'string',
                'description': 'A test option',
                'required': False,
                'default': 'default_value'
            }
        }
    }
    result = _do_lookup_snippet(doc)
    assert result == [
        "# option1(string): A test option",
        "",
        "lookup('test_plugin', , option1='default_value')"
    ]

    # Test case 4: Option type is not string
    doc = {
        'plugin': 'test_plugin',
        'options': {
            'option1': {
                'type': 'int',
                'description': 'A test option',
                'required': False,
                'default': 10
            }
        }
    }
    result = _do_lookup_snippet(doc)
    assert result == [
        "# option1(int): A test option",
        "",
        "lookup('test_plugin', , option1=10)"
    ]

    # Test case 5: Special options _terms, _raw, _list
    doc = {
        'plugin': 'test_plugin',
        'options': {
            '_terms': {
                'type': 'string',
                'description': 'A special option',
                'required': True
            }
        }
    }
    result = _do_lookup_snippet(doc)
    assert result == [
        "# _terms(string): A special option",
        "",
        "lookup('test_plugin', < _terms >)"
    ]
