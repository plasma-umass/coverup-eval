# file: lib/ansible/cli/doc.py:515-517
# asked: {"lines": [515, 516, 517], "branches": []}
# gained: {"lines": [515, 516, 517], "branches": []}

import pytest
from unittest.mock import patch, mock_open
import pkgutil
from ansible.cli.doc import DocCLI

@pytest.fixture
def mock_pkgutil_get_data(monkeypatch):
    mock_data = b"key: value"
    monkeypatch.setattr(pkgutil, 'get_data', lambda *args, **kwargs: mock_data)
    return mock_data

def test_list_keywords(mock_pkgutil_get_data):
    result = DocCLI._list_keywords()
    assert result == {'key': 'value'}
