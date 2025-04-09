# file: lib/ansible/cli/doc.py:1305-1347
# asked: {"lines": [1328], "branches": [[1325, 1328]]}
# gained: {"lines": [1328], "branches": [[1325, 1328]]}

import pytest
from ansible.cli.doc import _do_yaml_snippet
from ansible.module_utils.six import string_types

class MockDisplay:
    columns = 80

class MockDocCLI:
    @classmethod
    def tty_ify(cls, text):
        return text

@pytest.fixture
def mock_display(monkeypatch):
    monkeypatch.setattr("ansible.cli.doc.display", MockDisplay)

@pytest.fixture
def mock_doccli(monkeypatch):
    monkeypatch.setattr("ansible.cli.doc.DocCLI", MockDocCLI)

def test_do_yaml_snippet_with_module(mock_display, mock_doccli):
    doc = {
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
    result = _do_yaml_snippet(doc)
    assert result == [
        "- name: Test short description",
        "  test_module:",
        "      option1:               # (required) Option 1 description",
        "      option2:               # Option 2 description"
    ]

def test_do_yaml_snippet_without_module(mock_display, mock_doccli):
    doc = {
        'short_description': 'Test short description',
        'plugin': 'test_plugin',
        'options': {
            'option1': {
                'description': 'Option 1 description',
                'required': True
            },
            'option2': {
                'description': ['Option 2', 'description'],
                'required': False,
                'default': 'default_value'
            }
        }
    }
    result = _do_yaml_snippet(doc)
    assert result == [
        "# test_plugin:",
        "option1: (required) # Option 1 description",
        "option2: default_value # Option 2 description"
    ]

def test_do_yaml_snippet_invalid_required(mock_display, mock_doccli):
    doc = {
        'short_description': 'Test short description',
        'module': 'test_module',
        'options': {
            'option1': {
                'description': 'Option 1 description',
                'required': 'yes'
            }
        }
    }
    with pytest.raises(ValueError, match="Incorrect value for 'Required', a boolean is needed: yes"):
        _do_yaml_snippet(doc)
