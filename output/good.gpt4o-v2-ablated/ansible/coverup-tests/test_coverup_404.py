# file: lib/ansible/cli/doc.py:1305-1347
# asked: {"lines": [1306, 1308, 1309, 1311, 1313, 1314, 1317, 1319, 1320, 1321, 1323, 1324, 1325, 1326, 1328, 1330, 1331, 1332, 1334, 1335, 1336, 1337, 1338, 1340, 1341, 1343, 1345, 1347], "branches": [[1311, 1313], [1311, 1317], [1323, 1324], [1323, 1347], [1325, 1326], [1325, 1328], [1331, 1332], [1331, 1334], [1335, 1336], [1335, 1340], [1336, 1337], [1336, 1338], [1340, 1341], [1340, 1343]]}
# gained: {"lines": [1306, 1308, 1309, 1311, 1313, 1314, 1317, 1319, 1320, 1321, 1323, 1324, 1325, 1326, 1328, 1330, 1331, 1332, 1334, 1335, 1336, 1337, 1338, 1340, 1341, 1343, 1345, 1347], "branches": [[1311, 1313], [1311, 1317], [1323, 1324], [1323, 1347], [1325, 1326], [1325, 1328], [1331, 1332], [1331, 1334], [1335, 1336], [1335, 1340], [1336, 1337], [1336, 1338], [1340, 1341], [1340, 1343]]}

import pytest
from unittest.mock import patch
import textwrap

# Mocking the necessary parts of the ansible/cli/doc.py module
class DocCLI:
    @staticmethod
    def tty_ify(text):
        return text

class display:
    columns = 80

string_types = str

@pytest.fixture
def doc_with_module():
    return {
        'short_description': 'Test short description',
        'module': 'test_module',
        'options': {
            'option1': {
                'description': 'Option 1 description',
                'required': True
            },
            'option2': {
                'description': ['Option 2', 'description'],
                'required': False
            }
        }
    }

@pytest.fixture
def doc_without_module():
    return {
        'short_description': 'Test short description',
        'plugin': 'test_plugin',
        'options': {
            'option1': {
                'description': 'Option 1 description',
                'required': True
            },
            'option2': {
                'description': ['Option 2', 'description'],
                'required': False
            }
        }
    }

@pytest.fixture
def doc_with_invalid_required():
    return {
        'short_description': 'Test short description',
        'module': 'test_module',
        'options': {
            'option1': {
                'description': 'Option 1 description',
                'required': 'yes'  # Invalid boolean
            }
        }
    }

def test_do_yaml_snippet_with_module(doc_with_module):
    from ansible.cli.doc import _do_yaml_snippet

    result = _do_yaml_snippet(doc_with_module)
    assert result == [
        '- name: Test short description',
        '  test_module:',
        '      option1:               # (required) Option 1 description',
        '      option2:               # Option 2 description'
    ]

def test_do_yaml_snippet_without_module(doc_without_module):
    from ansible.cli.doc import _do_yaml_snippet

    result = _do_yaml_snippet(doc_without_module)
    assert result == [
        '# test_plugin:',
        'option1: (required) # Option 1 description',
        'option2: None      # Option 2 description'
    ]

def test_do_yaml_snippet_invalid_required(doc_with_invalid_required):
    from ansible.cli.doc import _do_yaml_snippet

    with pytest.raises(ValueError, match="Incorrect value for 'Required', a boolean is needed: yes"):
        _do_yaml_snippet(doc_with_invalid_required)
