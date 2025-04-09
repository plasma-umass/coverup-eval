# file lib/ansible/cli/doc.py:1305-1347
# lines [1305, 1306, 1308, 1309, 1311, 1313, 1314, 1317, 1319, 1320, 1321, 1323, 1324, 1325, 1326, 1328, 1330, 1331, 1332, 1334, 1335, 1336, 1337, 1338, 1340, 1341, 1343, 1345, 1347]
# branches ['1311->1313', '1311->1317', '1323->1324', '1323->1347', '1325->1326', '1325->1328', '1331->1332', '1331->1334', '1335->1336', '1335->1340', '1336->1337', '1336->1338', '1340->1341', '1340->1343']

import pytest
from unittest.mock import patch
from ansible.cli.doc import DocCLI, display, string_types
import textwrap

def _do_yaml_snippet(doc):
    text = []

    mdesc = DocCLI.tty_ify(doc['short_description'])
    module = doc.get('module')

    if module:
        # this is actually a usable task!
        text.append("- name: %s" % (mdesc))
        text.append("  %s:" % (module))
    else:
        # just a comment, hopefully useful yaml file
        text.append("# %s:" % doc.get('plugin', doc.get('name')))

    pad = 29
    subdent = '# '.rjust(pad + 2)
    limit = display.columns - pad

    for o in sorted(doc['options'].keys()):
        opt = doc['options'][o]
        if isinstance(opt['description'], string_types):
            desc = DocCLI.tty_ify(opt['description'])
        else:
            desc = DocCLI.tty_ify(" ".join(opt['description']))

        required = opt.get('required', False)
        if not isinstance(required, bool):
            raise ValueError("Incorrect value for 'Required', a boolean is needed: %s" % required)

        o = '%s:' % o
        if module:
            if required:
                desc = "(required) %s" % desc
            text.append("      %-20s   # %s" % (o, textwrap.fill(desc, limit, subsequent_indent=subdent)))
        else:
            if required:
                default = '(required)'
            else:
                default = opt.get('default', 'None')

            text.append("%s %-9s # %s" % (o, default, textwrap.fill(desc, limit, subsequent_indent=subdent, max_lines=3)))

    return text

@pytest.fixture
def mock_display_columns(mocker):
    mocker.patch.object(display, 'columns', 80)

def test_do_yaml_snippet_module(mock_display_columns):
    doc = {
        'short_description': 'Test module',
        'module': 'test_module',
        'options': {
            'option1': {
                'description': 'This is a test option',
                'required': True
            },
            'option2': {
                'description': ['This is another test option'],
                'required': False
            }
        }
    }

    result = _do_yaml_snippet(doc)
    expected = [
        "- name: Test module",
        "  test_module:",
        "      option1:               # (required) This is a test option",
        "      option2:               # This is another test option"
    ]
    assert result == expected

def test_do_yaml_snippet_plugin(mock_display_columns):
    doc = {
        'short_description': 'Test plugin',
        'plugin': 'test_plugin',
        'options': {
            'option1': {
                'description': 'This is a test option',
                'required': True
            },
            'option2': {
                'description': ['This is another test option'],
                'required': False,
                'default': 'default_value'
            }
        }
    }

    result = _do_yaml_snippet(doc)
    expected = [
        "# test_plugin:",
        "option1: (required) # This is a test option",
        "option2: default_value # This is another test option"
    ]
    assert result == expected

def test_do_yaml_snippet_invalid_required(mock_display_columns):
    doc = {
        'short_description': 'Test invalid required',
        'module': 'test_invalid_required',
        'options': {
            'option1': {
                'description': 'This is a test option',
                'required': 'yes'  # Invalid boolean value
            }
        }
    }

    with pytest.raises(ValueError, match="Incorrect value for 'Required', a boolean is needed: yes"):
        _do_yaml_snippet(doc)
